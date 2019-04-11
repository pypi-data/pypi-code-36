# coding=utf-8
import datetime
import json
import os
import uuid

from jinja2 import Environment

from ..commons import utils
from ..commons.types import Optional, Union
from ..datasets import FILENAMES
from ..globals import CurrentConfig, NotebookType, ThemeType
from ..options import InitOpts
from ..render.display import HTML, Javascript
from ..render.engine import RenderEngine


class Base:
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        self.width = init_opts.width
        self.height = init_opts.height
        self.renderer = init_opts.renderer
        self.page_title = init_opts.page_title
        self.theme = init_opts.theme
        self.chart_id = init_opts.chart_id or uuid.uuid4().hex

        self.options: dict = {}
        self.js_host: str = init_opts.js_host or CurrentConfig.ONLINE_HOST
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_dependencies: utils.OrderedSet = utils.OrderedSet("echarts")

    @staticmethod
    def produce_js_func(fn: str) -> str:
        return utils.filter_js_func(fn)

    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)

    def get_options(self) -> dict:
        return utils.remove_key_with_none_value(self.options)

    def dump_options(self) -> str:
        return json.dumps(self.get_options(), indent=4, default=default)

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_chart.html",
        env: Optional[Environment] = None,
    ) -> str:
        self.json_contents = self.dump_options()
        self._use_theme()
        RenderEngine(env).render_chart_to_file(
            chart=self, path=path, template_name=template_name
        )
        return os.path.abspath(path)

    def _use_theme(self):
        if self.theme not in ThemeType.BUILTIN_THEMES:
            self.js_dependencies.add(self.theme)

    def render_notebook(self):
        self.chart_id = uuid.uuid4().hex
        self.json_contents = self.dump_options()
        self._use_theme()
        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
            require_config = utils.produce_require_dict(
                self.js_dependencies, self.js_host
            )
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_notebook.html",
                    charts=(self,),
                    config_items=require_config["config_items"],
                    libraries=require_config["libraries"],
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_lab.html", charts=(self,)
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
            pass

    def load_javascript(self):
        scripts = []
        for dep in self.js_dependencies.items:
            f, ext = FILENAMES[dep]
            scripts.append("{}{}.{}".format(CurrentConfig.ONLINE_HOST, f, ext))
        return Javascript(lib=scripts)


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
