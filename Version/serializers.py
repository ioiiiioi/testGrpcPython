from django_grpc_framework import proto_serializers
from .models import Versions
from .proto import Version_pb2, Versioning_pb2

class versionSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Versions
        proto_class = Versioning_pb2.VersionDataResponse
        fields = ['id', 'names', 'codeBases','versions','activeStates', 'description', 'createAt', 'updateAt', 'deleteAt']