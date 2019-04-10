import numpy as np

from holoviews.core.dimension import Dimension
from holoviews.element import Labels

try:
    from bokeh.models import LinearColorMapper, CategoricalColorMapper
except:
    pass

from ..utils import ParamLogStream
from .testplot import TestBokehPlot, bokeh_renderer


class TestLabelsPlot(TestBokehPlot):

    def test_labels_simple(self):
        labels = Labels([(0, 1, 'A'), (1, 0, 'B')])
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        expected = {'x': np.array([0, 1]), 'y': np.array([1, 0]),
                    'Label': ['A', 'B']}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'x')
        self.assertEqual(glyph.y, 'y')
        self.assertEqual(glyph.text, 'Label')

    def test_labels_empty(self):
        labels = Labels([])
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        expected = {'x': np.array([]), 'y': np.array([]), 'Label': []}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'x')
        self.assertEqual(glyph.y, 'y')
        self.assertEqual(glyph.text, 'Label')

    def test_labels_formatter(self):
        vdim = Dimension('text', value_format=lambda x: '%.1f' % x)
        labels = Labels([(0, 1, 0.33333), (1, 0, 0.66666)], vdims=vdim)
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        expected = {'x': np.array([0, 1]), 'y': np.array([1, 0]),
                    'text': ['0.3', '0.7']}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'x')
        self.assertEqual(glyph.y, 'y')
        self.assertEqual(glyph.text, 'text')

    def test_labels_inverted(self):
        labels = Labels([(0, 1, 'A'), (1, 0, 'B')]).options(invert_axes=True)
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        expected = {'x': np.array([0, 1]), 'y': np.array([1, 0]), 'Label': ['A', 'B']}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'y')
        self.assertEqual(glyph.y, 'x')
        self.assertEqual(glyph.text, 'Label')

    def test_labels_color_mapped_text_vals(self):
        labels = Labels([(0, 1, 0.33333), (1, 0, 0.66666)]).options(color_index=2)
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        cmapper = plot.handles['color_mapper']
        expected = {'x': np.array([0, 1]), 'y': np.array([1, 0]),
                    'Label': ['0.33333', '0.66666'],
                    'text_color': np.array([0.33333, 0.66666])}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'x')
        self.assertEqual(glyph.y, 'y')
        self.assertEqual(glyph.text, 'Label')
        self.assertEqual(glyph.text_color, {'field': 'text_color', 'transform': cmapper})
        self.assertEqual(cmapper.low, 0.33333)
        self.assertEqual(cmapper.high, 0.66666)

    def test_labels_color_mapped(self):
        labels = Labels([(0, 1, 0.33333, 2), (1, 0, 0.66666, 1)], vdims=['text', 'color']).options(color_index=3)
        plot = bokeh_renderer.get_plot(labels)
        source = plot.handles['source']
        glyph = plot.handles['glyph']
        cmapper = plot.handles['color_mapper']
        expected = {'x': np.array([0, 1]), 'y': np.array([1, 0]),
                    'text': ['0.33333', '0.66666'],
                    'color': np.array([2, 1])}
        for k, vals in expected.items():
            self.assertEqual(source.data[k], vals)
        self.assertEqual(glyph.x, 'x')
        self.assertEqual(glyph.y, 'y')
        self.assertEqual(glyph.text, 'text')
        self.assertEqual(glyph.text_color, {'field': 'color', 'transform': cmapper})
        self.assertEqual(cmapper.low, 1)
        self.assertEqual(cmapper.high, 2)

    ###########################
    #    Styling mapping      #
    ###########################

    def test_label_color_op(self):
        labels = Labels([(0, 0, '#000'), (0, 1, '#F00'), (0, 2, '#0F0')],
                        vdims='color').options(text_color='color')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        self.assertEqual(cds.data['text_color'], np.array(['#000', '#F00', '#0F0']))
        self.assertEqual(glyph.text_color, {'field': 'text_color'})

    def test_label_linear_color_op(self):
        labels = Labels([(0, 0, 0), (0, 1, 1), (0, 2, 2)],
                        vdims='color').options(text_color='color')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        cmapper = plot.handles['text_color_color_mapper']
        self.assertTrue(cmapper, LinearColorMapper)
        self.assertEqual(cmapper.low, 0)
        self.assertEqual(cmapper.high, 2)
        self.assertEqual(cds.data['text_color'], np.array([0, 1, 2]))
        self.assertEqual(glyph.text_color, {'field': 'text_color', 'transform': cmapper})

    def test_label_categorical_color_op(self):
        labels = Labels([(0, 0, 'A'), (0, 1, 'B'), (0, 2, 'C')],
                        vdims='color').options(text_color='color')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        cmapper = plot.handles['text_color_color_mapper']
        self.assertTrue(cmapper, CategoricalColorMapper)
        self.assertEqual(cmapper.factors, ['A', 'B', 'C'])
        self.assertEqual(cds.data['text_color'], np.array(['A', 'B', 'C']))
        self.assertEqual(glyph.text_color, {'field': 'text_color', 'transform': cmapper})

    def test_label_angle_op(self):
        labels = Labels([(0, 0, 0), (0, 1, 45), (0, 2, 90)],
                        vdims='angle').options(angle='angle')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        self.assertEqual(cds.data['angle'], np.array([0, 0.785398, 1.570796]))
        self.assertEqual(glyph.angle, {'field': 'angle'})

    def test_label_alpha_op(self):
        labels = Labels([(0, 0, 0), (0, 1, 0.2), (0, 2, 0.7)],
                        vdims='alpha').options(text_alpha='alpha')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        self.assertEqual(cds.data['text_alpha'], np.array([0, 0.2, 0.7]))
        self.assertEqual(glyph.text_alpha, {'field': 'text_alpha'})

    def test_label_font_size_op_strings(self):
        labels = Labels([(0, 0, '10pt'), (0, 1, '4pt'), (0, 2, '8pt')],
                        vdims='size').options(text_font_size='size')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        self.assertEqual(cds.data['text_font_size'], np.array(['10pt', '4pt', '8pt']))
        self.assertEqual(glyph.text_font_size, {'field': 'text_font_size'})

    def test_label_font_size_op_ints(self):
        labels = Labels([(0, 0, 10), (0, 1, 4), (0, 2, 8)],
                        vdims='size').options(text_font_size='size')
        plot = bokeh_renderer.get_plot(labels)
        cds = plot.handles['cds']
        glyph = plot.handles['glyph']
        self.assertEqual(cds.data['text_font_size'], ['10pt', '4pt', '8pt'])
        self.assertEqual(glyph.text_font_size, {'field': 'text_font_size'})

    def test_labels_color_index_color_clash(self):
        labels = Labels([(0, 0, 0), (0, 1, 1), (0, 2, 2)],
                        vdims='color').options(text_color='color', color_index='color')        
        with ParamLogStream() as log:
            bokeh_renderer.get_plot(labels)
        log_msg = log.stream.read()
        warning = ("Cannot declare style mapping for 'text_color' option "
                   "and declare a color_index; ignoring the color_index.\n")
        self.assertEqual(log_msg, warning)
