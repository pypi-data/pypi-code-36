from __future__ import absolute_import, division, unicode_literals

import numpy as np

from bokeh.models import WMTSTileSource, BBoxTileSource, QUADKEYTileSource, SaveTool

from ...core import util
from ...core.options import SkipRendering
from ...element.tiles import _ATTRIBUTIONS
from .element import ElementPlot


class TilePlot(ElementPlot):

    style_opts = ['alpha', 'render_parents', 'level', 'smoothing', 'min_zoom', 'max_zoom']

    def get_extents(self, element, ranges, range_type='combined'):
        extents = super(TilePlot, self).get_extents(element, ranges, range_type)
        if (not self.overlaid and all(e is None or not np.isfinite(e) for e in extents)
            and range_type in ('combined', 'data')):
            x0, x1 = (-20037508.342789244, 20037508.342789244)
            y0, y1 = (-20037508.342789255, 20037508.342789244)
            global_extent = (x0, y0, x1, y1)
            return global_extent
        return extents

    def get_data(self, element, ranges, style):
        if not isinstance(element.data, util.basestring):
            SkipRendering("WMTS element data must be a URL string, "
                          "bokeh cannot render %r" % element.data)
        if '{Q}' in element.data:
            tile_source = QUADKEYTileSource
        elif all(kw in element.data for kw in ('{XMIN}', '{XMAX}', '{YMIN}', '{YMAX}')):
            tile_source = BBoxTileSource
        elif all(kw in element.data for kw in ('{X}', '{Y}', '{Z}')):
            tile_source = WMTSTileSource
        else:
            raise ValueError('Tile source URL format not recognized. '
                             'Must contain {X}/{Y}/{Z}, {XMIN}/{XMAX}/{YMIN}/{YMAX} '
                             'or {Q} template strings.')
        params = {'url': element.data}
        for zoom in ('min_zoom', 'max_zoom'):
            if zoom in style:
                params[zoom] = style[zoom]
        for key, attribution in _ATTRIBUTIONS.items():
            if all(k in element.data for k in key):
                params['attribution'] = attribution
        return {}, {'tile_source': tile_source(**params)}, style

    def _update_glyph(self, renderer, properties, mapping, glyph, source=None, data=None):
        glyph.url = mapping['tile_source'].url
        glyph.update(**{k: v for k, v in properties.items()
                           if k in glyph.properties()})
        renderer.update(**{k: v for k, v in properties.items()
                           if k in renderer.properties()})

    def _init_glyph(self, plot, mapping, properties):
        """
        Returns a Bokeh glyph object.
        """
        tile_source = mapping['tile_source']
        level = properties.pop('level', 'glyph')
        renderer = plot.add_tile(tile_source, level=level)
        renderer.alpha = properties.get('alpha', 1)

        # Remove save tool
        plot.tools = [t for t in plot.tools if not isinstance(t, SaveTool)]
        return renderer, tile_source
