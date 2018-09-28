
from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc
import time
import Queue
import threading

#Myclass
import RRclass


Jobs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
IDX=0
CPU_util_state=[0,0,0,0,0,0]
is_continued=True

def Run_KID1():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50051', 'KID1')
        global IDX
        cpu_core=Get_JOB(IDX)
        Process_Request(stub,cpu_core, 3)
        global IDX
        IDX += 1
        time.sleep(1)
    

def Run_KID3():
    
    while is_continued:
        # Having a connection
        stub=Connect_servers('localhost:50052', 'KID3')
        global IDX
        cpu_core=Get_JOB(IDX)
        Process_Request(stub, cpu_core, 1)
        global IDX
        IDX += 1
        time.sleep(1)
    

def Run_KID5():
    
    while is_continued:
        # Having a connection
        stub=Connect_servers('localhost:50053', 'KID5')
        global IDX
        cpu_core=Get_JOB(IDX)
        Process_Request(stub, cpu_core, 1)
        global IDX
        IDX += 1
        time.sleep(1)

def ListenServeState_KID1():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50051', 'KID1')
        global CPU_util_state
        CPU_util_state[0]=Get_CPUutil(stub)

def ListenServeState_KID3():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50052', 'KID3')
        global CPU_util_state
        CPU_util_state[1]=Get_CPUutil(stub)

def ListenServeState_KID5():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50053', 'KID5')
        global CPU_util_state
        CPU_util_state[2]=Get_CPUutil(stub)

def Get_JOB(idx):
    cpu_core=Jobs[idx]
    return cpu_core

def Connect_servers(server_addr_port, server_name):
    channel = grpc.insecure_channel(server_addr_port)
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name=server_name))
    print("Load_Balancer recieved:" + response.message)
    return stub


def Get_CPUutil(stub):
    response = stub.GetCPUutil(GT_balance_pb2.HelloRequest(name='cpu_usage'))
    #print("Response:", response.message)
    #print("CPU_util:", response.cpu_util)
    return response.cpu_util
    
def Process_Request(stub, CPUCORES, TIME):
    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=CPUCORES, time=TIME))
    print("Response: " + response.message)
    return response

# Here are load balancing methods

def RoundRobin(Jobs):
    print("Round_Robin")

    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    Jobs_queue=hoge.All_Enqueue(Jobs)
    print("All jobs size is %d" % Jobs_queue.qsize())
    Kid1_queue=hoge.Enqueue_TO_KID1(Jobs_queue)
    print("KID1 queue size is %d" % Kid1_queue.qsize())

    while not Jobs_queue.empty():
        

def ThermalBased():
    
    print("ThermalBased")

def CPUBased():
    
    print("CPUBased:")

if __name__ == '__main__':
    
    RoundRobin(Jobs)



# For thread
    """
    thread_1 = threading.Thread(target=Run_KID1)
    thread_3 = threading.Thread(target=Run_KID3)
    thread_5 = threading.Thread(target=Run_KID5)
    thread_state1 = threading.Thread(target=ListenServeState_KID1)
    thread_state3 = threading.Thread(target=ListenServeState_KID3)
    thread_state5 = threading.Thread(target=ListenServeState_KID5)

    thread_1.setDaemon(True)
    thread_3.setDaemon(True)
    thread_5.setDaemon(True)
    thread_state1.setDaemon(True)
    thread_state3.setDaemon(True)
    thread_state5.setDaemon(True)

    thread_state1.start()
    thread_state3.start()
    thread_state5.start()

    thread_1.start()
    time.sleep(1)
    thread_3.start()
    time.sleep(1)
    thread_5.start()
    """
    
    # This is going to kill the subprocess just in case that they are going to be alive after the main proces is gone.
    time.sleep(10)
    is_continued=False
    
