# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LedgerWalletProxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LedgerWalletProxy.proto',
  package='',
  serialized_pb=_b('\n\x17LedgerWalletProxy.proto\"\\\n\rCodeRangeType\x12\r\n\x05\x66lags\x18\x01 \x02(\r\x12\r\n\x05start\x18\x02 \x02(\r\x12\x0b\n\x03\x65nd\x18\x03 \x02(\r\x12\x12\n\ndataLength\x18\x04 \x02(\r\x12\x0c\n\x04\x64\x61ta\x18\x05 \x02(\x0c\"1\n\x0bOpenSession\x12\r\n\x05nvram\x18\x01 \x01(\x0c\x12\x13\n\x0b\x61ttestation\x18\x02 \x01(\x0c\"\x0e\n\x0c\x43loseSession\"w\n\tStartCode\x12\x12\n\nentryPoint\x18\x01 \x02(\r\x12\x11\n\tstackSize\x18\x02 \x02(\r\x12\x1c\n\x04\x63ode\x18\x03 \x03(\x0b\x32\x0e.CodeRangeType\x12\x12\n\nparameters\x18\x04 \x01(\x0c\x12\x11\n\tsignature\x18\x05 \x02(\x0c\"\x0c\n\nResumeCode\"\n\n\x08GetNVRAM\"\x10\n\x0eGetAttestation\"\x1e\n\x0e\x45xchangeWallet\x12\x0c\n\x04\x61pdu\x18\x01 \x01(\x0c\"\x91\x02\n\x18LedgerWalletProxyRequest\x12!\n\x0bopenSession\x18\x01 \x01(\x0b\x32\x0c.OpenSession\x12#\n\x0c\x63loseSession\x18\x02 \x01(\x0b\x32\r.CloseSession\x12\x1d\n\tstartCode\x18\x03 \x01(\x0b\x32\n.StartCode\x12\x1f\n\nresumeCode\x18\x04 \x01(\x0b\x32\x0b.ResumeCode\x12\x1b\n\x08getNVRAM\x18\x05 \x01(\x0b\x32\t.GetNVRAM\x12\'\n\x0egetAttestation\x18\x06 \x01(\x0b\x32\x0f.GetAttestation\x12\'\n\x0e\x65xchangeWallet\x18\x07 \x01(\x0b\x32\x0f.ExchangeWallet\"\t\n\x07\x42usyAck\"\x19\n\x06LogAck\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x0c\n\nGenericAck\"!\n\x0fGenericErrorAck\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\x1c\n\x0bGetNVRAMAck\x12\r\n\x05nvram\x18\x01 \x02(\x0c\"(\n\x11GetAttestationAck\x12\x13\n\x0b\x61ttestation\x18\x01 \x02(\x0c\"%\n\x11\x45xchangeWalletAck\x12\x10\n\x08response\x18\x01 \x02(\x0c\"(\n\x14StartCodeResponseAck\x12\x10\n\x08response\x18\x01 \x01(\x0c\"&\n\x11StartCodeErrorAck\x12\x11\n\terrorCode\x18\x01 \x01(\r\"\x80\x03\n\x19LedgerWalletProxyResponse\x12\x19\n\x07\x62usyAck\x18\x01 \x01(\x0b\x32\x08.BusyAck\x12\x17\n\x06logAck\x18\x02 \x01(\x0b\x32\x07.LogAck\x12\x1f\n\ngenericAck\x18\x03 \x01(\x0b\x32\x0b.GenericAck\x12)\n\x0fgenericErrorAck\x18\x04 \x01(\x0b\x32\x10.GenericErrorAck\x12!\n\x0bgetNVRAMAck\x18\x05 \x01(\x0b\x32\x0c.GetNVRAMAck\x12-\n\x11getAttestationAck\x18\x06 \x01(\x0b\x32\x12.GetAttestationAck\x12-\n\x11\x65xchangeWalletAck\x18\x07 \x01(\x0b\x32\x12.ExchangeWalletAck\x12\x33\n\x14startCodeResponseAck\x18\x08 \x01(\x0b\x32\x15.StartCodeResponseAck\x12-\n\x11startCodeErrorAck\x18\t \x01(\x0b\x32\x12.StartCodeErrorAckB=\n com.ledger.wallet.proxy.protobufB\x19LedgerWalletProxyProtobuf')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CODERANGETYPE = _descriptor.Descriptor(
  name='CodeRangeType',
  full_name='CodeRangeType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='CodeRangeType.flags', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='CodeRangeType.start', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='CodeRangeType.end', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataLength', full_name='CodeRangeType.dataLength', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='CodeRangeType.data', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=119,
)


