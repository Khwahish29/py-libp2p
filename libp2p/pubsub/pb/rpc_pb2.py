# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="rpc.proto",
    package="pubsub.pb",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=_b(
        '\n\trpc.proto\x12\tpubsub.pb"\xb4\x01\n\x03RPC\x12-\n\rsubscriptions\x18\x01 \x03(\x0b\x32\x16.pubsub.pb.RPC.SubOpts\x12#\n\x07publish\x18\x02 \x03(\x0b\x32\x12.pubsub.pb.Message\x12*\n\x07\x63ontrol\x18\x03 \x01(\x0b\x32\x19.pubsub.pb.ControlMessage\x1a-\n\x07SubOpts\x12\x11\n\tsubscribe\x18\x01 \x01(\x08\x12\x0f\n\x07topicid\x18\x02 \x01(\t"i\n\x07Message\x12\x0f\n\x07\x66rom_id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05seqno\x18\x03 \x01(\x0c\x12\x10\n\x08topicIDs\x18\x04 \x03(\t\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x12\x0b\n\x03key\x18\x06 \x01(\x0c"\xb0\x01\n\x0e\x43ontrolMessage\x12&\n\x05ihave\x18\x01 \x03(\x0b\x32\x17.pubsub.pb.ControlIHave\x12&\n\x05iwant\x18\x02 \x03(\x0b\x32\x17.pubsub.pb.ControlIWant\x12&\n\x05graft\x18\x03 \x03(\x0b\x32\x17.pubsub.pb.ControlGraft\x12&\n\x05prune\x18\x04 \x03(\x0b\x32\x17.pubsub.pb.ControlPrune"3\n\x0c\x43ontrolIHave\x12\x0f\n\x07topicID\x18\x01 \x01(\t\x12\x12\n\nmessageIDs\x18\x02 \x03(\t""\n\x0c\x43ontrolIWant\x12\x12\n\nmessageIDs\x18\x01 \x03(\t"\x1f\n\x0c\x43ontrolGraft\x12\x0f\n\x07topicID\x18\x01 \x01(\t"\x1f\n\x0c\x43ontrolPrune\x12\x0f\n\x07topicID\x18\x01 \x01(\t"\x87\x03\n\x0fTopicDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x04\x61uth\x18\x02 \x01(\x0b\x32#.pubsub.pb.TopicDescriptor.AuthOpts\x12/\n\x03\x65nc\x18\x03 \x01(\x0b\x32".pubsub.pb.TopicDescriptor.EncOpts\x1a|\n\x08\x41uthOpts\x12:\n\x04mode\x18\x01 \x01(\x0e\x32,.pubsub.pb.TopicDescriptor.AuthOpts.AuthMode\x12\x0c\n\x04keys\x18\x02 \x03(\x0c"&\n\x08\x41uthMode\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03KEY\x10\x01\x12\x07\n\x03WOT\x10\x02\x1a\x83\x01\n\x07\x45ncOpts\x12\x38\n\x04mode\x18\x01 \x01(\x0e\x32*.pubsub.pb.TopicDescriptor.EncOpts.EncMode\x12\x11\n\tkeyHashes\x18\x02 \x03(\x0c"+\n\x07\x45ncMode\x12\x08\n\x04NONE\x10\x00\x12\r\n\tSHAREDKEY\x10\x01\x12\x07\n\x03WOT\x10\x02'
    ),
)


_TOPICDESCRIPTOR_AUTHOPTS_AUTHMODE = _descriptor.EnumDescriptor(
    name="AuthMode",
    full_name="pubsub.pb.TopicDescriptor.AuthOpts.AuthMode",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="KEY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WOT", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=868,
    serialized_end=906,
)
_sym_db.RegisterEnumDescriptor(_TOPICDESCRIPTOR_AUTHOPTS_AUTHMODE)

_TOPICDESCRIPTOR_ENCOPTS_ENCMODE = _descriptor.EnumDescriptor(
    name="EncMode",
    full_name="pubsub.pb.TopicDescriptor.EncOpts.EncMode",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SHAREDKEY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WOT", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=997,
    serialized_end=1040,
)
_sym_db.RegisterEnumDescriptor(_TOPICDESCRIPTOR_ENCOPTS_ENCMODE)


_RPC_SUBOPTS = _descriptor.Descriptor(
    name="SubOpts",
    full_name="pubsub.pb.RPC.SubOpts",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="subscribe",
            full_name="pubsub.pb.RPC.SubOpts.subscribe",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="topicid",
            full_name="pubsub.pb.RPC.SubOpts.topicid",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=160,
    serialized_end=205,
)

_RPC = _descriptor.Descriptor(
    name="RPC",
    full_name="pubsub.pb.RPC",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="subscriptions",
            full_name="pubsub.pb.RPC.subscriptions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="publish",
            full_name="pubsub.pb.RPC.publish",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="control",
            full_name="pubsub.pb.RPC.control",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_RPC_SUBOPTS],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=25,
    serialized_end=205,
)


