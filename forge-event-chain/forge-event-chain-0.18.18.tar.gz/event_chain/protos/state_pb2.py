# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto
import sys

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from . import type_pb2 as type__pb2
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='state.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x0bstate.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\ntype.proto\"\xbf\x03\n\x0c\x41\x63\x63ountState\x12#\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12\x0f\n\x07num_txs\x18\x03 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\n\n\x02pk\x18\x05 \x01(\x0c\x12#\n\x04type\x18\x06 \x01(\x0b\x32\x15.forge_abi.WalletType\x12\x0f\n\x07moniker\x18\x07 \x01(\t\x12(\n\x07\x63ontext\x18\x08 \x01(\x0b\x32\x17.forge_abi.StateContext\x12\x0e\n\x06issuer\x18\t \x01(\t\x12\x13\n\x0bmigrated_to\x18\r \x03(\t\x12\x15\n\rmigrated_from\x18\x0e \x03(\t\x12\x12\n\nnum_assets\x18\x0f \x01(\x04\x12&\n\x05stake\x18\x10 \x01(\x0b\x32\x17.forge_abi.StakeContext\x12.\n\x0cpinned_files\x18\x11 \x01(\x0b\x32\x18.forge_abi.CircularQueue\x12!\n\x04poke\x18\x12 \x01(\x0b\x32\x13.forge_abi.PokeInfo\x12\"\n\x04\x64\x61ta\x18\x32 \x01(\x0b\x32\x14.google.protobuf.Any\"\xac\x02\n\nAssetState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x0f\n\x07moniker\x18\x03 \x01(\t\x12\x10\n\x08readonly\x18\x04 \x01(\x08\x12\x15\n\rtransferrable\x18\x05 \x01(\x08\x12\x0b\n\x03ttl\x18\x06 \x01(\r\x12\x31\n\rconsumed_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06issuer\x18\x08 \x01(\t\x12&\n\x05stake\x18\r \x01(\x0b\x32\x17.forge_abi.StakeContext\x12(\n\x07\x63ontext\x18\x0e \x01(\x0b\x32\x17.forge_abi.StateContext\x12\"\n\x04\x64\x61ta\x18\x32 \x01(\x0b\x32\x14.google.protobuf.Any\"\xe6\x04\n\nForgeState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12-\n\tconsensus\x18\x02 \x01(\x0b\x32\x1a.forge_abi.ConsensusParams\x12/\n\x05tasks\x18\x03 \x03(\x0b\x32 .forge_abi.ForgeState.TasksEntry\x12>\n\rstake_summary\x18\x04 \x03(\x0b\x32\'.forge_abi.ForgeState.StakeSummaryEntry\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x14\n\x0c\x64\x61ta_version\x18\x06 \x01(\t\x12\x16\n\x0e\x66orge_app_hash\x18\x07 \x01(\x0c\x12$\n\x05token\x18\x08 \x01(\x0b\x32\x15.forge_abi.ForgeToken\x12/\n\ttx_config\x18\t \x01(\x0b\x32\x1c.forge_abi.TransactionConfig\x12,\n\x0cstake_config\x18\n \x01(\x0b\x32\x16.forge_abi.StakeConfig\x12*\n\x0bpoke_config\x18\x0b \x01(\x0b\x32\x15.forge_abi.PokeConfig\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\x1a\x45\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.forge_abi.UpgradeTasks:\x02\x38\x01\x1aL\n\x11StakeSummaryEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.forge_abi.StakeSummary:\x02\x38\x01\"M\n\tRootState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0c\x12\r\n\x05\x61sset\x18\x03 \x01(\x0c\x12\x0f\n\x07receipt\x18\x04 \x01(\x0c\"\xbb\x01\n\nStakeState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x01(\t\x12#\n\x07\x62\x61lance\x18\x04 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0f\n\x07message\x18\x05 \x01(\t\x12(\n\x07\x63ontext\x18\x0e \x01(\x0b\x32\x17.forge_abi.StateContext\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"\xb7\x01\n\x0fStatisticsState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\nnum_blocks\x18\x02 \x01(\x04\x12\x0f\n\x07num_txs\x18\x03 \x01(\x04\x12&\n\nnum_stakes\x18\x04 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x16\n\x0enum_validators\x18\x05 \x01(\r\x12.\n\rtx_statistics\x18\x06 \x01(\x0b\x32\x17.forge_abi.TxStatisticsb\x06proto3'),
    dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR, google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, type__pb2.DESCRIPTOR, ])


