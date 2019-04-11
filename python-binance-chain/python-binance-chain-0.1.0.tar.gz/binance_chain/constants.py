from enum import Enum


class KlineInterval(str, Enum):
    ONE_MINUTE = '1m'
    THREE_MINUTES = '3m'
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    ONE_HOUR = '1h'
    TWO_HOURS = '2h'
    FOUR_HOURS = '4h'
    SIX_HOURS = '6h'
    EIGHT_HOURS = '8h'
    TWELVE_HOURS = '12h'
    ONE_DAY = '1d'
    THREE_DAYS = '3d'
    ONE_WEEK = '1w'
    ONE_MONTH = '1M'


class OrderStatus(str, Enum):
    ACK = 'Ack'
    PARTIAL_FILL = 'PartialFill'
    IOC_NO_FILL = 'IocNoFill'
    FULLY_FILL = 'FullyFill'
    CANCELED = 'Canceled'
    EXPIRED = 'Expired'
    FAILED_BLOCKING = 'FailedBlocking'
    FAILED_MATCHING = 'FailedMatching'


class OrderSide(str, Enum):
    BUY = 'buy'
    SELL = 'sell'


class TimeInForce(str, Enum):
    GOOD_TILL_EXPIRE = "GTE"
    IMMEDIATE_OR_CANCEL = "IOC"


class TransactionSide(str, Enum):
    RECEIVE = 'RECEIVE'
    SEND = 'SEND'


class TransactionType(str, Enum):
    NEW_ORDER = 'NEW_ORDER'
    ISSUE_TOKEN = 'ISSUE_TOKEN'
    BURN_TOKEN = 'BURN_TOKEN'
    LIST_TOKEN = 'LIST_TOKEN'
    CANCEL_ORDER = 'CANCEL_ORDER'
    FREEZE_TOKEN = 'FREEZE_TOKEN'
    UN_FREEZE_TOKEN = 'UN_FREEZE_TOKEN'
    TRANSFER = 'TRANSFER'
    PROPOSAL = 'PROPOSAL'
    VOTE = 'VOTE'


class OrderType(str, Enum):
    LIMIT = "LIMIT"


class PeerType(str, Enum):
    NODE = 'node'
    WEBSOCKET = 'ws'


class RpcBroadcastRequestType(int, Enum):
    SYNC = 1
    ASYNC = 2
    COMMIT = 3
