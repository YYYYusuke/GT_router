from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc
import time
import datetime
import random
from Queue import Queue
import copy
import heapq
import threading
import csv
import pandas as pd
# Myclass_below import RRclass
import HEAPclass
import RRclass
import RecordClass 

#Jobs=[11,22,13,14,15,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#Jobs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
global Jobs
global MonitorQueueList
Balancer_Queue=Queue()
Jobs_Queue=Queue()
KID1_Queue=Queue()
KID3_Queue=Queue()
KID5_Queue=Queue()
KID7_Queue=Queue()
KID9_Queue=Queue()
KID11_Queue=Queue()

# For dynamic
"""
#For six queue
CPU_util_state=[0,0,0,0,0,0]
Fan_state=[0,0,0,0,0,0]
CPU_temp_state=[0,0,0,0,0,0]
"""
#For five queue
CPU_util_state=[0,0,0,0,0]
Fan_state=[0,0,0,0,0]
CPU_temp_state=[0,0,0,0,0]

# For static
#KID_servers=[KID1, KID3, KID5, KID7, KID9, KID11]
Static_CPU_util_state=[1,1,0,0,2,2]
Static_CPU_temp_state=[1,1,0,0,2,2]

is_continued=True
path_w='/nethome/ynakajo6/local_logs'
Algorithm_time=[]
E_time=[]

def Job_csv_reader(path):
	df=pd.read_csv(path, header=None)
	df=df.T.values.tolist()
	Jobs_list=df[0]
	return Jobs_list

def Run_KID(IP_Port, Server_Name, Queue):
    print("Running " + Server_Name + " at IPaddr:" + IP_Port)
    while is_continued:
        # Havin a connection
        stub=Connect_servers(IP_Port, Server_Name)
        # Getting a job from own queue
        cpu_core=Queue.get()
	timeout=1
        Process_Request(stub, cpu_core, timeout)
        time.sleep(1)

def Run_KID_TWOPorts(IP, Server_Name, Queue):
    print("Running " + Server_Name + " at IPaddr:" + IP)
    PortA=':111'
    PortB=':112'
    while is_continued:
        # Havin two connections
        stub_A=Connect_servers(IP+PortA, Server_Name)
        stub_B=Connect_servers(IP+PortB, Server_Name)
        # Getting jobs from own queue
        cpu_core_portA=Queue.get()
        cpu_core_portB=Queue.get()
        #timeout=random.randint(1,5)
	timeout=5
        Daemon(Process_Request, stub_A, cpu_core_portA, timeout)
        Daemon(Process_Request, stub_B, cpu_core_portB, timeout)
        time.sleep(1)
    
def ListenServeState_KID(IP_Port, Server_Name, state_num):
    print("Listen Server state of " + Server_Name + ". IPaddr:" + IP_Port)
    while is_continued:
        # Havin a connection
        stub=Connect_servers(IP_Port, Server_Name)
        global CPU_util_state
	global CPU_temp_state
	global Fan_state
	global E_time
	global MonitorQueueList
	#MonitorQueueList=[]

	nowi=time.time()
        CPU_util_state[state_num]=Get_CPUutil(stub)
	CPU_temp_state[state_num]=Get_CPUtemp(stub)
	Fan_state[state_num]=Get_FAN(stub)
	elapsed_CPUutil=time.time()-nowi
	E_time.append(elapsed_CPUutil)
	
	MonitorQueueList=[MonitorQueueContents(KID1_Queue), MonitorQueueContents(KID3_Queue), MonitorQueueContents(KID7_Queue), MonitorQueueContents(KID9_Queue), MonitorQueueContents(KID11_Queue)]
        print("CPU_utilization: ",  CPU_util_state)
        print("CPU_Temperature: ", CPU_temp_state)
        print("Local Fan Rotation speed:", Fan_state)
        print("Queue list: ", MonitorQueueList)
        print("----------------------------------------")

def Connect_servers(server_addr_port, server_name):
    channel = grpc.insecure_channel(server_addr_port)
    stub = GT_balance_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(GT_balance_pb2.HelloRequest(name=server_name))
    return stub

def MonitorQueueContents(KID_Queue):
    Contents=[]
    queue_copy=Queue()
    queue_copy.queue=copy.deepcopy(KID_Queue.queue)
    for i in range(KID_Queue.qsize()):
	tmp=queue_copy.get()
	Contents.append(tmp)
    return Contents
    
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

