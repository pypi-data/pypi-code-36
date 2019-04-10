"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
from concurrent.futures import Future
import dateutil
import pandas as pd
from typing import Iterable, List, Union
from gs_quant.target.risk import RiskMeasure, RiskMeasureType, RiskMeasureUnit, RiskPosition, RiskRequest
from gs_quant.common import AssetClass
from gs_quant.datetime import point_sort_order
from gs_quant.markets.core import PricingContext
from typing import Optional


__field_sort_fns = {
    'point': point_sort_order
}
__field_order = ('date', 'marketDataType', 'assetId', 'pointClass', 'point', 'value')


def sum_formatter(result: List) -> float:
    return sum(r.get('value', result[0].get('Val')) for r in result)


def scalar_formatter(result: List) -> Optional[Union[float, pd.Series]]:
    if not result:
        return None

    if 'date' in result[0]:
        series = pd.Series(
            data=[r.get('value', r.get('Val')) for r in result],
            index=[dateutil.parser.isoparse(r['date']).date() for r in result]
        )
        return series.sort_index()
    else:
        return result[0].get('value', result[0].get('Val'))


def structured_formatter(result: List) -> pd.DataFrame:
    return sort_risk(pd.DataFrame(result))


def aggregate_risk(results: Iterable[Union[pd.DataFrame, Future]], threshold: Optional[float]=None) -> pd.DataFrame:
    """
    Combine the results of multiple Instrument.calc() calls, into a single result

    :param results: An iterable of Dataframes and/or Futures (returned by Instrument.calc())
    :param threshold: exclude values whose absolute value falls below this threshold
    :return: A Dataframe with the aggregated results

    **Examples**

    >>> with PricingContext():
    >>>     delta_f = [inst.calc(risk.IRDelta) for inst in instruments]
    >>>     vega_f = [inst.calc(risk.IRVega) for inst in instruments]
    >>>
    >>> delta = aggregate_risk(delta_f, threshold=0.1)
    >>> vega = aggregate_risk(vega_f)

    delta_f and vega_f are lists of futures, where the result will be a Dataframe
    delta and vega are Dataframes, representing the merged risk of the individual instruments
    """
    dfs = [r.result() if isinstance(r, Future) else r for r in results]
    result = pd.concat(dfs)
    result = result.groupby([c for c in result.columns if c != 'value']).sum()
    result = pd.DataFrame.from_records(result.to_records())

    if threshold is not None:
        result = result[result.value.abs() > threshold]

    return sort_risk(result)


def sort_risk(df: pd.DataFrame, by=('date', 'marketDataType', 'assetId', 'point')):
    """
    Sort bucketed risk
    :param df: Input Dataframe
    :param by: Columns to sort by
    :return: A sorted Dataframe
    """
    columns = tuple(df.columns)
    indices = [columns.index(c) if c in columns else -1 for c in by]
    fns = [__field_sort_fns.get(c) for c in columns]

    def cmp(row) -> tuple:
        return tuple(fns[i](row[i]) if fns[i] else row[i] for i in indices if i != -1)

    data = sorted((tuple(r)[1:] for r in df.to_records()), key=cmp)
    return pd.DataFrame.from_records(data, columns=columns)[[f for f in __field_order if f in columns]]


def __risk_measure_with_doc_string(doc: str, measureType: RiskMeasureType, assetClass: AssetClass=None, unit: RiskMeasureUnit=None) -> RiskMeasure:
    measure = RiskMeasure(measureType=measureType, assetClass=assetClass, unit=unit)
    measure.__doc__ = doc
    return measure


