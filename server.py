import grpc
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc
import data_pb2
from concurrent import futures


class test(pb2_grpc.testServicer):

    def __init__(self):
        print("server starts>>>")

    def hello(self, request, context):
        data = data_pb2.data()
        data.ParseFromString(request.data)
        print(data.name)
        print(data.message)
        return pb2.empty()


def server():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4),
    )
    pb2_grpc.add_testServicer_to_server(test(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:50051')
    grpc_server.start()
    grpc_server.wait_for_termination()

if __name__ == "__main__":
    server()