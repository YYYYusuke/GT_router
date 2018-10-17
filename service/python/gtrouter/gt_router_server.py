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
import re
import threading
import RecordClass
import psutil

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
is_continued = True
path_w='/nethome/ynakajo6/local_logs'

class Greeter(GT_balance_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return GT_balance_pb2.HelloReply(message='Hello! Processed server is %s' % request.name)

    def SayHelloAgain(self, request, context):
        return GT_balance_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def CPUProcessRequest(self, request, context):

        num_cpu=request.cpu_cores
        timeout=request.time
        print("Processed_cpu is %d cores" %num_cpu, "Processed_time is %d ms" %timeout)
        os.system("stress --cpu " + str(num_cpu) + " --timeout " + str(timeout) + "s")
        
        return GT_balance_pb2.HelloReply(message='Job (Cores= %s) is completed' % num_cpu)

    def GetCPUtemp (self, request, context):
	"""
        cpu_temp=commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
	CPU_temp=cpu_temp.split(",")
	SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
	cpu_temp=SumOfCPUtemp/2
	"""
	core_temp=commands.getoutput("sensors | grep Core")
	tmp=re.split('[()]', core_temp)
	Hoge=[]

	for i in range(0, len(tmp)-1, 2):
		A=re.split('[+C]', tmp[i])
		Hoge.append(float(A[2]))

	cpu_temp=sum(Hoge)/len(Hoge)

        return GT_balance_pb2.CPUtempReply(message='This is CPUtemp, %s!', cpu_temp=cpu_temp)

    def GetFanRotation (self, request, context):
	fan_rotation=commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
	Fan_rotation=fan_rotation.split(",")
	SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
	fan_speed=SumOfFan/2
        return GT_balance_pb2.FanReply(message="Fan_speed",fan_speed=fan_speed )

    def GetCPUutil (self, request, context):
	"""
        MSG_from_Client="THis is cpu usage within 1 min"
	uptime=commands.getoutput("uptime")
	Load_avg=uptime.split(":")
	LoadAvg=Load_avg[-1].split(",")
        cpu_util=float(LoadAvg[0]) 
	"""
	cpu_util=psutil.cpu_percent(interval=1)

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
	is_continued=False

    """
    Start gRPC server based on given addr adn port number
    """

def serve_based_addr(addr, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GT_balance_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    #addr_with_port = '130.207.110.' + addr + ':' + str(port)
    addr_with_port = addr + ':' + str(port)
    server.add_insecure_port(addr_with_port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
	is_continued=False

def GetSensorsLoop():
    fuga=RecordClass.Record()
    while is_continued:
	fuga.GetSensors()
	time.sleep(1)
	
def GetFANLoop():
    fuga=RecordClass.Record()
    while is_continued:
	fuga.GetFanRotation()
	time.sleep(1)

def GetCputilLoop():
    fuga=RecordClass.Record()
    while is_continued:
	fuga.GetCPUutil()
	time.sleep(1)

def GetPSLoop():
    fuga=RecordClass.Record()
    while is_continued:
	fuga.GetPSutil()
	time.sleep(1)

def RecordDaemon(func):
    thread=threading.Thread(target=func)
    thread.setDaemon(True)
    thread.start()

if __name__ == '__main__':
    print("Cleaning old files.....")
    try:
	os.remove(path_w+"/PStest.csv")
    except:
	print("PS file is already deleted.")
    try:
	os.remove(path_w+"/CPU_temp_test.csv")
    except:
	print("CPU_temp file is already deleted.")
    try:
	os.remove(path_w+"/CPU_temp_sensorstest.csv")
    except:
	print("Sensors file is already deleted.")
    try:
	os.remove(path_w+"/FANtest.csv")
    except:
	print("FAN file is already deleted.")
    try:
	os.remove(path_w+"/CPU_util_test.csv")
    except:
	print("CPU util file is already deleted.") 

    print("StartRecording.....")
    RecordDaemon(GetSensorsLoop)
    time.sleep(1)
    RecordDaemon(GetFANLoop)
    time.sleep(1)
    RecordDaemon(GetCputilLoop)
    time.sleep(1)
    RecordDaemon(GetPSLoop)
    print("Opening server.....") 
    args =sys.argv
    print(args[1], args[2])
    serve_based_addr(args[1], args[2])
