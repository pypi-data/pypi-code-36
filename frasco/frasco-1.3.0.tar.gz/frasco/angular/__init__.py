from frasco.ext import *
from frasco.assets import expose_package, register_assets_builder
from frasco.utils import join_url_rule
from flask import render_template
import os
import json
import re
import htmlmin
import codecs


class FrascoAngular(Extension):
    name = "angular"
    defaults = {"static_dir": None, # defaults to app.static_folder
                "static_url_path": None, # defaults to app.static_url_path
                "angular_template": "angular_layout.html",
                "app_dir": "app",
                "services_module": "services",
                "services_name": "%s",
                "templates_file": None,
                "templates_module": "templatesCache",
                "disable_templates_cache": None, # app.debug
                "templates_matcher": r".*\.html$",
                "add_app_dir_in_babel_extract": True}

    def _init_app(self, app, state):
        require_extension('frasco_assets', app)
        expose_package(app, "frasco_angular", __name__)

        if not state.options["static_dir"]:
            state.options["static_dir"] = app.static_folder
        if not state.options["static_url_path"]:
            state.options["static_url_path"] = app.static_url_path

        if state.options['templates_file']:
            register_assets_builder(self.build_templates)

        if has_extension('frasco_babel', app) and state.options['add_app_dir_in_babel_extract']:
            app.extensions.frasco_babel.add_extract_dir(os.path.join(state.options['static_dir'], state.options['app_dir']),
                '.', ['frasco.angular.babel.AngularCompatExtension'], [('javascript:**.js', {})])

    @ext_stateful_method
    def add_route(self, state, endpoint, rule, decorators=None, **options):
        rules = rule if isinstance(rule, (list, tuple)) else [rule]
        def func(*args, **kwargs):
            return render_template(state.options['angular_template'])
        if decorators:
            for decorator in reversed(decorators):
                func = decorator(func)
        for rule in rules:
            self.get_app().add_url_rule(rule, endpoint, func, **options)

    @ext_stateful_method
    def register_service_builder(self, state, api_version, filename):
        def builder():
            module = ("/* This file is auto-generated by frasco-angular. DO NOT MODIFY. */\n'use strict';\n"
                    "\n(function() {\n\nvar services = angular.module('%s', ['frasco']);\n") % state.options["services_module"]

            for service in api_version.iter_services():
                endpoints = {}
                for rule, endpoint, func, options in service.iter_endpoints():
                    args = []
                    if hasattr(func, 'request_params'):
                        for p in reversed(func.request_params):
                            args.extend(p.names)
                    endpoints[endpoint] = [_convert_url_args(join_url_rule(service.url_prefix, rule)), args]
                module += ("\nservices.factory('%s', ['frascoServiceFactory', function(frascoServiceFactory) {\n"
                        "return frascoServiceFactory.make('%s', '%s', [], %s);\n}]);\n") % \
                            (state.options['services_name'] % service.name, service.name, api_version.url_prefix,
                            json.dumps(endpoints, indent=2))

            module += "\n})();";
            _write_file(os.path.join(state.options["static_dir"], state.options["app_dir"], filename), module)
        register_assets_builder(builder)

    @ext_stateful_method
    def build_templates(self, state):
        module = [("/* This file is auto-generated by frasco-angular. DO NOT MODIFY. */\n'use strict';\n"
                  "\nangular.module('%s', []).run(['$templateCache', function($templateCache) {") % state.options["templates_module"]]
        matcher = re.compile(state.options["templates_matcher"], re.I)
        done = set()

        def process_file(filename, path=None, content=None):
            if not path:
                pathname = filename
                path = os.path.dirname(filename)
                filename = os.path.basename(filename)
            else:
                pathname = os.path.join(path, filename)
            relname = state.options["static_url_path"] + "/" + os.path.relpath(path, state.options["static_dir"]) + "/" + filename
            if pathname not in done and matcher.match(relname):
                if not content:
                    with codecs.open(pathname, 'r', 'utf-8') as f:
                        content = f.read()
                module.append("  $templateCache.put('%s', %s);" % (relname, json.dumps(htmlmin.minify(content))))
                done.add(pathname)

        disable = state.options["disable_templates_cache"]
        if (disable is None and not self.get_app().debug) or disable is False:
            for path, dirnames, filenames in os.walk(os.path.join(state.options["static_dir"], state.options['app_dir'])):
                for filename in filenames:
                    process_file(filename, path)

        module = "\n".join(module) + "\n}]);"
        filename = os.path.join(state.options["static_dir"], state.options["app_dir"], state.options['templates_file'])
        _write_file(filename, module)


_url_arg_re = re.compile(r"<([a-z]+:)?([a-z0-9_]+)>")
def _convert_url_args(url):
    return _url_arg_re.sub(r":\2", url)


def _write_file(filename, source):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with codecs.open(filename, "w", "utf-8") as f:
        f.write(source)
