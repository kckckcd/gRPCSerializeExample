import grpc
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc
import data_pb2


def getData():
    return pb2.request(data = getProtoData().SerializeToString())

def getProtoData():
    return data_pb2.data(name='client', message="Hi, I'm client!")

def client():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    client = pb2_grpc.testStub(channel=channel)
    client.hello(getData())


if __name__ == "__main__":
    client()