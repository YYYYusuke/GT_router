from concurrent import futures
import time
import subprocess
import grpc
import os
import sys
import random
import commands
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
        #os.system("stress --cpu " + str(num_cpu) + "--timeout " + "1s")
        os.system("stress --cpu " + str(num_cpu) + " --timeout " + str(timeout) + "s")
        
        return GT_balance_pb2.HelloReply(message='Job (Cores= %s) is completed' % num_cpu)

    def GetCPUtemp (self, request, context):
        cpu_temp=commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
	CPU_temp=cpu_temp.split(",")
	SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
	cpu_temp=SumOfCPUtemp/2
        return GT_balance_pb2.CPUtempReply(message='This is CPUtemp, %s!', cpu_temp=cpu_temp)

    def GetFanRotation (self, request, context):
	fan_rotation=commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
	Fan_rotation=fan_rotation.split(",")
	SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
	fan_speed=SumOfFan/2
        return GT_balance_pb2.FanReply(message="Fan_speed",fan_speed=fan_speed )

    def GetCPUutil (self, request, context):
        # Getting CPU's utilization
        MSG_from_Client="THis is cpu usage within 1 min"
	uptime=commands.getoutput("uptime")
	Load_avg=uptime.split(":")
	LoadAvg=Load_avg[-1].split(",")
        cpu_util=float(LoadAvg[0]) 
	return GT_balance_pb2.CPUutilReply(message=MSG_from_Client,cpu_util=cpu_util)


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
    addr_with_port = '130.207.110.' + addr + ':' + str(port)
    server.add_insecure_port(addr_with_port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    args =sys.argv
    print(args[1], args[2])
    serve_based_addr(args[1], args[2])
