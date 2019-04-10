from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .VuetifyWidget import VuetifyWidget


class Dialog(VuetifyWidget):

    _model_name = Unicode('DialogModel').tag(sync=True)

    attach = Any(Undefined).tag(sync=True)

    content_class = Any(Undefined).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    disabled = Bool(None, allow_none=True).tag(sync=True)

    full_width = Bool(None, allow_none=True).tag(sync=True)

    fullscreen = Bool(None, allow_none=True).tag(sync=True)

    hide_overlay = Bool(None, allow_none=True).tag(sync=True)

    lazy = Bool(None, allow_none=True).tag(sync=True)

    light = Bool(None, allow_none=True).tag(sync=True)

    max_width = Union([
        Unicode(),
        Float()
    ], default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(None, allow_none=True).tag(sync=True)

    origin = Unicode(None, allow_none=True).tag(sync=True)

    persistent = Bool(None, allow_none=True).tag(sync=True)

    return_value = Any(Undefined).tag(sync=True)

    scrollable = Bool(None, allow_none=True).tag(sync=True)

    transition = Union([
        Unicode(),
        Bool()
    ], default_value=None, allow_none=True).tag(sync=True)

    value = Any(Undefined).tag(sync=True)

    width = Union([
        Unicode(),
        Float()
    ], default_value=None, allow_none=True).tag(sync=True)





__all__ = ['Dialog']
