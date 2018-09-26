# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import GT_balance_pb2 as GT__balance__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/gtrouter.Greeter/SayHello',
        request_serializer=GT__balance__pb2.HelloRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.HelloReply.FromString,
        )
    self.SayHelloAgain = channel.unary_unary(
        '/gtrouter.Greeter/SayHelloAgain',
        request_serializer=GT__balance__pb2.HelloRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.HelloReply.FromString,
        )
    self.CPUProcessRequest = channel.unary_unary(
        '/gtrouter.Greeter/CPUProcessRequest',
        request_serializer=GT__balance__pb2.CPU_coresRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.HelloReply.FromString,
        )
    self.GetCPUtemp = channel.unary_unary(
        '/gtrouter.Greeter/GetCPUtemp',
        request_serializer=GT__balance__pb2.HelloRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.HelloReply.FromString,
        )
    self.GetFanRotation = channel.unary_unary(
        '/gtrouter.Greeter/GetFanRotation',
        request_serializer=GT__balance__pb2.HelloRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.HelloReply.FromString,
        )
    self.GetCPUutil = channel.unary_unary(
        '/gtrouter.Greeter/GetCPUutil',
        request_serializer=GT__balance__pb2.HelloRequest.SerializeToString,
        response_deserializer=GT__balance__pb2.CPUutilReply.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloAgain(self, request, context):
    """Send another greetingly
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CPUProcessRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCPUtemp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFanRotation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCPUutil(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=GT__balance__pb2.HelloRequest.FromString,
          response_serializer=GT__balance__pb2.HelloReply.SerializeToString,
      ),
      'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
          servicer.SayHelloAgain,
          request_deserializer=GT__balance__pb2.HelloRequest.FromString,
          response_serializer=GT__balance__pb2.HelloReply.SerializeToString,
      ),
      'CPUProcessRequest': grpc.unary_unary_rpc_method_handler(
          servicer.CPUProcessRequest,
          request_deserializer=GT__balance__pb2.CPU_coresRequest.FromString,
          response_serializer=GT__balance__pb2.HelloReply.SerializeToString,
      ),
      'GetCPUtemp': grpc.unary_unary_rpc_method_handler(
          servicer.GetCPUtemp,
          request_deserializer=GT__balance__pb2.HelloRequest.FromString,
          response_serializer=GT__balance__pb2.HelloReply.SerializeToString,
      ),
      'GetFanRotation': grpc.unary_unary_rpc_method_handler(
          servicer.GetFanRotation,
          request_deserializer=GT__balance__pb2.HelloRequest.FromString,
          response_serializer=GT__balance__pb2.HelloReply.SerializeToString,
      ),
      'GetCPUutil': grpc.unary_unary_rpc_method_handler(
          servicer.GetCPUutil,
          request_deserializer=GT__balance__pb2.HelloRequest.FromString,
          response_serializer=GT__balance__pb2.CPUutilReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gtrouter.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
