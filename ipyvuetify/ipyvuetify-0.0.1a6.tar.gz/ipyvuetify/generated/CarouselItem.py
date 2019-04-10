from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .VuetifyWidget import VuetifyWidget


class CarouselItem(VuetifyWidget):

    _model_name = Unicode('CarouselItemModel').tag(sync=True)

    active_class = Unicode(None, allow_none=True).tag(sync=True)

    disabled = Bool(None, allow_none=True).tag(sync=True)

    lazy = Bool(None, allow_none=True).tag(sync=True)

    reverse_transition = Union([
        Bool(),
        Unicode()
    ], default_value=None, allow_none=True).tag(sync=True)

    transition = Union([
        Bool(),
        Unicode()
    ], default_value=None, allow_none=True).tag(sync=True)

    value = Any(Undefined).tag(sync=True)





__all__ = ['CarouselItem']