_OPENSESSION = _descriptor.Descriptor(
  name='OpenSession',
  full_name='OpenSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nvram', full_name='OpenSession.nvram', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attestation', full_name='OpenSession.attestation', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=170,
)


_CLOSESESSION = _descriptor.Descriptor(
  name='CloseSession',
  full_name='CloseSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=186,
)


_STARTCODE = _descriptor.Descriptor(
  name='StartCode',
  full_name='StartCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entryPoint', full_name='StartCode.entryPoint', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stackSize', full_name='StartCode.stackSize', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='StartCode.code', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='StartCode.parameters', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='StartCode.signature', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=307,
)


_RESUMECODE = _descriptor.Descriptor(
  name='ResumeCode',
  full_name='ResumeCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=321,
)


_GETNVRAM = _descriptor.Descriptor(
  name='GetNVRAM',
  full_name='GetNVRAM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=333,
)


_GETATTESTATION = _descriptor.Descriptor(
  name='GetAttestation',
  full_name='GetAttestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=351,
)


_EXCHANGEWALLET = _descriptor.Descriptor(
  name='ExchangeWallet',
  full_name='ExchangeWallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apdu', full_name='ExchangeWallet.apdu', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=383,
)


_LEDGERWALLETPROXYREQUEST = _descriptor.Descriptor(
  name='LedgerWalletProxyRequest',
  full_name='LedgerWalletProxyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openSession', full_name='LedgerWalletProxyRequest.openSession', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='closeSession', full_name='LedgerWalletProxyRequest.closeSession', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startCode', full_name='LedgerWalletProxyRequest.startCode', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resumeCode', full_name='LedgerWalletProxyRequest.resumeCode', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getNVRAM', full_name='LedgerWalletProxyRequest.getNVRAM', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getAttestation', full_name='LedgerWalletProxyRequest.getAttestation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchangeWallet', full_name='LedgerWalletProxyRequest.exchangeWallet', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=659,
)


_BUSYACK = _descriptor.Descriptor(
  name='BusyAck',
  full_name='BusyAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=670,
)


_LOGACK = _descriptor.Descriptor(
  name='LogAck',
  full_name='LogAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='LogAck.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=672,
  serialized_end=697,
)


_GENERICACK = _descriptor.Descriptor(
  name='GenericAck',
  full_name='GenericAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=711,
)


_GENERICERRORACK = _descriptor.Descriptor(
  name='GenericErrorAck',
  full_name='GenericErrorAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='GenericErrorAck.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=746,
)


_GETNVRAMACK = _descriptor.Descriptor(
  name='GetNVRAMAck',
  full_name='GetNVRAMAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nvram', full_name='GetNVRAMAck.nvram', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=748,
  serialized_end=776,
)


_GETATTESTATIONACK = _descriptor.Descriptor(
  name='GetAttestationAck',
  full_name='GetAttestationAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attestation', full_name='GetAttestationAck.attestation', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=818,
)


_EXCHANGEWALLETACK = _descriptor.Descriptor(
  name='ExchangeWalletAck',
  full_name='ExchangeWalletAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='ExchangeWalletAck.response', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=820,
  serialized_end=857,
)


_STARTCODERESPONSEACK = _descriptor.Descriptor(
  name='StartCodeResponseAck',
  full_name='StartCodeResponseAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='StartCodeResponseAck.response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=899,
)


_STARTCODEERRORACK = _descriptor.Descriptor(
  name='StartCodeErrorAck',
  full_name='StartCodeErrorAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='StartCodeErrorAck.errorCode', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=939,
)


_LEDGERWALLETPROXYRESPONSE = _descriptor.Descriptor(
  name='LedgerWalletProxyResponse',
  full_name='LedgerWalletProxyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='busyAck', full_name='LedgerWalletProxyResponse.busyAck', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logAck', full_name='LedgerWalletProxyResponse.logAck', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genericAck', full_name='LedgerWalletProxyResponse.genericAck', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genericErrorAck', full_name='LedgerWalletProxyResponse.genericErrorAck', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getNVRAMAck', full_name='LedgerWalletProxyResponse.getNVRAMAck', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getAttestationAck', full_name='LedgerWalletProxyResponse.getAttestationAck', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchangeWalletAck', full_name='LedgerWalletProxyResponse.exchangeWalletAck', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startCodeResponseAck', full_name='LedgerWalletProxyResponse.startCodeResponseAck', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startCodeErrorAck', full_name='LedgerWalletProxyResponse.startCodeErrorAck', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=1326,
)

