# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: load_balancer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='load_balancer.proto',
  package='Load_Balancer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13load_balancer.proto\x12\rLoad_Balancer\"=\n\x16Tweet_Analyzer_Request\x12\x0f\n\x07hashtag\x18\x01 \x01(\t\x12\x12\n\nnum_tweets\x18\x02 \x01(\x05\"R\n\x14Tweet_Analyzer_Reply\x12\x12\n\npos_tweets\x18\x01 \x01(\x02\x12\x12\n\nneg_tweets\x18\x02 \x01(\x02\x12\x12\n\nneu_tweets\x18\x03 \x01(\x02\"\x18\n\x06Tweets\x12\x0e\n\x06tweets\x18\x01 \x03(\t\"\x15\n\x05\x44ummy\x12\x0c\n\x04temp\x18\x01 \x01(\x05\x32\xcf\x02\n\rLoad_Balancer\x12g\n\x17Tweet_Sentiment_Request\x12%.Load_Balancer.Tweet_Analyzer_Request\x1a#.Load_Balancer.Tweet_Analyzer_Reply\"\x00\x12\x46\n\x13Get_Positive_Tweets\x12\x14.Load_Balancer.Dummy\x1a\x15.Load_Balancer.Tweets\"\x00\x30\x01\x12\x46\n\x13Get_Negative_Tweets\x12\x14.Load_Balancer.Dummy\x1a\x15.Load_Balancer.Tweets\"\x00\x30\x01\x12\x45\n\x12Get_Neutral_Tweets\x12\x14.Load_Balancer.Dummy\x1a\x15.Load_Balancer.Tweets\"\x00\x30\x01\x62\x06proto3'
)




_TWEET_ANALYZER_REQUEST = _descriptor.Descriptor(
  name='Tweet_Analyzer_Request',
  full_name='Load_Balancer.Tweet_Analyzer_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashtag', full_name='Load_Balancer.Tweet_Analyzer_Request.hashtag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tweets', full_name='Load_Balancer.Tweet_Analyzer_Request.num_tweets', index=1,
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
  serialized_start=38,
  serialized_end=99,
)


_TWEET_ANALYZER_REPLY = _descriptor.Descriptor(
  name='Tweet_Analyzer_Reply',
  full_name='Load_Balancer.Tweet_Analyzer_Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_tweets', full_name='Load_Balancer.Tweet_Analyzer_Reply.pos_tweets', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neg_tweets', full_name='Load_Balancer.Tweet_Analyzer_Reply.neg_tweets', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neu_tweets', full_name='Load_Balancer.Tweet_Analyzer_Reply.neu_tweets', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=101,
  serialized_end=183,
)


_TWEETS = _descriptor.Descriptor(
  name='Tweets',
  full_name='Load_Balancer.Tweets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tweets', full_name='Load_Balancer.Tweets.tweets', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=185,
  serialized_end=209,
)


_DUMMY = _descriptor.Descriptor(
  name='Dummy',
  full_name='Load_Balancer.Dummy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temp', full_name='Load_Balancer.Dummy.temp', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=211,
  serialized_end=232,
)

DESCRIPTOR.message_types_by_name['Tweet_Analyzer_Request'] = _TWEET_ANALYZER_REQUEST
DESCRIPTOR.message_types_by_name['Tweet_Analyzer_Reply'] = _TWEET_ANALYZER_REPLY
DESCRIPTOR.message_types_by_name['Tweets'] = _TWEETS
DESCRIPTOR.message_types_by_name['Dummy'] = _DUMMY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tweet_Analyzer_Request = _reflection.GeneratedProtocolMessageType('Tweet_Analyzer_Request', (_message.Message,), {
  'DESCRIPTOR' : _TWEET_ANALYZER_REQUEST,
  '__module__' : 'load_balancer_pb2'
  # @@protoc_insertion_point(class_scope:Load_Balancer.Tweet_Analyzer_Request)
  })
_sym_db.RegisterMessage(Tweet_Analyzer_Request)

Tweet_Analyzer_Reply = _reflection.GeneratedProtocolMessageType('Tweet_Analyzer_Reply', (_message.Message,), {
  'DESCRIPTOR' : _TWEET_ANALYZER_REPLY,
  '__module__' : 'load_balancer_pb2'
  # @@protoc_insertion_point(class_scope:Load_Balancer.Tweet_Analyzer_Reply)
  })
_sym_db.RegisterMessage(Tweet_Analyzer_Reply)

Tweets = _reflection.GeneratedProtocolMessageType('Tweets', (_message.Message,), {
  'DESCRIPTOR' : _TWEETS,
  '__module__' : 'load_balancer_pb2'
  # @@protoc_insertion_point(class_scope:Load_Balancer.Tweets)
  })
_sym_db.RegisterMessage(Tweets)

Dummy = _reflection.GeneratedProtocolMessageType('Dummy', (_message.Message,), {
  'DESCRIPTOR' : _DUMMY,
  '__module__' : 'load_balancer_pb2'
  # @@protoc_insertion_point(class_scope:Load_Balancer.Dummy)
  })
_sym_db.RegisterMessage(Dummy)



_LOAD_BALANCER = _descriptor.ServiceDescriptor(
  name='Load_Balancer',
  full_name='Load_Balancer.Load_Balancer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=235,
  serialized_end=570,
  methods=[
  _descriptor.MethodDescriptor(
    name='Tweet_Sentiment_Request',
    full_name='Load_Balancer.Load_Balancer.Tweet_Sentiment_Request',
    index=0,
    containing_service=None,
    input_type=_TWEET_ANALYZER_REQUEST,
    output_type=_TWEET_ANALYZER_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_Positive_Tweets',
    full_name='Load_Balancer.Load_Balancer.Get_Positive_Tweets',
    index=1,
    containing_service=None,
    input_type=_DUMMY,
    output_type=_TWEETS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_Negative_Tweets',
    full_name='Load_Balancer.Load_Balancer.Get_Negative_Tweets',
    index=2,
    containing_service=None,
    input_type=_DUMMY,
    output_type=_TWEETS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_Neutral_Tweets',
    full_name='Load_Balancer.Load_Balancer.Get_Neutral_Tweets',
    index=3,
    containing_service=None,
    input_type=_DUMMY,
    output_type=_TWEETS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOAD_BALANCER)

DESCRIPTOR.services_by_name['Load_Balancer'] = _LOAD_BALANCER

# @@protoc_insertion_point(module_scope)
