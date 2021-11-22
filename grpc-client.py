import grpc
from Version.proto import Version_pb2, Version_pb2_grpc, Versioning_pb2_grpc, Versioning_pb2
from django.db import IntegrityError, transaction
try:
    # with transcaction.atomic():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Versioning_pb2_grpc.VersioningServiceStub(channel)
        print('----- Create -----')
        response = stub.postVersion(Versioning_pb2.PostVersionRequest(
                names = 'test_microservice', 
                codeBases = 'Python', 
                versions = '0.1', 
                activeStates = True
            ))
        print((response), end='')

        print('----- List -----')
        post = stub.getMultiVersion(Versioning_pb2.GetMultiVersionRequest())
        print(post, end='')

        print('----- Retrieve -----')
        response = stub.getSingleVersion(Versioning_pb2.VersionIdRequest(id=response.id))
        print(response, end='')

        print('----- Update -----')
        response = stub.putVersion(Versioning_pb2.PutVersionRequest(
            id=response.id, 
            names='microservices', 
            codeBases='Python3', 
            versions='0.1'
            ))
        print(response, end='')

        print('----- Delete -----')
        response = stub.deleteVersion(Versioning_pb2.VersionIdRequest(id=response.id))
        print((response), end='')

        print('----- List Again -----')
        post = stub.getMultiVersion(Versioning_pb2.GetMultiVersionRequest())
        print(post, end='')

except IntegrityError as i:
    print(i)
except Exception as e:
    print(e)