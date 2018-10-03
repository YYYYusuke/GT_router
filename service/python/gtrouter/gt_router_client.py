from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc
import time
from Queue import Queue
import threading

#Myclass
import RRclass


Jobs=[11,22,13,14,15,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


Balancer_Queue=Queue()
KID1_Queue=Queue()
KID3_Queue=Queue()
KID5_Queue=Queue()

CPU_util_state=[0,0,0,0,0,0]
CPU_temp_state=[0,0,0,0,0,0]

is_continued=True

def Run_KID1():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50051', 'KID1')
        # Getting a job from own queue
        cpu_core=KID1_Queue.get()
        Process_Request(stub,cpu_core, 3)
        time.sleep(1)
    

def Run_KID3():
    
    while is_continued:
        # Having a connection
        stub=Connect_servers('localhost:50052', 'KID3')
        # Getting a job from own queue
        cpu_core=KID3_Queue.get()
        Process_Request(stub, cpu_core, 1)
        time.sleep(1)
    

def Run_KID5():
    
    while is_continued:
        # Having a connection
        stub=Connect_servers('localhost:50053', 'KID5')
        # Getting a job from own queue
        cpu_core=KID5_Queue.get()
        Process_Request(stub, cpu_core, 1)
        time.sleep(1)

def ListenServeState_KID1():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50051', 'KID1')
        global CPU_util_state
        CPU_util_state[0]=Get_CPUutil(stub)
        print(CPU_util_state)

def ListenServeState_KID3():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50052', 'KID3')
        global CPU_util_state
        CPU_util_state[1]=Get_CPUutil(stub)
        print(CPU_util_state)

def ListenServeState_KID5():
    
    while is_continued:
        # Havin a connection
        stub=Connect_servers('localhost:50053', 'KID5')
        global CPU_util_state
        CPU_util_state[2]=Get_CPUutil(stub)
        print(CPU_util_state)

def Connect_servers(server_addr_port, server_name):
    channel = grpc.insecure_channel(server_addr_port)
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name=server_name))
    #print("Load_Balancer recieved:" + response.message)
    return stub


def Get_CPUutil(stub):
    response = stub.GetCPUutil(GT_balance_pb2.HelloRequest(name='Give me cpu_usage'))
    #print("Response:", response.message)
    #print("CPU_util:", response.cpu_util)
    return response.cpu_util
    
def Process_Request(stub, CPUCORES, TIME):
    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=CPUCORES, time=TIME))
    #print("Response: " + response.message)
    return response

def GetSixCores():

    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    i=0
    while i < 6:
        global Balancer_Queue
        global Jobs_queue
        Balancer_Queue=hoge.Enqueue_TO_KID(Balancer_Queue, Jobs_queue)
        i+=1
    print("Captured six cores at Load balancer")

def Contents_confir(queue):
    Contents=[]
    queueCopy=queue
    for i in range(queueCopy.qsize()):
        tmp=queueCopy.get()
        Contents.append(tmp)
    return Contents

def Daemon():
    print("Daemon")

# Here are load balancing methods

def RRbin():
    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    # Round_Robin
    while not Balancer_Queue.empty():
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)

def ThermalBased():
    print("ThermalBased")
    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    # ThermalBased
    while not Balancer_Queue.empty():
        
        # Sorting algorithms part
        
        
        
        # Queueing part
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)

def CPUBased():
    print("CPUBased:")
    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    # CPUBased
    while not Balancer_Queue.empty():
        
        # Sorting alogorithm part
        
        
        
        # Queueing part
        
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)


def RunBalancing():
    print("Start !!")
    hoge=RRclass.RR() # Make an instance
    hoge.SayHello()
    global Jobs_queue
    global Jobs
    Jobs_queue=hoge.All_Enqueue(Jobs)
    print("All jobs size is %d" % Jobs_queue.qsize())
    
    while is_continued:
        GetSixCores()
        RRbin()
    

# Confirming the Contents

    """
    print("Balancer_Queue contents are", Contents_confir(Balancer_Queue))
    print("All jobs contents are", Contents_confir(Jobs_queue))
    print("KID1_Queue contents are", Contents_confir(KID1_Queue))
    print("KID3_Queue contents are", Contents_confir(KID3_Queue))
    print("KID5_Queue contents are", Contents_confir(KID5_Queue))
    print("Demo Queue size is %d" % Balancer_Queue.qsize())
    print("All jobs size is %d" % Jobs_queue.qsize())
    print("KID1 queue size is %d" % KID1_Queue.qsize())
    print("KID3 queue size is %d" % KID3_Queue.qsize())
    print("KID5 queue size is %d" % KID5_Queue.qsize())
    """


if __name__ == '__main__':
    """    
    thread=threading.Thread(target=(RunBalancing))
    thread_1 = threading.Thread(target=Run_KID1)
    thread_3 = threading.Thread(target=Run_KID3)
    thread_5 = threading.Thread(target=Run_KID5)
    thread.setDaemon(True)
    thread_1.setDaemon(True)
    thread_3.setDaemon(True)
    thread_5.setDaemon(True)
    thread.start()
    time.sleep(1)
    thread_1.start()
    time.sleep(1)
    thread_3.start()
    time.sleep(1)
    thread_5.start()
    """
    

# For thread
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
    
    # This is going to kill the subprocess just in case that they are going to be alive after the main proces is gone.
    time.sleep(50)
    is_continued=False
    