_ACCOUNTSTATE = _descriptor.Descriptor(
    name='AccountState',
    full_name='forge_abi.AccountState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='balance', full_name='forge_abi.AccountState.balance', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='nonce', full_name='forge_abi.AccountState.nonce', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_txs', full_name='forge_abi.AccountState.num_txs', index=2,
            number=3, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.AccountState.address', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='pk', full_name='forge_abi.AccountState.pk', index=4,
            number=5, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type', full_name='forge_abi.AccountState.type', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.AccountState.moniker', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='context', full_name='forge_abi.AccountState.context', index=7,
            number=8, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='issuer', full_name='forge_abi.AccountState.issuer', index=8,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='migrated_to', full_name='forge_abi.AccountState.migrated_to', index=9,
            number=13, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='migrated_from', full_name='forge_abi.AccountState.migrated_from', index=10,
            number=14, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_assets', full_name='forge_abi.AccountState.num_assets', index=11,
            number=15, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stake', full_name='forge_abi.AccountState.stake', index=12,
            number=16, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='pinned_files', full_name='forge_abi.AccountState.pinned_files', index=13,
            number=17, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='poke', full_name='forge_abi.AccountState.poke', index=14,
            number=18, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.AccountState.data', index=15,
            number=50, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=99,
    serialized_end=546,
)


_ASSETSTATE = _descriptor.Descriptor(
    name='AssetState',
    full_name='forge_abi.AssetState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.AssetState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='owner', full_name='forge_abi.AssetState.owner', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.AssetState.moniker', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='readonly', full_name='forge_abi.AssetState.readonly', index=3,
            number=4, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='transferrable', full_name='forge_abi.AssetState.transferrable', index=4,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ttl', full_name='forge_abi.AssetState.ttl', index=5,
            number=6, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='consumed_time', full_name='forge_abi.AssetState.consumed_time', index=6,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='issuer', full_name='forge_abi.AssetState.issuer', index=7,
            number=8, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stake', full_name='forge_abi.AssetState.stake', index=8,
            number=13, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='context', full_name='forge_abi.AssetState.context', index=9,
            number=14, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.AssetState.data', index=10,
            number=50, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=549,
    serialized_end=849,
)


_FORGESTATE_TASKSENTRY = _descriptor.Descriptor(
    name='TasksEntry',
    full_name='forge_abi.ForgeState.TasksEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='forge_abi.ForgeState.TasksEntry.key', index=0,
            number=1, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='forge_abi.ForgeState.TasksEntry.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1319,
    serialized_end=1388,
)

_FORGESTATE_STAKESUMMARYENTRY = _descriptor.Descriptor(
    name='StakeSummaryEntry',
    full_name='forge_abi.ForgeState.StakeSummaryEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='forge_abi.ForgeState.StakeSummaryEntry.key', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='forge_abi.ForgeState.StakeSummaryEntry.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1390,
    serialized_end=1466,
)

