
from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc


def run():
    
    channel = grpc.insecure_channel('localhost:50051')
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name='KID1'))
    print("Load_Balancer recieved:" + response.message)

    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=16, time=3))
    print("Response: " + response.message)
    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=10, time=2))
    print("Response: " + response.message)

    response = stub.GetCPUutil(GT_balance_pb2.HelloRequest(name='cpu_usage'))
    print("Response:", response.message)
    print("CPU_util:", response.cpu_util)


    channel = grpc.insecure_channel('localhost:50052')
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name='KID3'))
    print("Load_Balancer recieved:" + response.message)
    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=16, time=1))
    print("Response: " + response.message)


# Here are load balancing methods

def RoundRobin():

    print("Round_Robin")

def ThermalBased():

    print("ThermalBased")

def CPUBased():

    print("CPUBased:")


if __name__ == '__main__':
    run()