_MESSAGE = _descriptor.Descriptor(
    name="Message",
    full_name="pubsub.pb.Message",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="from_id",
            full_name="pubsub.pb.Message.from_id",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="pubsub.pb.Message.data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="seqno",
            full_name="pubsub.pb.Message.seqno",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="topicIDs",
            full_name="pubsub.pb.Message.topicIDs",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="pubsub.pb.Message.signature",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="key",
            full_name="pubsub.pb.Message.key",
            index=5,
            number=6,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=207,
    serialized_end=312,
)


_CONTROLMESSAGE = _descriptor.Descriptor(
    name="ControlMessage",
    full_name="pubsub.pb.ControlMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ihave",
            full_name="pubsub.pb.ControlMessage.ihave",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="iwant",
            full_name="pubsub.pb.ControlMessage.iwant",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="graft",
            full_name="pubsub.pb.ControlMessage.graft",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prune",
            full_name="pubsub.pb.ControlMessage.prune",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=315,
    serialized_end=491,
)


_CONTROLIHAVE = _descriptor.Descriptor(
    name="ControlIHave",
    full_name="pubsub.pb.ControlIHave",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="topicID",
            full_name="pubsub.pb.ControlIHave.topicID",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="messageIDs",
            full_name="pubsub.pb.ControlIHave.messageIDs",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=493,
    serialized_end=544,
)


_CONTROLIWANT = _descriptor.Descriptor(
    name="ControlIWant",
    full_name="pubsub.pb.ControlIWant",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="messageIDs",
            full_name="pubsub.pb.ControlIWant.messageIDs",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=546,
    serialized_end=580,
)


_CONTROLGRAFT = _descriptor.Descriptor(
    name="ControlGraft",
    full_name="pubsub.pb.ControlGraft",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="topicID",
            full_name="pubsub.pb.ControlGraft.topicID",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=582,
    serialized_end=613,
)


_CONTROLPRUNE = _descriptor.Descriptor(
    name="ControlPrune",
    full_name="pubsub.pb.ControlPrune",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="topicID",
            full_name="pubsub.pb.ControlPrune.topicID",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=615,
    serialized_end=646,
)


_TOPICDESCRIPTOR_AUTHOPTS = _descriptor.Descriptor(
    name="AuthOpts",
    full_name="pubsub.pb.TopicDescriptor.AuthOpts",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="mode",
            full_name="pubsub.pb.TopicDescriptor.AuthOpts.mode",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="keys",
            full_name="pubsub.pb.TopicDescriptor.AuthOpts.keys",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_TOPICDESCRIPTOR_AUTHOPTS_AUTHMODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=782,
    serialized_end=906,
)

_TOPICDESCRIPTOR_ENCOPTS = _descriptor.Descriptor(
    name="EncOpts",
    full_name="pubsub.pb.TopicDescriptor.EncOpts",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="mode",
            full_name="pubsub.pb.TopicDescriptor.EncOpts.mode",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="keyHashes",
            full_name="pubsub.pb.TopicDescriptor.EncOpts.keyHashes",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_TOPICDESCRIPTOR_ENCOPTS_ENCMODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=909,
    serialized_end=1040,
)

_TOPICDESCRIPTOR = _descriptor.Descriptor(
    name="TopicDescriptor",
    full_name="pubsub.pb.TopicDescriptor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="pubsub.pb.TopicDescriptor.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="auth",
            full_name="pubsub.pb.TopicDescriptor.auth",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="enc",
            full_name="pubsub.pb.TopicDescriptor.enc",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_TOPICDESCRIPTOR_AUTHOPTS, _TOPICDESCRIPTOR_ENCOPTS],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=649,
    serialized_end=1040,
)

