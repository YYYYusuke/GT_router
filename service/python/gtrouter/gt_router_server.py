from concurrent import futures
import time
import subprocess
import grpc
import os
import sys
import random
#import psutil
import GT_balance_pb2
import GT_balance_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Greeter(GT_balance_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return GT_balance_pb2.HelloReply(message='Hello! Processed server is %s' % request.name)

    def SayHelloAgain(self, request, context):
        return GT_balance_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def CPUProcessRequest(self, request, context):

        num_cpu=request.cpu_cores
        timeout=request.time
        print("Processed_cpu is %d cores" %num_cpu, "Processed_time is %d ms" %timeout)
        
        #stress cores on CPU ex) stress --cpu 15 --timeout 30s
        #cmd = ['ls', '-l', '/usr/bin']
        #subprocess.run(cmd)
        time.sleep(timeout)
        os.system("stress --cpu " + num_cpu + "--timeout " + "1s")
        return GT_balance_pb2.HelloReply(message='Job (Cores= %s) is completed' % num_cpu)

    def GetCPUtemp (self, request, context):
        
        return GT_balance_pb2.HelloReply(message='This is CPUtemp, %s!' % request.name)

    def GetFanRotation (self, request, context):
        
        return GT_balance_pb2.HelloReply(message='This is Fan Rotation, %s!' % request.name)

    def GetCPUutil (self, request, context):
        # Getting CPU's utilization
        # os.system(uptime)

        #MSG_from_Client=request.name
        MSG_from_Client="THis is cpu usage"
        #num =random.random()
        num = random.randint(0,10)
        return GT_balance_pb2.CPUutilReply(message=MSG_from_Client,cpu_util=num)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GT_balance_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

    """
    Start gRPC server based on given addr adn port number
    """

def serve_based_addr(addr, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GT_balance_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    addr_with_port = addr + ':' + str(port)
    server.add_insecure_port(addr_with_port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    #serve()
    args =sys.argv
    print(args[1], args[2])
    serve_based_addr(args[1], args[2])
