from irods_capability_automated_ingest.core import Core
from irods_capability_automated_ingest.utils import Operation

class event_handler(Core):

    @staticmethod
    def operation(session, meta, **options):
        return Operation.REGISTER_AS_REPLICA_SYNC

    @staticmethod
    def to_resource(session, meta, **options):
        return "regiResc2"




