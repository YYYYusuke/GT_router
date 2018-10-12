from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc
import time
import random
from Queue import Queue
import heapq
import threading
# Myclass_below
import RRclass
import HEAPclass

#Jobs=[11,22,13,14,15,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Jobs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

Balancer_Queue=Queue()
Jobs_Queue=Queue()
KID1_Queue=Queue()
KID3_Queue=Queue()
KID5_Queue=Queue()
KID7_Queue=Queue()
KID9_Queue=Queue()
KID11_Queue=Queue()

# For dynamic
CPU_util_state=[0,0,0,0,0,0]
Fan_state=[0,0,0,0,0,0]
CPU_temp_state=[0,0,0,0,0,0]
#CPU_temp_state=[12,10,11,9,2,3]

# For static
Static_CPU_util_state=[1,1,0,0,2,2]
Static_CPU_temp_state=[1,1,0,0,2,2]
#KID_servers=[KID1, KID3, KID5, KID7, KID9, KID11]

is_continued=True

def Run_KID(IP_Port, Server_Name, Queue):
    print("Running " + Server_Name + " at IPaddr:" + IP_Port)
    while is_continued:
        # Havin a connection
        stub=Connect_servers(IP_Port, Server_Name)
        # Getting a job from own queue
        cpu_core=Queue.get()
        timeout=random.randint(1,5)
        Process_Request(stub,cpu_core, timeout)
        time.sleep(1)

    
def ListenServeState_KID(IP_Port, Server_Name, state_num):
    print("Listen Server state of " + Server_Name + ". IPaddr:" + IP_Port)
    while is_continued:
        # Havin a connection
        stub=Connect_servers(IP_Port, Server_Name)
        global CPU_util_state
	global CPU_temp_state
	global Fan_state
        CPU_util_state[state_num]=Get_CPUutil(stub)
	CPU_temp_state[state_num]=Get_CPUtemp(stub)
	Fan_state[state_num]=Get_FAN(stub)
        print("CPU_utilization: ",  CPU_util_state)
        print("CPU_Temperature: ", CPU_temp_state)
        print("Local Fan Rotation speed:", Fan_state)
        print("----------------------------------------")

def Connect_servers(server_addr_port, server_name):
    channel = grpc.insecure_channel(server_addr_port)
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name=server_name))
    #print("Load_Balancer recieved:" + response.message)
    return stub

def Get_CPUutil(stub):
    response = stub.GetCPUutil(GT_balance_pb2.HelloRequest(name='Give me cpu_usage'))
    return response.cpu_util

def Get_FAN(stub):
    response = stub.GetFanRotation(GT_balance_pb2.HelloRequest(name='Give me fan_speed'))
    return response.fan_speed
    
def Get_CPUtemp(stub):
    response = stub.GetCPUtemp(GT_balance_pb2.HelloRequest(name='Give me cpu_temp'))
    return response.cpu_temp

def Process_Request(stub, CPUCORES, TIME):
    response = stub.CPUProcessRequest(GT_balance_pb2.CPU_coresRequest(cpu_cores=CPUCORES, time=TIME))
    #print("Response: " + response.message)
    return response

def GetSixCores():
    hoge=RRclass.RR() # Make an instance
    i=0
    while i < 6:
        global Balancer_Queue
        global Jobs_Queue
        Balancer_Queue=hoge.Enqueue_TO_KID(Balancer_Queue, Jobs_Queue)
        i+=1
    print("Captured six cores at Load balancer")

def QueueTolist(queue):
    Contents=[]
    queueCopy=queue
    for i in range(queueCopy.qsize()):
        tmp=queueCopy.get()
        Contents.append(tmp)
    return Contents

# Here are load balancing methods

