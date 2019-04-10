import datetime
import logging
import logging.handlers
import os
from flask import Flask, request, render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_security import login_required
from flask_login import current_user
from flask_cors import CORS
from jinja2.exceptions import TemplateNotFound
from importlib import reload

from .external_connector import ExternalConnector
from .workers import MeltanoBackgroundCompiler, UIAvailableWorker
from . import config as default_config

from meltano.core.project import Project, ProjectNotFound
from meltano.core.projects import Projects
from meltano.core.compiler.project_compiler import ProjectCompiler

connector = ExternalConnector()
logger = logging.getLogger(__name__)


def create_app(config={}):
    try:
        project = Project.find()
    except ProjectNotFound as e:
        project = None

    projects = Projects()
    app = Flask(__name__)
    app.config.from_object(reload(default_config))
    app.config.update(**config)

    if project:
        meltano_db_path = project.root.joinpath("meltano.db")
    else:
        meltano_db_path = projects.meltano_projects_dir.joinpath("meltano.db")
    if not app.config["SQLALCHEMY_DATABASE_URI"]:
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{meltano_db_path}"

    # Initial compilation
    if project:
        compiler = ProjectCompiler(project)
    try:
        compiler.compile()
    except Exception as e:
        pass

    # Logging
    file_handler = logging.handlers.RotatingFileHandler(
        app.config["LOG_PATH"], maxBytes=2000, backupCount=10
    )
    stdout_handler = logging.StreamHandler()

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    now = str(datetime.datetime.utcnow().strftime("%b %d %Y %I:%M:%S:%f"))
    logger.warning(f"Meltano UI started at: {now}")

    # Extensions
    security_options = {}

    from .models import db
    from .mail import mail
    from .security import security, users, setup_security
    from .security.oauth import setup_oauth

    db.init_app(app)
    mail.init_app(app)
    setup_security(app, project)
    setup_oauth(app)
    CORS(app, origins="*")

    from .controllers.root import root
    from .controllers.projects import projectsBP
    from .controllers.dashboards import dashboardsBP
    from .controllers.reports import reportsBP
    from .controllers.repos import reposBP
    from .controllers.settings import settingsBP
    from .controllers.sql import sqlBP

    app.register_blueprint(root)
    app.register_blueprint(projectsBP)
    app.register_blueprint(dashboardsBP)
    app.register_blueprint(reportsBP)
    app.register_blueprint(reposBP)
    app.register_blueprint(settingsBP)
    app.register_blueprint(sqlBP)

    if app.config["PROFILE"]:
        from .profiler import init

        init(app)

    @app.after_request
    def after_request(res):
        request_message = f"[{request.url}]"

        if request.method != "OPTIONS":
            request_message += f" as {current_user}"

        logger.info(request_message)
        return res

    return app


def start(project, **kwargs):
    """Start Meltano UI as a single-threaded web server."""
    starting_url = "projects"

    available_worker = UIAvailableWorker(
        f"http://localhost:5000/{starting_url}", not kwargs.get("use_reloader", False)
    )
    if project:
        compiler_worker = MeltanoBackgroundCompiler(project)
        compiler_worker.start()

    available_worker.start()

    try:
        app_config = kwargs.pop("app_config", {})
        app = create_app(app_config)
        from .security.identity import create_dev_user

        with app.app_context():
            # TODO: alembic migration
            create_dev_user()

        app.run(**kwargs)
    finally:
        if project:
            compiler_worker.stop()

        available_worker.stop()
