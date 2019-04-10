import marshmallow

from .early_ack import GoogleEarlyAckReceiveAndReply, GoogleEarlyAckReceiver
from happyly.caching.cacher import Cacher
from happyly.caching.mixins import CacheByRequestIdMixin
from happyly.handling import Handler


class GoogleCachedReceiveAndReply(CacheByRequestIdMixin, GoogleEarlyAckReceiveAndReply):
    def __init__(
        self,
        handler: Handler,
        input_schema: marshmallow.Schema,
        from_subscription: str,
        from_topic: str,
        output_schema: marshmallow.Schema,
        to_topic: str,
        project: str,
        cacher: Cacher,
    ):
        GoogleEarlyAckReceiveAndReply.__init__(
            self,
            handler=handler,
            input_schema=input_schema,
            from_subscription=from_subscription,
            output_schema=output_schema,
            to_topic=to_topic,
            project=project,
            from_topic=from_topic,
        )
        CacheByRequestIdMixin.__init__(self, cacher)


class GoogleCachedReceiver(CacheByRequestIdMixin, GoogleEarlyAckReceiver):
    def __init__(
        self,
        handler: Handler,
        input_schema: marshmallow.Schema,
        from_subscription: str,
        from_topic: str,
        project: str,
        cacher: Cacher,
    ):
        GoogleEarlyAckReceiver.__init__(
            self,
            handler=handler,
            input_schema=input_schema,
            from_subscription=from_subscription,
            project=project,
            from_topic=from_topic,
        )
        CacheByRequestIdMixin.__init__(self, cacher)
