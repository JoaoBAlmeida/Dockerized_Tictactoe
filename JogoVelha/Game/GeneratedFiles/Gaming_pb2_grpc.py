# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Gaming_pb2 as Gaming__pb2


class GamingStub(object):
    """Gaming Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayWelcome = channel.unary_unary(
                '/JogoVelha.Gaming/SayWelcome',
                request_serializer=Gaming__pb2.UserRegistry.SerializeToString,
                response_deserializer=Gaming__pb2.WelcomeReply.FromString,
                )
        self.makeMove = channel.unary_unary(
                '/JogoVelha.Gaming/makeMove',
                request_serializer=Gaming__pb2.UserRegistry.SerializeToString,
                response_deserializer=Gaming__pb2.Board.FromString,
                )
        self.setDraw = channel.unary_unary(
                '/JogoVelha.Gaming/setDraw',
                request_serializer=Gaming__pb2.Board.SerializeToString,
                response_deserializer=Gaming__pb2.Board.FromString,
                )


class GamingServicer(object):
    """Gaming Service
    """

    def SayWelcome(self, request, context):
        """Sends welcome message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def makeMove(self, request, context):
        """Function to make a board move
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setDraw(self, request, context):
        """Function for a draw
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GamingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayWelcome': grpc.unary_unary_rpc_method_handler(
                    servicer.SayWelcome,
                    request_deserializer=Gaming__pb2.UserRegistry.FromString,
                    response_serializer=Gaming__pb2.WelcomeReply.SerializeToString,
            ),
            'makeMove': grpc.unary_unary_rpc_method_handler(
                    servicer.makeMove,
                    request_deserializer=Gaming__pb2.UserRegistry.FromString,
                    response_serializer=Gaming__pb2.Board.SerializeToString,
            ),
            'setDraw': grpc.unary_unary_rpc_method_handler(
                    servicer.setDraw,
                    request_deserializer=Gaming__pb2.Board.FromString,
                    response_serializer=Gaming__pb2.Board.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'JogoVelha.Gaming', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gaming(object):
    """Gaming Service
    """

    @staticmethod
    def SayWelcome(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoVelha.Gaming/SayWelcome',
            Gaming__pb2.UserRegistry.SerializeToString,
            Gaming__pb2.WelcomeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def makeMove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoVelha.Gaming/makeMove',
            Gaming__pb2.UserRegistry.SerializeToString,
            Gaming__pb2.Board.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setDraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoVelha.Gaming/setDraw',
            Gaming__pb2.Board.SerializeToString,
            Gaming__pb2.Board.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
