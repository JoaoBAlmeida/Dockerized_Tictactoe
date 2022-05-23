# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Gaming.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cGaming.proto\x12\tJogoVelha\"S\n\x0cUserRegistry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nboardXMove\x18\x02 \x01(\x05\x12\x12\n\nboardYMove\x18\x03 \x01(\x05\x12\r\n\x05piece\x18\x04 \x01(\t\"1\n\x08UserMove\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.JogoVelha.UserRegistry\"\x1f\n\x0cWelcomeReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x05\x42oard\x12\x0e\n\x06pieces\x18\x01 \x01(\t2\xb4\x01\n\x06Gaming\x12@\n\nSayWelcome\x12\x17.JogoVelha.UserRegistry\x1a\x17.JogoVelha.WelcomeReply\"\x00\x12\x37\n\x08makeMove\x12\x17.JogoVelha.UserRegistry\x1a\x10.JogoVelha.Board\"\x00\x12/\n\x07setDraw\x12\x10.JogoVelha.Board\x1a\x10.JogoVelha.Board\"\x00\x62\x06proto3')



_USERREGISTRY = DESCRIPTOR.message_types_by_name['UserRegistry']
_USERMOVE = DESCRIPTOR.message_types_by_name['UserMove']
_WELCOMEREPLY = DESCRIPTOR.message_types_by_name['WelcomeReply']
_BOARD = DESCRIPTOR.message_types_by_name['Board']
UserRegistry = _reflection.GeneratedProtocolMessageType('UserRegistry', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTRY,
  '__module__' : 'Gaming_pb2'
  # @@protoc_insertion_point(class_scope:JogoVelha.UserRegistry)
  })
_sym_db.RegisterMessage(UserRegistry)

UserMove = _reflection.GeneratedProtocolMessageType('UserMove', (_message.Message,), {
  'DESCRIPTOR' : _USERMOVE,
  '__module__' : 'Gaming_pb2'
  # @@protoc_insertion_point(class_scope:JogoVelha.UserMove)
  })
_sym_db.RegisterMessage(UserMove)

WelcomeReply = _reflection.GeneratedProtocolMessageType('WelcomeReply', (_message.Message,), {
  'DESCRIPTOR' : _WELCOMEREPLY,
  '__module__' : 'Gaming_pb2'
  # @@protoc_insertion_point(class_scope:JogoVelha.WelcomeReply)
  })
_sym_db.RegisterMessage(WelcomeReply)

Board = _reflection.GeneratedProtocolMessageType('Board', (_message.Message,), {
  'DESCRIPTOR' : _BOARD,
  '__module__' : 'Gaming_pb2'
  # @@protoc_insertion_point(class_scope:JogoVelha.Board)
  })
_sym_db.RegisterMessage(Board)

_GAMING = DESCRIPTOR.services_by_name['Gaming']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERREGISTRY._serialized_start=27
  _USERREGISTRY._serialized_end=110
  _USERMOVE._serialized_start=112
  _USERMOVE._serialized_end=161
  _WELCOMEREPLY._serialized_start=163
  _WELCOMEREPLY._serialized_end=194
  _BOARD._serialized_start=196
  _BOARD._serialized_end=219
  _GAMING._serialized_start=222
  _GAMING._serialized_end=402
# @@protoc_insertion_point(module_scope)