def RRbin():
    hoge=RRclass.RR() # Make an instance
    # Round_Robin
    while not Balancer_Queue.empty():
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def ThermalBased_static():
    print("ThermalBased_static")
    hoge=RRclass.RR() # Make an instance
    #ThermalBased
    # Sorting algorithms part
    hoge=RRclass.RR() # Make an instance
    global Static_CPU_temp_state
    global Balancer_Queue
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_Queue_size_before_sorting =", Balancer_Queue.qsize())
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(Static_CPU_temp_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
    # Queueing part
    RRbin()

def CPUBased_static():
    print("CPUBased_static")
    hoge=RRclass.RR() # Make an instance
    #CPUBased
    # Sorting alogorithm part
    hoge=RRclass.RR() # Make an instance
    global Static_CPU_util_state
    global Balancer_Queue
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_Queue_size_before_sorting =", Balancer_Queue.qsize())
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(Static_CPU_util_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
    # Queueing part
    RRbin()

def CPUBased_dynamic():
    print("CPUBased_dynamic")
    hoge=RRclass.RR() # Make an instance
    # Sorting alogorithm part
    global CPU_util_state
    global Balancer_Queue
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_Queue_size_before_sorting =", Balancer_Queue.qsize())
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(CPU_util_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
	
    while not Balancer_Queue.empty():
        # Queueing part
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def ThermalBased_dynamic():
    print("ThermalBased_dynamic")
    hoge=RRclass.RR() # Make an instance
    # CPUBased
    global CPU_temp_state
    global Balancer_Queue
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_Queue_size_before_sorting =", Balancer_Queue.qsize())
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(CPU_temp_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
	
    while not Balancer_Queue.empty():
        # Queueing part
        global KID1_Queue
        global KID3_Queue
        global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def RunBalancing():
    print("Start !!")
    hoge=RRclass.RR() # Make an instance
    global Jobs_Queue
    global Jobs
    Jobs_Queue=hoge.All_Enqueue(Jobs)
    print("All jobs size is %d" % Jobs_Queue.qsize())
    
    while is_continued:
        GetSixCores()
        #RRbin()
	CPUBased_dynamic()
	#ThermalBased_dynamic()
	#ThermalBased_static()
	time.sleep(1)
    
def Daemon(func, IP_addr, Server_Name, int_or_queue):
     
    thread=threading.Thread(target=func, args=(IP_addr, Server_Name, int_or_queue))
    thread.setDaemon(True)
    thread.start()


if __name__ == '__main__':
    
    print("Start")
    t1 = time.time()
    Daemon(ListenServeState_KID, '130.207.110.21:111', 'KID11', 5) 
    Daemon(ListenServeState_KID, '130.207.110.17:111', 'KID7', 3)
    Daemon(ListenServeState_KID, '130.207.110.11:111', 'KID1', 0)
    time.sleep(3)
    Daemon(Run_KID, '130.207.110.21:111', 'KID11', KID11_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.17:111', 'KID7', KID7_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.11:111', 'KID1', KID1_Queue)
    
    thread=threading.Thread(target=(RunBalancing))
    thread.setDaemon(True)
    thread.start()

    """
# Listening state part
    thread_state1 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.11:111', 'KID1', 0))
    thread_state3 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.13:111', 'KID3', 1))
    thread_state5 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.1?:111', 'KID5', 2))
    thread_state7 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.17:111', 'KID7', 3))
    thread_state9 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.19:111', 'KID9', 4))
    thread_state11 = threading.Thread(target=ListenServeState_KID, args=('130.207.110.21:111', 'KID11', 5))
    
    # For localhost connection
    thread_state1 = threading.Thread(target=ListenServeState_KID, args=('localhost:50051', 'KID1', 0))
    thread_state3 = threading.Thread(target=ListenServeState_KID, args=('localhost:50052', 'KID3', 1))
    thread_state5 = threading.Thread(target=ListenServeState_KID, args=('localhost:50053', 'KID5', 2))
    thread_state7 = threading.Thread(target=ListenServeState_KID, args=('localhost:50054', 'KID7', 3))
    thread_state9 = threading.Thread(target=ListenServeState_KID, args=('localhost:50055', 'KID9', 4))
    thread_state11 = threading.Thread(target=ListenServeState_KID, args=('localhost:50056', 'KID11', 5))
    
    thread_state1.setDaemon(True)
    thread_state3.setDaemon(True)
    thread_state5.setDaemon(True)
    thread_state7.setDaemon(True)
    thread_state9.setDaemon(True)
    thread_state11.setDaemon(True)
    
    thread_state1.start()
    thread_state3.start()
    thread_state5.start()
    thread_state7.start()
    thread_state9.start()
    thread_state11.start()
    
# For Balancing
  
    thread=threading.Thread(target=(RunBalancing))

    thread_1 = threading.Thread(target=Run_KID, args=('130.207.110.11:111', 'KID1', KID1_Queue))
    thread_3 = threading.Thread(target=Run_KID, args=('130.207.110.13:111', 'KID3', KID3_Queue))
    #thread_5 = threading.Thread(target=Run_KID, args=('130.207.110.1?:111', 'KID5', KID5_Queue))
    thread_7 = threading.Thread(target=Run_KID, args=('130.207.110.17:111', 'KID7', KID7_Queue))
    thread_9 = threading.Thread(target=Run_KID, args=('130.207.110.19:111', 'KID9', KID9_Queue))
    thread_11 = threading.Thread(target=Run_KID, args=('130.207.110.21:111', 'KID11', KID11_Queue))
    
    # For localhost connection
    thread_1 = threading.Thread(target=Run_KID, args=('localhost:50051', 'KID1', KID1_Queue))
    thread_3 = threading.Thread(target=Run_KID, args=('localhost:50052', 'KID3', KID3_Queue))
    thread_5 = threading.Thread(target=Run_KID, args=('localhost:50053', 'KID5', KID5_Queue))
    thread_7 = threading.Thread(target=Run_KID, args=('localhost:50054', 'KID7', KID7_Queue))
    thread_9 = threading.Thread(target=Run_KID, args=('localhost:50055', 'KID9', KID9_Queue))
    thread_11 = threading.Thread(target=Run_KID, args=('localhost:50056', 'KID11', KID11_Queue))
    
    thread.setDaemon(True)
    thread_1.setDaemon(True)
    thread_3.setDaemon(True)
    thread_5.setDaemon(True)
    thread_7.setDaemon(True)
    thread_9.setDaemon(True)
    thread_11.setDaemon(True)

    thread.start()
    thread_1.start()
    time.sleep(1)
    thread_3.start()
    time.sleep(1)
    thread_5.start()
    time.sleep(1)
    thread_7.start()
    time.sleep(1)
    thread_9.start()
    time.sleep(1)
    thread_11.start()
    time.sleep(1)
    """

    # This is going to kill the subprocess just in case that they are going to be alive after the main proces is gone.
    time.sleep(30)
    is_continued=False
  
    t2= time.time()
    elapsed_time = t2 - t1
    print(f"ElapsedTime:{elapsed_time}")
    print("End")
