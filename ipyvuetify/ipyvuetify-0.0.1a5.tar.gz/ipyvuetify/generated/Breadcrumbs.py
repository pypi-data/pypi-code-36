from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .VuetifyWidget import VuetifyWidget


class Breadcrumbs(VuetifyWidget):

    _model_name = Unicode('BreadcrumbsModel').tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    divider = Unicode(None, allow_none=True).tag(sync=True)

    items = List(None, allow_none=True).tag(sync=True)

    justify_center = Bool(None, allow_none=True).tag(sync=True)

    justify_end = Bool(None, allow_none=True).tag(sync=True)

    large = Bool(None, allow_none=True).tag(sync=True)

    light = Bool(None, allow_none=True).tag(sync=True)


Breadcrumbs.items.default_value=None



__all__ = ['Breadcrumbs']