_FORGESTATE = _descriptor.Descriptor(
    name='ForgeState',
    full_name='forge_abi.ForgeState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.ForgeState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='consensus', full_name='forge_abi.ForgeState.consensus', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tasks', full_name='forge_abi.ForgeState.tasks', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stake_summary', full_name='forge_abi.ForgeState.stake_summary', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='version', full_name='forge_abi.ForgeState.version', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data_version', full_name='forge_abi.ForgeState.data_version', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='forge_app_hash', full_name='forge_abi.ForgeState.forge_app_hash', index=6,
            number=7, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='token', full_name='forge_abi.ForgeState.token', index=7,
            number=8, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tx_config', full_name='forge_abi.ForgeState.tx_config', index=8,
            number=9, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stake_config', full_name='forge_abi.ForgeState.stake_config', index=9,
            number=10, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='poke_config', full_name='forge_abi.ForgeState.poke_config', index=10,
            number=11, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.ForgeState.data', index=11,
            number=15, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_FORGESTATE_TASKSENTRY, _FORGESTATE_STAKESUMMARYENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=852,
    serialized_end=1466,
)


_ROOTSTATE = _descriptor.Descriptor(
    name='RootState',
    full_name='forge_abi.RootState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.RootState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='account', full_name='forge_abi.RootState.account', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='asset', full_name='forge_abi.RootState.asset', index=2,
            number=3, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='receipt', full_name='forge_abi.RootState.receipt', index=3,
            number=4, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1468,
    serialized_end=1545,
)


_STAKESTATE = _descriptor.Descriptor(
    name='StakeState',
    full_name='forge_abi.StakeState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.StakeState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='from', full_name='forge_abi.StakeState.from', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='to', full_name='forge_abi.StakeState.to', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='balance', full_name='forge_abi.StakeState.balance', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='message', full_name='forge_abi.StakeState.message', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='context', full_name='forge_abi.StakeState.context', index=5,
            number=14, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.StakeState.data', index=6,
            number=15, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1548,
    serialized_end=1735,
)


_STATISTICSSTATE = _descriptor.Descriptor(
    name='StatisticsState',
    full_name='forge_abi.StatisticsState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.StatisticsState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_blocks', full_name='forge_abi.StatisticsState.num_blocks', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_txs', full_name='forge_abi.StatisticsState.num_txs', index=2,
            number=3, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_stakes', full_name='forge_abi.StatisticsState.num_stakes', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_validators', full_name='forge_abi.StatisticsState.num_validators', index=4,
            number=5, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tx_statistics', full_name='forge_abi.StatisticsState.tx_statistics', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1738,
    serialized_end=1921,
)