_STARTCODE.fields_by_name['code'].message_type = _CODERANGETYPE
_LEDGERWALLETPROXYREQUEST.fields_by_name['openSession'].message_type = _OPENSESSION
_LEDGERWALLETPROXYREQUEST.fields_by_name['closeSession'].message_type = _CLOSESESSION
_LEDGERWALLETPROXYREQUEST.fields_by_name['startCode'].message_type = _STARTCODE
_LEDGERWALLETPROXYREQUEST.fields_by_name['resumeCode'].message_type = _RESUMECODE
_LEDGERWALLETPROXYREQUEST.fields_by_name['getNVRAM'].message_type = _GETNVRAM
_LEDGERWALLETPROXYREQUEST.fields_by_name['getAttestation'].message_type = _GETATTESTATION
_LEDGERWALLETPROXYREQUEST.fields_by_name['exchangeWallet'].message_type = _EXCHANGEWALLET
_LEDGERWALLETPROXYRESPONSE.fields_by_name['busyAck'].message_type = _BUSYACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['logAck'].message_type = _LOGACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['genericAck'].message_type = _GENERICACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['genericErrorAck'].message_type = _GENERICERRORACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['getNVRAMAck'].message_type = _GETNVRAMACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['getAttestationAck'].message_type = _GETATTESTATIONACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['exchangeWalletAck'].message_type = _EXCHANGEWALLETACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['startCodeResponseAck'].message_type = _STARTCODERESPONSEACK
_LEDGERWALLETPROXYRESPONSE.fields_by_name['startCodeErrorAck'].message_type = _STARTCODEERRORACK
DESCRIPTOR.message_types_by_name['CodeRangeType'] = _CODERANGETYPE
DESCRIPTOR.message_types_by_name['OpenSession'] = _OPENSESSION
DESCRIPTOR.message_types_by_name['CloseSession'] = _CLOSESESSION
DESCRIPTOR.message_types_by_name['StartCode'] = _STARTCODE
DESCRIPTOR.message_types_by_name['ResumeCode'] = _RESUMECODE
DESCRIPTOR.message_types_by_name['GetNVRAM'] = _GETNVRAM
DESCRIPTOR.message_types_by_name['GetAttestation'] = _GETATTESTATION
DESCRIPTOR.message_types_by_name['ExchangeWallet'] = _EXCHANGEWALLET
DESCRIPTOR.message_types_by_name['LedgerWalletProxyRequest'] = _LEDGERWALLETPROXYREQUEST
DESCRIPTOR.message_types_by_name['BusyAck'] = _BUSYACK
DESCRIPTOR.message_types_by_name['LogAck'] = _LOGACK
DESCRIPTOR.message_types_by_name['GenericAck'] = _GENERICACK
DESCRIPTOR.message_types_by_name['GenericErrorAck'] = _GENERICERRORACK
DESCRIPTOR.message_types_by_name['GetNVRAMAck'] = _GETNVRAMACK
DESCRIPTOR.message_types_by_name['GetAttestationAck'] = _GETATTESTATIONACK
DESCRIPTOR.message_types_by_name['ExchangeWalletAck'] = _EXCHANGEWALLETACK
DESCRIPTOR.message_types_by_name['StartCodeResponseAck'] = _STARTCODERESPONSEACK
DESCRIPTOR.message_types_by_name['StartCodeErrorAck'] = _STARTCODEERRORACK
DESCRIPTOR.message_types_by_name['LedgerWalletProxyResponse'] = _LEDGERWALLETPROXYRESPONSE

CodeRangeType = _reflection.GeneratedProtocolMessageType('CodeRangeType', (_message.Message,), dict(
  DESCRIPTOR = _CODERANGETYPE,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:CodeRangeType)
  ))
_sym_db.RegisterMessage(CodeRangeType)

OpenSession = _reflection.GeneratedProtocolMessageType('OpenSession', (_message.Message,), dict(
  DESCRIPTOR = _OPENSESSION,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:OpenSession)
  ))
_sym_db.RegisterMessage(OpenSession)

CloseSession = _reflection.GeneratedProtocolMessageType('CloseSession', (_message.Message,), dict(
  DESCRIPTOR = _CLOSESESSION,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:CloseSession)
  ))
_sym_db.RegisterMessage(CloseSession)

