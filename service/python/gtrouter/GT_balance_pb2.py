# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GT_balance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GT_balance.proto',
  package='gtrouter',
  syntax='proto3',
  serialized_options=_b('\n\031io.grpc.examples.gtrouterB\rGtRouterProtoP\001\242\002\003GTR'),
  serialized_pb=_b('\n\x10GT_balance.proto\x12\x08gtrouter\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"3\n\x10\x43PU_coresRequest\x12\x11\n\tcpu_cores\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\"-\n\x0bServerReply\x12\x0e\n\x06mess_1\x18\x01 \x01(\t\x12\x0e\n\x06mess_2\x18\x02 \x01(\t\"1\n\x0c\x43PUutilReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08\x63pu_util\x18\x02 \x01(\x02\"1\n\x0c\x43PUtempReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08\x63pu_temp\x18\x02 \x01(\x02\".\n\x08\x46\x61nReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tfan_speed\x18\x02 \x01(\x02\x32\x8f\x03\n\x07Greeter\x12:\n\x08SayHello\x12\x16.gtrouter.HelloRequest\x1a\x14.gtrouter.HelloReply\"\x00\x12?\n\rSayHelloAgain\x12\x16.gtrouter.HelloRequest\x1a\x14.gtrouter.HelloReply\"\x00\x12G\n\x11\x43PUProcessRequest\x12\x1a.gtrouter.CPU_coresRequest\x1a\x14.gtrouter.HelloReply\"\x00\x12>\n\nGetCPUtemp\x12\x16.gtrouter.HelloRequest\x1a\x16.gtrouter.CPUtempReply\"\x00\x12>\n\x0eGetFanRotation\x12\x16.gtrouter.HelloRequest\x1a\x12.gtrouter.FanReply\"\x00\x12>\n\nGetCPUutil\x12\x16.gtrouter.HelloRequest\x1a\x16.gtrouter.CPUutilReply\"\x00\x42\x32\n\x19io.grpc.examples.gtrouterB\rGtRouterProtoP\x01\xa2\x02\x03GTRb\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='gtrouter.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gtrouter.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=30,
  serialized_end=58,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='gtrouter.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gtrouter.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=60,
  serialized_end=89,
)


_CPU_CORESREQUEST = _descriptor.Descriptor(
  name='CPU_coresRequest',
  full_name='gtrouter.CPU_coresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu_cores', full_name='gtrouter.CPU_coresRequest.cpu_cores', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='gtrouter.CPU_coresRequest.time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=91,
  serialized_end=142,
)


_SERVERREPLY = _descriptor.Descriptor(
  name='ServerReply',
  full_name='gtrouter.ServerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mess_1', full_name='gtrouter.ServerReply.mess_1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mess_2', full_name='gtrouter.ServerReply.mess_2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=144,
  serialized_end=189,
)


_CPUUTILREPLY = _descriptor.Descriptor(
  name='CPUutilReply',
  full_name='gtrouter.CPUutilReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gtrouter.CPUutilReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_util', full_name='gtrouter.CPUutilReply.cpu_util', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=191,
  serialized_end=240,
)


_CPUTEMPREPLY = _descriptor.Descriptor(
  name='CPUtempReply',
  full_name='gtrouter.CPUtempReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gtrouter.CPUtempReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_temp', full_name='gtrouter.CPUtempReply.cpu_temp', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=242,
  serialized_end=291,
)


_FANREPLY = _descriptor.Descriptor(
  name='FanReply',
  full_name='gtrouter.FanReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gtrouter.FanReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fan_speed', full_name='gtrouter.FanReply.fan_speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=293,
  serialized_end=339,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['CPU_coresRequest'] = _CPU_CORESREQUEST
DESCRIPTOR.message_types_by_name['ServerReply'] = _SERVERREPLY
DESCRIPTOR.message_types_by_name['CPUutilReply'] = _CPUUTILREPLY
DESCRIPTOR.message_types_by_name['CPUtempReply'] = _CPUTEMPREPLY
DESCRIPTOR.message_types_by_name['FanReply'] = _FANREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)

CPU_coresRequest = _reflection.GeneratedProtocolMessageType('CPU_coresRequest', (_message.Message,), dict(
  DESCRIPTOR = _CPU_CORESREQUEST,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.CPU_coresRequest)
  ))
_sym_db.RegisterMessage(CPU_coresRequest)

ServerReply = _reflection.GeneratedProtocolMessageType('ServerReply', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREPLY,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.ServerReply)
  ))
_sym_db.RegisterMessage(ServerReply)

CPUutilReply = _reflection.GeneratedProtocolMessageType('CPUutilReply', (_message.Message,), dict(
  DESCRIPTOR = _CPUUTILREPLY,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.CPUutilReply)
  ))
_sym_db.RegisterMessage(CPUutilReply)

CPUtempReply = _reflection.GeneratedProtocolMessageType('CPUtempReply', (_message.Message,), dict(
  DESCRIPTOR = _CPUTEMPREPLY,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.CPUtempReply)
  ))
_sym_db.RegisterMessage(CPUtempReply)

FanReply = _reflection.GeneratedProtocolMessageType('FanReply', (_message.Message,), dict(
  DESCRIPTOR = _FANREPLY,
  __module__ = 'GT_balance_pb2'
  # @@protoc_insertion_point(class_scope:gtrouter.FanReply)
  ))
_sym_db.RegisterMessage(FanReply)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='gtrouter.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=342,
  serialized_end=741,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='gtrouter.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='gtrouter.Greeter.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CPUProcessRequest',
    full_name='gtrouter.Greeter.CPUProcessRequest',
    index=2,
    containing_service=None,
    input_type=_CPU_CORESREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCPUtemp',
    full_name='gtrouter.Greeter.GetCPUtemp',
    index=3,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_CPUTEMPREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFanRotation',
    full_name='gtrouter.Greeter.GetFanRotation',
    index=4,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_FANREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCPUutil',
    full_name='gtrouter.Greeter.GetCPUutil',
    index=5,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_CPUUTILREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