_ACCOUNTSTATE.fields_by_name['balance'].message_type = type__pb2._BIGUINT
_ACCOUNTSTATE.fields_by_name['type'].message_type = type__pb2._WALLETTYPE
_ACCOUNTSTATE.fields_by_name['context'].message_type = type__pb2._STATECONTEXT
_ACCOUNTSTATE.fields_by_name['stake'].message_type = type__pb2._STAKECONTEXT
_ACCOUNTSTATE.fields_by_name['pinned_files'].message_type = type__pb2._CIRCULARQUEUE
_ACCOUNTSTATE.fields_by_name['poke'].message_type = type__pb2._POKEINFO
_ACCOUNTSTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ASSETSTATE.fields_by_name['consumed_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSETSTATE.fields_by_name['stake'].message_type = type__pb2._STAKECONTEXT
_ASSETSTATE.fields_by_name['context'].message_type = type__pb2._STATECONTEXT
_ASSETSTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FORGESTATE_TASKSENTRY.fields_by_name['value'].message_type = type__pb2._UPGRADETASKS
_FORGESTATE_TASKSENTRY.containing_type = _FORGESTATE
_FORGESTATE_STAKESUMMARYENTRY.fields_by_name['value'].message_type = type__pb2._STAKESUMMARY
_FORGESTATE_STAKESUMMARYENTRY.containing_type = _FORGESTATE
_FORGESTATE.fields_by_name['consensus'].message_type = type__pb2._CONSENSUSPARAMS
_FORGESTATE.fields_by_name['tasks'].message_type = _FORGESTATE_TASKSENTRY
_FORGESTATE.fields_by_name['stake_summary'].message_type = _FORGESTATE_STAKESUMMARYENTRY
_FORGESTATE.fields_by_name['token'].message_type = type__pb2._FORGETOKEN
_FORGESTATE.fields_by_name['tx_config'].message_type = type__pb2._TRANSACTIONCONFIG
_FORGESTATE.fields_by_name['stake_config'].message_type = type__pb2._STAKECONFIG
_FORGESTATE.fields_by_name['poke_config'].message_type = type__pb2._POKECONFIG
_FORGESTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_STAKESTATE.fields_by_name['balance'].message_type = type__pb2._BIGUINT
_STAKESTATE.fields_by_name['context'].message_type = type__pb2._STATECONTEXT
_STAKESTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_STATISTICSSTATE.fields_by_name['num_stakes'].message_type = type__pb2._BIGUINT
_STATISTICSSTATE.fields_by_name['tx_statistics'].message_type = type__pb2._TXSTATISTICS
DESCRIPTOR.message_types_by_name['AccountState'] = _ACCOUNTSTATE
DESCRIPTOR.message_types_by_name['AssetState'] = _ASSETSTATE
DESCRIPTOR.message_types_by_name['ForgeState'] = _FORGESTATE
DESCRIPTOR.message_types_by_name['RootState'] = _ROOTSTATE
DESCRIPTOR.message_types_by_name['StakeState'] = _STAKESTATE
DESCRIPTOR.message_types_by_name['StatisticsState'] = _STATISTICSSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountState = _reflection.GeneratedProtocolMessageType('AccountState', (_message.Message,), dict(
    DESCRIPTOR=_ACCOUNTSTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.AccountState)
))
_sym_db.RegisterMessage(AccountState)

AssetState = _reflection.GeneratedProtocolMessageType('AssetState', (_message.Message,), dict(
    DESCRIPTOR=_ASSETSTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.AssetState)
))
_sym_db.RegisterMessage(AssetState)

ForgeState = _reflection.GeneratedProtocolMessageType('ForgeState', (_message.Message,), dict(

    TasksEntry=_reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), dict(
        DESCRIPTOR=_FORGESTATE_TASKSENTRY,
        __module__='state_pb2'
        # @@protoc_insertion_point(class_scope:forge_abi.ForgeState.TasksEntry)
    )),

    StakeSummaryEntry=_reflection.GeneratedProtocolMessageType('StakeSummaryEntry', (_message.Message,), dict(
        DESCRIPTOR=_FORGESTATE_STAKESUMMARYENTRY,
        __module__='state_pb2'
        # @@protoc_insertion_point(class_scope:forge_abi.ForgeState.StakeSummaryEntry)
    )),
    DESCRIPTOR=_FORGESTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.ForgeState)
))
_sym_db.RegisterMessage(ForgeState)
_sym_db.RegisterMessage(ForgeState.TasksEntry)
_sym_db.RegisterMessage(ForgeState.StakeSummaryEntry)

RootState = _reflection.GeneratedProtocolMessageType('RootState', (_message.Message,), dict(
    DESCRIPTOR=_ROOTSTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.RootState)
))
_sym_db.RegisterMessage(RootState)

StakeState = _reflection.GeneratedProtocolMessageType('StakeState', (_message.Message,), dict(
    DESCRIPTOR=_STAKESTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.StakeState)
))
_sym_db.RegisterMessage(StakeState)

StatisticsState = _reflection.GeneratedProtocolMessageType('StatisticsState', (_message.Message,), dict(
    DESCRIPTOR=_STATISTICSSTATE,
    __module__='state_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.StatisticsState)
))
_sym_db.RegisterMessage(StatisticsState)


_FORGESTATE_TASKSENTRY._options = None
_FORGESTATE_STAKESUMMARYENTRY._options = None
# @@protoc_insertion_point(module_scope)
