from django_grpc_framework.services import Service
from django_grpc_framework import generics
from .serializers import versionSerializer
from google.protobuf import empty_pb2
from .proto import Versioning_pb2
from .models import Versions
import grpc
# from proto.Versioning_pb2 import
# class VersionsService(generics.ModelService):
#     """
#     gRPC service that allows users to be retrieved or updated.
#     """
#     queryset = Versions.objects.all().order_by('-names')
#     serializer_class = versionSerializer

class VersionsService(Service):
    def get_object(self, pk, singular=False):
        try:
            if singular:
                print('singular')
                rsp = Versions.objects.get(id=pk)
            else:
                print('non singular')
                rsp = Versions.objects.all()
            print('Rsp >>',rsp)
            return rsp
        except Versions.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'ID {pk} NOT FOUND')
        except Exception as q:
            print(q)
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'ID {pk} NOT FOUND')

    def getSingleVersion(self, request, context):
        queryset = self.get_object(request.id, True)
        serializer = versionSerializer(queryset)
        return serializer.message

    def getMultiVersion(self, request, context):
        queryset = self.get_object(None, False)
        serializer = versionSerializer(queryset, many=True)
        response = Versioning_pb2.GetMultiVersionResponse()
        for data in serializer.message:
            response.version.append(data)
        return response

    def deleteVersion(self, request, context):
        queryset = self.get_object(request.id, True)
        serializer = versionSerializer(queryset)
        queryset.delete()
        response = Versioning_pb2.DeleteVersionResponse()
        response.status = True
        return response

    # def forceDeleteVersion(self.request, context):
    #     return

    def postVersion(self, request, context):
        payload = {
            "names" : request.names,
            "codeBases" : request.codeBases,
            "activeStates" : request.activeStates,
            "versions" : request.versions
        }
        queryset = Versions.objects.create(**payload)
        serializer = versionSerializer(queryset)
        print(f"postVersion Response {serializer.message} <<<<")
        return serializer.message
    
    def putVersion(self, request, context):
        queryset = self.get_object(request.id, True)
        serializer = versionSerializer(queryset, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message