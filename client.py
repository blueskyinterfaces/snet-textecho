# __PROJECT__
# __SERVICE_PORT__

import sys
import grpc

sys.path.append("./service_spec")
import textecho_pb2 as pb2
import textecho_pb2_grpc as pb2_grpc

def textEcho(channel):
    in_text = "gerror"
    if len(sys.argv) == 2:
        in_text = sys.argv[1]
    stub = pb2_grpc.ServiceDefinitionStub(channel)
    response = stub.textEcho(pb2.Input(in_text=in_text))
    print("Output: {}".format(response.out_text))
    return response

def main():
    # Connect to the server
    with grpc.insecure_channel('localhost:8105') as channel:
        textEcho(channel)

if __name__ == '__main__':
    main()