_RPC_SUBOPTS.containing_type = _RPC
_RPC.fields_by_name["subscriptions"].message_type = _RPC_SUBOPTS
_RPC.fields_by_name["publish"].message_type = _MESSAGE
_RPC.fields_by_name["control"].message_type = _CONTROLMESSAGE
_CONTROLMESSAGE.fields_by_name["ihave"].message_type = _CONTROLIHAVE
_CONTROLMESSAGE.fields_by_name["iwant"].message_type = _CONTROLIWANT
_CONTROLMESSAGE.fields_by_name["graft"].message_type = _CONTROLGRAFT
_CONTROLMESSAGE.fields_by_name["prune"].message_type = _CONTROLPRUNE
_TOPICDESCRIPTOR_AUTHOPTS.fields_by_name[
    "mode"
].enum_type = _TOPICDESCRIPTOR_AUTHOPTS_AUTHMODE
_TOPICDESCRIPTOR_AUTHOPTS.containing_type = _TOPICDESCRIPTOR
_TOPICDESCRIPTOR_AUTHOPTS_AUTHMODE.containing_type = _TOPICDESCRIPTOR_AUTHOPTS
_TOPICDESCRIPTOR_ENCOPTS.fields_by_name[
    "mode"
].enum_type = _TOPICDESCRIPTOR_ENCOPTS_ENCMODE
_TOPICDESCRIPTOR_ENCOPTS.containing_type = _TOPICDESCRIPTOR
_TOPICDESCRIPTOR_ENCOPTS_ENCMODE.containing_type = _TOPICDESCRIPTOR_ENCOPTS
_TOPICDESCRIPTOR.fields_by_name["auth"].message_type = _TOPICDESCRIPTOR_AUTHOPTS
_TOPICDESCRIPTOR.fields_by_name["enc"].message_type = _TOPICDESCRIPTOR_ENCOPTS
DESCRIPTOR.message_types_by_name["RPC"] = _RPC
DESCRIPTOR.message_types_by_name["Message"] = _MESSAGE
DESCRIPTOR.message_types_by_name["ControlMessage"] = _CONTROLMESSAGE
DESCRIPTOR.message_types_by_name["ControlIHave"] = _CONTROLIHAVE
DESCRIPTOR.message_types_by_name["ControlIWant"] = _CONTROLIWANT
DESCRIPTOR.message_types_by_name["ControlGraft"] = _CONTROLGRAFT
DESCRIPTOR.message_types_by_name["ControlPrune"] = _CONTROLPRUNE
DESCRIPTOR.message_types_by_name["TopicDescriptor"] = _TOPICDESCRIPTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RPC = _reflection.GeneratedProtocolMessageType(
    "RPC",
    (_message.Message,),
    dict(
        SubOpts=_reflection.GeneratedProtocolMessageType(
            "SubOpts",
            (_message.Message,),
            dict(
                DESCRIPTOR=_RPC_SUBOPTS,
                __module__="rpc_pb2"
                # @@protoc_insertion_point(class_scope:pubsub.pb.RPC.SubOpts)
            ),
        ),
        DESCRIPTOR=_RPC,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.RPC)
    ),
)
_sym_db.RegisterMessage(RPC)
_sym_db.RegisterMessage(RPC.SubOpts)

Message = _reflection.GeneratedProtocolMessageType(
    "Message",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MESSAGE,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.Message)
    ),
)
_sym_db.RegisterMessage(Message)

ControlMessage = _reflection.GeneratedProtocolMessageType(
    "ControlMessage",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTROLMESSAGE,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.ControlMessage)
    ),
)
_sym_db.RegisterMessage(ControlMessage)

ControlIHave = _reflection.GeneratedProtocolMessageType(
    "ControlIHave",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTROLIHAVE,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.ControlIHave)
    ),
)
_sym_db.RegisterMessage(ControlIHave)

ControlIWant = _reflection.GeneratedProtocolMessageType(
    "ControlIWant",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTROLIWANT,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.ControlIWant)
    ),
)
_sym_db.RegisterMessage(ControlIWant)

ControlGraft = _reflection.GeneratedProtocolMessageType(
    "ControlGraft",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTROLGRAFT,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.ControlGraft)
    ),
)
_sym_db.RegisterMessage(ControlGraft)

ControlPrune = _reflection.GeneratedProtocolMessageType(
    "ControlPrune",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTROLPRUNE,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.ControlPrune)
    ),
)
_sym_db.RegisterMessage(ControlPrune)

TopicDescriptor = _reflection.GeneratedProtocolMessageType(
    "TopicDescriptor",
    (_message.Message,),
    dict(
        AuthOpts=_reflection.GeneratedProtocolMessageType(
            "AuthOpts",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TOPICDESCRIPTOR_AUTHOPTS,
                __module__="rpc_pb2"
                # @@protoc_insertion_point(class_scope:pubsub.pb.TopicDescriptor.AuthOpts)
            ),
        ),
        EncOpts=_reflection.GeneratedProtocolMessageType(
            "EncOpts",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TOPICDESCRIPTOR_ENCOPTS,
                __module__="rpc_pb2"
                # @@protoc_insertion_point(class_scope:pubsub.pb.TopicDescriptor.EncOpts)
            ),
        ),
        DESCRIPTOR=_TOPICDESCRIPTOR,
        __module__="rpc_pb2"
        # @@protoc_insertion_point(class_scope:pubsub.pb.TopicDescriptor)
    ),
)
_sym_db.RegisterMessage(TopicDescriptor)
_sym_db.RegisterMessage(TopicDescriptor.AuthOpts)
_sym_db.RegisterMessage(TopicDescriptor.EncOpts)


# @@protoc_insertion_point(module_scope)
