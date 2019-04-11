#: chain_types
class ChainTypes:
    def __init__(self):
        self.reserved_spaces = {
            'RELATIVE_PROTOCOL_IDS': 0,
            'PROTOCOL_IDS': 1,
            'IMPLEMENTATION_IDS': 2,
        }

        self.implementation_object_type = {
            'GLOBAL_PROPERTY': 0,
            'DYNAMIC_GLOBAL_PROPERTY': 1,
            'INDEX_META': 2,
            'ASSET_DYNAMIC_DATA': 3,
            'ASSET_BITASSET_DATA': 4,
            'ACCOUNT_BALANCE': 5,
            'ACCOUNT_STATISTICS': 6,
            'TRANSACTION': 7,
            'BLOCK_SUMMARY': 8,
            'ACCOUNT_TRANSACTION_HISTORY': 9,
            'BLINDED_BALANCE': 10,
            'CHAIN_PROPERTY': 11,
            'WITNESS_SCHEDULE': 12,
            'BUDGET_RECORD': 13,
        }

        self.vote_type = {
            'COMMITTEE': 0,
            'WITNESS': 1,
            'WORKER': 2,
        }