def GetFiveCores():
    hoge=RRclass.RR() # Make an instance
    i=0
    while i < 5:
        global Balancer_Queue
        global Jobs_Queue
        Balancer_Queue=hoge.Enqueue_TO_KID(Balancer_Queue, Jobs_Queue)
        i+=1
    print("Captured five cores at Load balancer")

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
        #global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        #KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def CPUBased_dynamic():
    global CPU_util_state, Balancer_Queue
    print("CPUBased_dynamic")
    hoge=RRclass.RR() # Make an instance
    # Sorting alogorithm part
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(CPU_util_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
	
    while not Balancer_Queue.empty():
        # Queueing part
        global KID1_Queue
        global KID3_Queue
        #global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        #KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def ThermalBased_dynamic():
    global CPU_temp_state, Balancer_Queue
    print("ThermalBased_dynamic")
    hoge=RRclass.RR() # Make an instance
    cores=QueueTolist(Balancer_Queue)
    print("Balancer_queue_before_sorting", cores)
    heapsort=HEAPclass.HEAP()
    sortd=heapsort.heap_route(CPU_temp_state, cores )
    Balancer_Queue=hoge.Six_Enqueue(sortd)
    print("Balancer_Queue_size_after_sorting=", Balancer_Queue.qsize())
	
    while not Balancer_Queue.empty():
        # Queueing part
        global KID1_Queue
        global KID3_Queue
        #global KID5_Queue
        global KID7_Queue
        global KID9_Queue
        global KID11_Queue
        KID1_Queue=hoge.Enqueue_TO_KID(KID1_Queue, Balancer_Queue)
        KID3_Queue=hoge.Enqueue_TO_KID(KID3_Queue, Balancer_Queue)
        #KID5_Queue=hoge.Enqueue_TO_KID(KID5_Queue, Balancer_Queue)
        KID7_Queue=hoge.Enqueue_TO_KID(KID7_Queue, Balancer_Queue)
        KID9_Queue=hoge.Enqueue_TO_KID(KID9_Queue, Balancer_Queue)
        KID11_Queue=hoge.Enqueue_TO_KID(KID11_Queue, Balancer_Queue)

def RunBalancing():
    print("Start !!")
    hoge=RRclass.RR() # Make an instance
    global Jobs_Queue
    global Jobs
    global Algorithm_time
    Jobs=Job_csv_reader("/nethome/ynakajo6/GT_router/Job_data/Jobs_list.csv")
    Jobs_Queue=hoge.All_Enqueue(Jobs)
    print("All jobs size is %d" % Jobs_Queue.qsize())
    
    while is_continued:
	t_algo1=time.time()

        GetFiveCores()
       	RRbin()
	#CPUBased_dynamic()
	#ThermalBased_dynamic()
	time.sleep(1)
	
	t_algo2=time.time()
	elapsed_algo = t_algo2 - t_algo1
	Algorithm_time.append(elapsed_algo)
	
def Daemon(func, IP_addr, Server_Name, int_or_queue):
    thread=threading.Thread(target=func, args=(IP_addr, Server_Name, int_or_queue))
    thread.setDaemon(True)
    thread.start()

def OnePortConnection():
    # ONE PORT CONNECTION
    Daemon(Run_KID, '130.207.110.11:111', 'KID1', KID1_Queue)
    time.sleep(1)
    Daemon(Run_KID, 'localhost:111', 'KID3', KID3_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.17:111', 'KID7', KID7_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.19:111', 'KID9', KID9_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.21:111', 'KID11', KID11_Queue)
	
def TwoPortConnection():
    # TWO PORT CONNECTION
    Daemon(Run_KID_TWOPorts, '130.207.110.11', 'KID1', KID1_Queue)
    time.sleep(1)
    Daemon(Run_KID_TWOPorts, 'localhost', 'KID3', KID3_Queue)
    time.sleep(1)
    Daemon(Run_KID_TWOPorts, '130.207.110.17', 'KID7', KID7_Queue)
    time.sleep(1)
    Daemon(Run_KID_TWOPorts, '130.207.110.19', 'KID9', KID9_Queue)
    time.sleep(1)
    Daemon(Run_KID_TWOPorts, '130.207.110.21', 'KID11', KID11_Queue)
    time.sleep(1)

def TestConnection():
    Daemon(Run_KID_TWOPorts, '130.207.110.11', 'KID1', KID1_Queue)
    time.sleep(1)
    print("Test connections have been made.")
    Daemon(Run_KID_TWOPorts, 'localhost', 'KID3', KID3_Queue)
    time.sleep(1)

def ServerMonitors():
    Daemon(ListenServeState_KID, '130.207.110.11:111', 'KID1', 0)
    Daemon(ListenServeState_KID, 'localhost:111', 'KID3', 1)
    Daemon(ListenServeState_KID, '130.207.110.17:111', 'KID7', 2)
    Daemon(ListenServeState_KID, '130.207.110.19:111', 'KID9', 3)
    Daemon(ListenServeState_KID, '130.207.110.21:111', 'KID11', 4) 
    time.sleep(1)

def TestServerMonitors():
    print("The test has been started !!")
    Daemon(ListenServeState_KID, '130.207.110.11:111', 'KID1', 0)
    Daemon(ListenServeState_KID, 'localhost:111', 'KID3', 1)
    time.sleep(1)

if __name__ == '__main__':
   
    # Cleaning old file part
    print("Cleaning old files.....")
    try:
	os.remove(path_w+"/algo_time.csv")
    except:
	print("Algorithm_Time file is already deleted.")
    
    print("Start")

    # Monitoring part 
    ServerMonitors()
    #TestServerMonitors()
 
    # Getting Jobs part (having the connection between servers and the balancer)
    #OnePortConnection()
    TwoPortConnection()
    #TestConnection()
    
    # Balancing part
    thread=threading.Thread(target=(RunBalancing))
    thread.setDaemon(True)
    thread.start()

    # This is going to kill the subprocess just in case that they are going to be alive after the main proces is gone.
    time.sleep(300)
    is_continued=False
    
    # Recording part
    print("Average_Algorithm_time: ", sum(Algorithm_time)/len(Algorithm_time))
    with open(path_w+'/algo_time.csv', mode='w') as f:
	writer=csv.writer(f, lineterminator='\n')
	for val in Algorithm_time:
		writer.writerow([val]) 
    print("Listneing_time: ", sum(E_time)/len(E_time))

    print("End")
