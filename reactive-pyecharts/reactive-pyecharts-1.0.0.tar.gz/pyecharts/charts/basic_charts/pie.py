# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Optional, Sequence, Union
from ...globals import ChartType


class Pie(Chart):
    """
    <<< 饼图 >>>

    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        *,
        color: Optional[str] = None,
        radius: Optional[Sequence] = None,
        center: Optional[Sequence] = None,
        rosetype: Optional[str] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

        data = [{"name": n, "value": v} for n, v in data_pair]

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        self._append_color(color)
        for a, _ in data_pair:
            self.options.get("legend")[0].get("data").append(a)

        _dlst = self.options.get("legend")[0].get("data")
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": ChartType.PIE,
                "name": series_name,
                "data": data,
                "radius": radius,
                "center": center,
                "roseType": rosetype,
                "label": label_opts,
                "tooltip": tooltip_opts,
            }
        )
        return self
