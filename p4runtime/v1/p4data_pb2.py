# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p4runtime-proto/v1/p4data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fp4runtime-proto/v1/p4data.proto\x12\x05p4.v1\"\x94\x03\n\x06P4Data\x12\x13\n\tbitstring\x18\x01 \x01(\x0cH\x00\x12!\n\x06varbit\x18\x02 \x01(\x0b\x32\x0f.p4.v1.P4VarbitH\x00\x12\x0e\n\x04\x62ool\x18\x03 \x01(\x08H\x00\x12$\n\x05tuple\x18\x04 \x01(\x0b\x32\x13.p4.v1.P4StructLikeH\x00\x12%\n\x06struct\x18\x05 \x01(\x0b\x32\x13.p4.v1.P4StructLikeH\x00\x12!\n\x06header\x18\x06 \x01(\x0b\x32\x0f.p4.v1.P4HeaderH\x00\x12,\n\x0cheader_union\x18\x07 \x01(\x0b\x32\x14.p4.v1.P4HeaderUnionH\x00\x12,\n\x0cheader_stack\x18\x08 \x01(\x0b\x32\x14.p4.v1.P4HeaderStackH\x00\x12\x37\n\x12header_union_stack\x18\t \x01(\x0b\x32\x19.p4.v1.P4HeaderUnionStackH\x00\x12\x0e\n\x04\x65num\x18\n \x01(\tH\x00\x12\x0f\n\x05\x65rror\x18\x0b \x01(\tH\x00\x12\x14\n\nenum_value\x18\x0c \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"/\n\x08P4Varbit\x12\x11\n\tbitstring\x18\x01 \x01(\x0c\x12\x10\n\x08\x62itwidth\x18\x02 \x01(\x05\".\n\x0cP4StructLike\x12\x1e\n\x07members\x18\x01 \x03(\x0b\x32\r.p4.v1.P4Data\"0\n\x08P4Header\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x12\n\nbitstrings\x18\x02 \x03(\x0c\"Q\n\rP4HeaderUnion\x12\x19\n\x11valid_header_name\x18\x01 \x01(\t\x12%\n\x0cvalid_header\x18\x02 \x01(\x0b\x32\x0f.p4.v1.P4Header\"1\n\rP4HeaderStack\x12 \n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x0f.p4.v1.P4Header\";\n\x12P4HeaderUnionStack\x12%\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x14.p4.v1.P4HeaderUnionB&Z$github.com/p4lang/p4runtime/go/p4/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p4runtime_proto.v1.p4data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/p4lang/p4runtime/go/p4/v1'
  _globals['_P4DATA']._serialized_start=43
  _globals['_P4DATA']._serialized_end=447
  _globals['_P4VARBIT']._serialized_start=449
  _globals['_P4VARBIT']._serialized_end=496
  _globals['_P4STRUCTLIKE']._serialized_start=498
  _globals['_P4STRUCTLIKE']._serialized_end=544
  _globals['_P4HEADER']._serialized_start=546
  _globals['_P4HEADER']._serialized_end=594
  _globals['_P4HEADERUNION']._serialized_start=596
  _globals['_P4HEADERUNION']._serialized_end=677
  _globals['_P4HEADERSTACK']._serialized_start=679
  _globals['_P4HEADERSTACK']._serialized_end=728
  _globals['_P4HEADERUNIONSTACK']._serialized_start=730
  _globals['_P4HEADERUNIONSTACK']._serialized_end=789
# @@protoc_insertion_point(module_scope)
