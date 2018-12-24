# textecho
# 8105

import sys
from concurrent import futures
import time

import grpc

sys.path.append("./service_spec")
import textecho_pb2 as pb2
import textecho_pb2_grpc as pb2_grpc

# SERVICE_API
class ServiceDefinition(pb2_grpc.ServiceDefinitionServicer):

    def __init__(self):
        self.in_text = ""
        self.response = None

    def communicate(self, request, context):
        self.in_text = request.in_text
        self.response = pb2.Output()
        self.response.out_text = "You said {}".format(request.in_text)
        return self.response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ServiceDefinitionServicer_to_server(ServiceDefinition(), server)
    server.add_insecure_port('[::]:8105')
    server.start()
    print("Server listening on 0.0.0.0:{}".format(8105))
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()