StartCode = _reflection.GeneratedProtocolMessageType('StartCode', (_message.Message,), dict(
  DESCRIPTOR = _STARTCODE,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:StartCode)
  ))
_sym_db.RegisterMessage(StartCode)

ResumeCode = _reflection.GeneratedProtocolMessageType('ResumeCode', (_message.Message,), dict(
  DESCRIPTOR = _RESUMECODE,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:ResumeCode)
  ))
_sym_db.RegisterMessage(ResumeCode)

GetNVRAM = _reflection.GeneratedProtocolMessageType('GetNVRAM', (_message.Message,), dict(
  DESCRIPTOR = _GETNVRAM,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GetNVRAM)
  ))
_sym_db.RegisterMessage(GetNVRAM)

GetAttestation = _reflection.GeneratedProtocolMessageType('GetAttestation', (_message.Message,), dict(
  DESCRIPTOR = _GETATTESTATION,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GetAttestation)
  ))
_sym_db.RegisterMessage(GetAttestation)

ExchangeWallet = _reflection.GeneratedProtocolMessageType('ExchangeWallet', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEWALLET,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeWallet)
  ))
_sym_db.RegisterMessage(ExchangeWallet)

LedgerWalletProxyRequest = _reflection.GeneratedProtocolMessageType('LedgerWalletProxyRequest', (_message.Message,), dict(
  DESCRIPTOR = _LEDGERWALLETPROXYREQUEST,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:LedgerWalletProxyRequest)
  ))
_sym_db.RegisterMessage(LedgerWalletProxyRequest)

BusyAck = _reflection.GeneratedProtocolMessageType('BusyAck', (_message.Message,), dict(
  DESCRIPTOR = _BUSYACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:BusyAck)
  ))
_sym_db.RegisterMessage(BusyAck)

LogAck = _reflection.GeneratedProtocolMessageType('LogAck', (_message.Message,), dict(
  DESCRIPTOR = _LOGACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:LogAck)
  ))
_sym_db.RegisterMessage(LogAck)

GenericAck = _reflection.GeneratedProtocolMessageType('GenericAck', (_message.Message,), dict(
  DESCRIPTOR = _GENERICACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GenericAck)
  ))
_sym_db.RegisterMessage(GenericAck)

GenericErrorAck = _reflection.GeneratedProtocolMessageType('GenericErrorAck', (_message.Message,), dict(
  DESCRIPTOR = _GENERICERRORACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GenericErrorAck)
  ))
_sym_db.RegisterMessage(GenericErrorAck)

GetNVRAMAck = _reflection.GeneratedProtocolMessageType('GetNVRAMAck', (_message.Message,), dict(
  DESCRIPTOR = _GETNVRAMACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GetNVRAMAck)
  ))
_sym_db.RegisterMessage(GetNVRAMAck)

GetAttestationAck = _reflection.GeneratedProtocolMessageType('GetAttestationAck', (_message.Message,), dict(
  DESCRIPTOR = _GETATTESTATIONACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:GetAttestationAck)
  ))
_sym_db.RegisterMessage(GetAttestationAck)

ExchangeWalletAck = _reflection.GeneratedProtocolMessageType('ExchangeWalletAck', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEWALLETACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeWalletAck)
  ))
_sym_db.RegisterMessage(ExchangeWalletAck)

StartCodeResponseAck = _reflection.GeneratedProtocolMessageType('StartCodeResponseAck', (_message.Message,), dict(
  DESCRIPTOR = _STARTCODERESPONSEACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:StartCodeResponseAck)
  ))
_sym_db.RegisterMessage(StartCodeResponseAck)

StartCodeErrorAck = _reflection.GeneratedProtocolMessageType('StartCodeErrorAck', (_message.Message,), dict(
  DESCRIPTOR = _STARTCODEERRORACK,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:StartCodeErrorAck)
  ))
_sym_db.RegisterMessage(StartCodeErrorAck)

LedgerWalletProxyResponse = _reflection.GeneratedProtocolMessageType('LedgerWalletProxyResponse', (_message.Message,), dict(
  DESCRIPTOR = _LEDGERWALLETPROXYRESPONSE,
  __module__ = 'LedgerWalletProxy_pb2'
  # @@protoc_insertion_point(class_scope:LedgerWalletProxyResponse)
  ))
_sym_db.RegisterMessage(LedgerWalletProxyResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.ledger.wallet.proxy.protobufB\031LedgerWalletProxyProtobuf'))
# @@protoc_insertion_point(module_scope)