# -*- coding: utf-8 -*-
from collections import OrderedDict
import hashlib
import hmac
import time

from cdecimal import *
from delorean import Delorean, parse, epoch

from base import *
from exceptions import *
from gryphon.lib.exchange.consts import Consts
from gryphon.lib.models.exchange import Balance
from gryphon.lib.money import Money
from gryphon.lib.exchange.bitstamp_btc_usd import BitstampBTCUSDExchange

from gryphon.lib.logger import get_logger
logger = get_logger(__name__)


class BitstampETHEURExchange(BitstampBTCUSDExchange):
    def __init__(self, session=None, configuration=None):
        super(BitstampETHEURExchange, self).__init__(session)

        self.name = u'BITSTAMP_ETH_EUR'
        self.friendly_name = u'Bitstamp ETH-EUR'
        self.currency = u'EUR'
        self.volume_currency = 'ETH'

        self.fiat_balance_tolerance = Money('0.0001', 'EUR')
        self.volume_balance_tolerance = Money('0.00000001', 'ETH')
        self.min_order_size = Money('0.001', 'ETH')

        if configuration:
            self.configure(configuration)

        # Endpoints.
        self.ticker_url = 'ticker/etheur/'
        self.orderbook_url = 'order_book/etheur/'
        self.buy_url = 'buy/etheur/'
        self.sell_url = 'sell/etheur/'
        self.open_orders_url = 'open_orders/etheur/'
        self.trade_status_url = 'user_transactions/etheur/'
        self.balance_url = 'balance/'
        self.trade_cancel_url = 'cancel_order/'

        # TODO: Implement deposit/withdrawal urls for bitstamp eth usd.
        self.withdrawl_requests_url = ''
        self.deposit_address_url = ''

