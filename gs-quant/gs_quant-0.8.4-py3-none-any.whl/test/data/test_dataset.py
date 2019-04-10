"""
Copyright 2018 Goldman Sachs.
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
from abc import ABCMeta

from gs_quant.api.gs.data import GsDataApi
from gs_quant.data import Dataset

import datetime as dt
import pandas as pd
from unittest import mock

test_data = [
    {
        'date': dt.date(2019, 1, 2),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2529,
        'adjustedAskPrice': 2529,
        'bidPrice': 2442.55,
        'adjustedBidPrice': 2442.55,
        'tradePrice': 2510.03,
        'adjustedTradePrice': 2510.03,
        'openPrice': 2476.96,
        'adjustedOpenPrice': 2476.96,
        'highPrice': 2519.49,
        'lowPrice': 2467.47,
        'adjustedHighPrice': 2519.49,
        'adjustedLowPrice': 2467.47,
        'updateTime': '2019-01-03T00:53:00Z'
    },
    {
        'date': dt.date(2019, 1, 3),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2502.34,
        'adjustedAskPrice': 2502.34,
        'bidPrice': 2418.09,
        'adjustedBidPrice': 2418.09,
        'tradePrice': 2447.89,
        'adjustedTradePrice': 2447.89,
        'openPrice': 2491.92,
        'adjustedOpenPrice': 2491.92,
        'highPrice': 2493.14,
        'lowPrice': 2443.96,
        'adjustedHighPrice': 2493.14,
        'adjustedLowPrice': 2443.96,
        'updateTime': '2019-01-04T00:14:00Z'
    },
    {
        'date': dt.date(2019, 1, 4),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2566.52,
        'adjustedAskPrice': 2566.52,
        'bidPrice': 2487.8,
        'adjustedBidPrice': 2487.8,
        'tradePrice': 2531.94,
        'adjustedTradePrice': 2531.94,
        'openPrice': 2474.33,
        'adjustedOpenPrice': 2474.33,
        'highPrice': 2538.07,
        'lowPrice': 2474.33,
        'adjustedHighPrice': 2538.07,
        'adjustedLowPrice': 2474.33,
        'updateTime': '2019-01-08T00:31:00Z'
    },
    {
        'date': dt.date(2019, 1, 7),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2591.75,
        'adjustedAskPrice': 2591.75,
        'bidPrice': 2509.77,
        'adjustedBidPrice': 2509.77,
        'tradePrice': 2549.69,
        'adjustedTradePrice': 2549.69,
        'openPrice': 2535.61,
        'adjustedOpenPrice': 2535.61,
        'highPrice': 2566.16,
        'lowPrice': 2524.56,
        'adjustedHighPrice': 2566.16,
        'adjustedLowPrice': 2524.56,
        'updateTime': '2019-01-08T00:31:00'
    },
    {
        'date': dt.date(2019, 1, 8),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2610.52,
        'adjustedAskPrice': 2610.52,
        'bidPrice': 2531.15,
        'adjustedBidPrice': 2531.15,
        'tradePrice': 2574.41,
        'adjustedTradePrice': 2574.41,
        'openPrice': 2568.11,
        'adjustedOpenPrice': 2568.11,
        'highPrice': 2579.82,
        'lowPrice': 2547.56,
        'adjustedHighPrice': 2579.82,
        'adjustedLowPrice': 2547.56,
        'updateTime': '2019-01-09T00:50:00Z'
    },
    {
        'date': dt.date(2019, 1, 9),
        'assetId': 'MA4B66MW5E27U8P32SB',
        'askPrice': 2623.09,
        'adjustedAskPrice': 2623.09,
        'bidPrice': 2537.19,
        'adjustedBidPrice': 2537.19,
        'tradePrice': 2584.96,
        'adjustedTradePrice': 2584.96,
        'openPrice': 2580,
        'adjustedOpenPrice': 2580,
        'highPrice': 2595.32,
        'lowPrice': 2568.89,
        'adjustedHighPrice': 2595.32,
        'adjustedLowPrice': 2568.89,
        'updateTime': '2019-01-10T00:44:00Z'
    }
]

test_coverage_data = { 'results': [{ 'gsid': 'gsid1' }] }

@mock.patch.object(GsDataApi, 'query_data')
def test_query_data(mocker):
    mocker.return_value = test_data
    dataset = Dataset(Dataset.TR.TREOD)
    data = dataset.get_data(dt.date(2019, 1, 2), dt.date(2019, 1, 9), assetId='MA4B66MW5E27U8P32SB')
    assert data.equals(pd.DataFrame(test_data))


@mock.patch.object(GsDataApi, 'last_data')
def test_last_data(mocker):
    mocker.return_value = [test_data[-1]]
    dataset = Dataset(Dataset.TR.TREOD)
    data = dataset.get_data_last(dt.date(2019, 1, 9), assetId='MA4B66MW5E27U8P32SB')
    assert data.equals(pd.DataFrame([test_data[-1]]))


def test_get_data_series(mocker):
    mocker.patch.object(GsDataApi, 'query_data', return_value=test_data)
    mocker.patch.object(GsDataApi, 'symbol_dimensions', return_value=('assetId',))
    mocker.patch.object(GsDataApi, 'time_field', return_value='date')

    dataset = Dataset(Dataset.TR.TREOD)
    series = dataset.get_data_series('tradePrice', dt.date(2019, 1, 2), dt.date(2019, 1, 9), assetId='MA4B66MW5E27U8P32SB')

    df = pd.DataFrame(test_data)
    index = pd.to_datetime(df.loc[:, 'date'].values)
    expected = pd.Series(index=index, data=df.loc[:, 'tradePrice'].values)

    assert series.equals(pd.Series(expected))


@mock.patch.object(GsDataApi, 'get_coverage')
def test_get_coverage(mocker):
    mocker.return_value = test_coverage_data
    data = Dataset(Dataset.TR.TREOD).get_coverage()

    assert data.equals(pd.DataFrame(test_coverage_data))

