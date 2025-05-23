# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Versioning_pb2 as Versioning__pb2


class VersioningServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getSingleVersion = channel.unary_unary(
                '/VersioningService/getSingleVersion',
                request_serializer=Versioning__pb2.VersionIdRequest.SerializeToString,
                response_deserializer=Versioning__pb2.VersionDataResponse.FromString,
                )
        self.getMultiVersion = channel.unary_unary(
                '/VersioningService/getMultiVersion',
                request_serializer=Versioning__pb2.GetMultiVersionRequest.SerializeToString,
                response_deserializer=Versioning__pb2.GetMultiVersionResponse.FromString,
                )
        self.deleteVersion = channel.unary_unary(
                '/VersioningService/deleteVersion',
                request_serializer=Versioning__pb2.VersionIdRequest.SerializeToString,
                response_deserializer=Versioning__pb2.DeleteVersionResponse.FromString,
                )
        self.forceDeleteVersion = channel.unary_unary(
                '/VersioningService/forceDeleteVersion',
                request_serializer=Versioning__pb2.VersionIdRequest.SerializeToString,
                response_deserializer=Versioning__pb2.VersionDataResponse.FromString,
                )
        self.postVersion = channel.unary_unary(
                '/VersioningService/postVersion',
                request_serializer=Versioning__pb2.PostVersionRequest.SerializeToString,
                response_deserializer=Versioning__pb2.VersionDataResponse.FromString,
                )
        self.putVersion = channel.unary_unary(
                '/VersioningService/putVersion',
                request_serializer=Versioning__pb2.PutVersionRequest.SerializeToString,
                response_deserializer=Versioning__pb2.VersionDataResponse.FromString,
                )


class VersioningServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getSingleVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMultiVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def forceDeleteVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def postVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def putVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VersioningServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getSingleVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.getSingleVersion,
                    request_deserializer=Versioning__pb2.VersionIdRequest.FromString,
                    response_serializer=Versioning__pb2.VersionDataResponse.SerializeToString,
            ),
            'getMultiVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.getMultiVersion,
                    request_deserializer=Versioning__pb2.GetMultiVersionRequest.FromString,
                    response_serializer=Versioning__pb2.GetMultiVersionResponse.SerializeToString,
            ),
            'deleteVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteVersion,
                    request_deserializer=Versioning__pb2.VersionIdRequest.FromString,
                    response_serializer=Versioning__pb2.DeleteVersionResponse.SerializeToString,
            ),
            'forceDeleteVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.forceDeleteVersion,
                    request_deserializer=Versioning__pb2.VersionIdRequest.FromString,
                    response_serializer=Versioning__pb2.VersionDataResponse.SerializeToString,
            ),
            'postVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.postVersion,
                    request_deserializer=Versioning__pb2.PostVersionRequest.FromString,
                    response_serializer=Versioning__pb2.VersionDataResponse.SerializeToString,
            ),
            'putVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.putVersion,
                    request_deserializer=Versioning__pb2.PutVersionRequest.FromString,
                    response_serializer=Versioning__pb2.VersionDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VersioningService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VersioningService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getSingleVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/getSingleVersion',
            Versioning__pb2.VersionIdRequest.SerializeToString,
            Versioning__pb2.VersionDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMultiVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/getMultiVersion',
            Versioning__pb2.GetMultiVersionRequest.SerializeToString,
            Versioning__pb2.GetMultiVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/deleteVersion',
            Versioning__pb2.VersionIdRequest.SerializeToString,
            Versioning__pb2.DeleteVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def forceDeleteVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/forceDeleteVersion',
            Versioning__pb2.VersionIdRequest.SerializeToString,
            Versioning__pb2.VersionDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def postVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/postVersion',
            Versioning__pb2.PostVersionRequest.SerializeToString,
            Versioning__pb2.VersionDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def putVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VersioningService/putVersion',
            Versioning__pb2.PutVersionRequest.SerializeToString,
            Versioning__pb2.VersionDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