DollarPrice = __risk_measure_with_doc_string('Present value in USD', RiskMeasureType.Dollar_Price)
Price = __risk_measure_with_doc_string('Present value in local currency', RiskMeasureType.PV)
ForwardPrice = __risk_measure_with_doc_string('Forward price', RiskMeasureType.Forward_Price, unit=RiskMeasureUnit.BPS)
Theta = __risk_measure_with_doc_string('1 day Theta', RiskMeasureType.Theta)
EqDelta = __risk_measure_with_doc_string('Equity Delta', RiskMeasureType.Delta, assetClass=AssetClass.Equity)
EqGamma = __risk_measure_with_doc_string('Equity Gamma', RiskMeasureType.Gamma, assetClass=AssetClass.Equity)
EqVega = __risk_measure_with_doc_string('Equity Vega', RiskMeasureType.Vega, assetClass=AssetClass.Equity)
EqSpot = __risk_measure_with_doc_string('Equity Spot Level', RiskMeasureType.Spot, assetClass=AssetClass.Equity)
CommodDelta = __risk_measure_with_doc_string('Commodity Delta', RiskMeasureType.Delta, assetClass=AssetClass.Commod)
CommodTheta = __risk_measure_with_doc_string('Commodity Theta', RiskMeasureType.Theta, assetClass=AssetClass.Commod)
CommodVega = __risk_measure_with_doc_string('Commodity Vega', RiskMeasureType.Vega, assetClass=AssetClass.Commod)
FXDelta = __risk_measure_with_doc_string('FX Delta', RiskMeasureType.Delta, assetClass=AssetClass.FX)
FXGamma = __risk_measure_with_doc_string('FX Gamma', RiskMeasureType.Gamma, assetClass=AssetClass.FX)
FXVega = __risk_measure_with_doc_string('FX Vega', RiskMeasureType.Vega, assetClass=AssetClass.FX)
FXSpot = __risk_measure_with_doc_string('FX Spot Rate', RiskMeasureType.Spot, assetClass=AssetClass.FX)
IRDelta = __risk_measure_with_doc_string('Interest Rate Delta', RiskMeasureType.Delta, assetClass=AssetClass.Rates)
IRDeltaLocalCcy = __risk_measure_with_doc_string('Interest Rate Delta', RiskMeasureType.DeltaLocalCcy, assetClass=AssetClass.Rates)
IRGamma = __risk_measure_with_doc_string('Interest Rate', RiskMeasureType.Gamma, assetClass=AssetClass.Rates)
IRVega = __risk_measure_with_doc_string('Interest Rate Gamma', RiskMeasureType.Vega, assetClass=AssetClass.Rates)
IRVegaLocalCcy = __risk_measure_with_doc_string('Interest Rate Vega', RiskMeasureType.VegaLocalCcy, assetClass=AssetClass.Rates)
IRAnnualImpliedVol = __risk_measure_with_doc_string('Interest Rate Annual Implied Volatility (%)', RiskMeasureType.Annual_Implied_Volatility, assetClass=AssetClass.Rates, unit=RiskMeasureUnit.Percent)
IRAnnualATMImpliedVol = __risk_measure_with_doc_string('Interest Rate Annual Implied At-The-Money Volatility (%)', RiskMeasureType.Annual_ATMF_Implied_Volatility, assetClass=AssetClass.Rates, unit=RiskMeasureUnit.Percent)
IRDailyImpliedVol = __risk_measure_with_doc_string('Interest Rate Daily Implied Volatility (bps)', RiskMeasureType.Annual_ATMF_Implied_Volatility, assetClass=AssetClass.Rates, unit=RiskMeasureUnit.BPS)

Formatters = {
    DollarPrice: scalar_formatter,
    Price: scalar_formatter,
    ForwardPrice: scalar_formatter,
    Theta: scalar_formatter,
    EqDelta: scalar_formatter,
    EqGamma: scalar_formatter,
    EqVega: sum_formatter,
    EqSpot: scalar_formatter,
    CommodDelta: structured_formatter,
    CommodVega: structured_formatter,
    CommodTheta: structured_formatter,
    FXDelta: structured_formatter,
    FXGamma: structured_formatter,
    FXVega: structured_formatter,
    FXSpot: scalar_formatter,
    IRDelta: structured_formatter,
    IRDeltaLocalCcy: structured_formatter,
    IRGamma: structured_formatter,
    IRVega: structured_formatter,
    IRVegaLocalCcy: scalar_formatter,
    IRAnnualImpliedVol: scalar_formatter,
    IRDailyImpliedVol: scalar_formatter,
    IRAnnualATMImpliedVol: scalar_formatter
}

