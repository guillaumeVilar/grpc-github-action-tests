# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execute_script.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='execute_script.proto',
  package='executescript',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x65xecute_script.proto\x12\rexecutescript\"s\n\x0cScriptChoice\x12\x32\n\x06script\x18\x02 \x01(\x0e\x32\".executescript.ScriptChoice.Script\"/\n\x06Script\x12\x0b\n\x07SCRIPT0\x10\x00\x12\x0b\n\x07SCRIPT1\x10\x01\x12\x0b\n\x07SCRIPT2\x10\x02\"@\n\x0cScriptResult\x12\x0e\n\x06stdout\x18\x01 \x01(\t\x12\x0e\n\x06stderr\x18\x02 \x01(\t\x12\x10\n\x08\x65xitcode\x18\x03 \x01(\x05\x32W\n\x08\x45xecuter\x12K\n\rExecuteScript\x12\x1b.executescript.ScriptChoice\x1a\x1b.executescript.ScriptResult0\x01\x62\x06proto3'
)



_SCRIPTCHOICE_SCRIPT = _descriptor.EnumDescriptor(
  name='Script',
  full_name='executescript.ScriptChoice.Script',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCRIPT0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCRIPT1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCRIPT2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=107,
  serialized_end=154,
)
_sym_db.RegisterEnumDescriptor(_SCRIPTCHOICE_SCRIPT)


_SCRIPTCHOICE = _descriptor.Descriptor(
  name='ScriptChoice',
  full_name='executescript.ScriptChoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='executescript.ScriptChoice.script', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCRIPTCHOICE_SCRIPT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=154,
)


_SCRIPTRESULT = _descriptor.Descriptor(
  name='ScriptResult',
  full_name='executescript.ScriptResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdout', full_name='executescript.ScriptResult.stdout', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='executescript.ScriptResult.stderr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exitcode', full_name='executescript.ScriptResult.exitcode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=156,
  serialized_end=220,
)

_SCRIPTCHOICE.fields_by_name['script'].enum_type = _SCRIPTCHOICE_SCRIPT
_SCRIPTCHOICE_SCRIPT.containing_type = _SCRIPTCHOICE
DESCRIPTOR.message_types_by_name['ScriptChoice'] = _SCRIPTCHOICE
DESCRIPTOR.message_types_by_name['ScriptResult'] = _SCRIPTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScriptChoice = _reflection.GeneratedProtocolMessageType('ScriptChoice', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTCHOICE,
  '__module__' : 'execute_script_pb2'
  # @@protoc_insertion_point(class_scope:executescript.ScriptChoice)
  })
_sym_db.RegisterMessage(ScriptChoice)

ScriptResult = _reflection.GeneratedProtocolMessageType('ScriptResult', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTRESULT,
  '__module__' : 'execute_script_pb2'
  # @@protoc_insertion_point(class_scope:executescript.ScriptResult)
  })
_sym_db.RegisterMessage(ScriptResult)



_EXECUTER = _descriptor.ServiceDescriptor(
  name='Executer',
  full_name='executescript.Executer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=222,
  serialized_end=309,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteScript',
    full_name='executescript.Executer.ExecuteScript',
    index=0,
    containing_service=None,
    input_type=_SCRIPTCHOICE,
    output_type=_SCRIPTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTER)

DESCRIPTOR.services_by_name['Executer'] = _EXECUTER

# @@protoc_insertion_point(module_scope)
