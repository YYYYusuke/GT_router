from __future__ import print_function
import grpc
import GT_balance_pb2
import GT_balance_pb2_grpc
import time
import random
from Queue import Queue
import heapq
import threading
import csv
import pandas as pd
# Myclass_below
import RRclass
import HEAPclass
import RecordClass 


#Jobs=[11,22,13,14,15,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#Jobs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
global Jobs

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
#KID_servers=[KID1, KID3, KID5, KID7, KID9, KID11]
Static_CPU_util_state=[1,1,0,0,2,2]
Static_CPU_temp_state=[1,1,0,0,2,2]

is_continued=True
path_w='/nethome/ynakajo6/local_logs'
Algorithm_time=[]


def Job_csv_reader(path_w):
	df=pd.read_csv(path_w, header=None)
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
    global Algorithm_time
    Jobs=Job_csv_reader("/nethome/ynakajo6/GT_router/Job_data/Jobs_list.csv")
    Jobs_Queue=hoge.All_Enqueue(Jobs)
    print("All jobs size is %d" % Jobs_Queue.qsize())
    
    while is_continued:
	t_algo1=time.time()

        GetSixCores()
        #RRbin()
	#ThermalBased_static()

	CPUBased_dynamic()
	#ThermalBased_dynamic()
	time.sleep(1)
	
	t_algo2=time.time()
	elapsed_algo = t_algo2 - t_algo1
	Algorithm_time.append(elapsed_algo)
	
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

def Daemon(func, IP_addr, Server_Name, int_or_queue):
     
    thread=threading.Thread(target=func, args=(IP_addr, Server_Name, int_or_queue))
    thread.setDaemon(True)
    thread.start()

def RecordDaemon(func):
    thread=threading.Thread(target=func)
    thread.setDaemon(True)
    thread.start()

if __name__ == '__main__':
    print("Cleaning old files.....")
    
    try:
	os.remove(path_w+"/algo_time.csv")
    except:
	print("Algorithm_Time file is already deleted.")
    
    print("Start")
    Daemon(ListenServeState_KID, '130.207.110.11:111', 'KID1', 0)
    Daemon(ListenServeState_KID, 'localhost:111', 'KID3', 1)
    Daemon(ListenServeState_KID, '130.207.110.17:111', 'KID7', 3)
    Daemon(ListenServeState_KID, '130.207.110.19:111', 'KID9', 4)
    Daemon(ListenServeState_KID, '130.207.110.21:111', 'KID11', 5) 
    time.sleep(1)

    Daemon(Run_KID, '130.207.110.11:111', 'KID1', KID1_Queue)
    time.sleep(1)
    Daemon(Run_KID, 'localhost:111', 'KID3', KID3_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.19:111', 'KID9', KID9_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.17:111', 'KID7', KID7_Queue)
    time.sleep(1)
    Daemon(Run_KID, '130.207.110.21:111', 'KID11', KID11_Queue)

    RecordDaemon(GetSensorsLoop)
    time.sleep(1)
    RecordDaemon(GetCputilLoop)
    time.sleep(1)
    RecordDaemon(GetFANLoop)
    time.sleep(1)
    RecordDaemon(GetPSLoop)
    time.sleep(1)
    
    thread=threading.Thread(target=(RunBalancing))
    thread.setDaemon(True)
    thread.start()

    # This is going to kill the subprocess just in case that they are going to be alive after the main proces is gone.
    time.sleep(300)
    is_continued=False

    print("Average_Algorithm_time: ", sum(Algorithm_time)/len(Algorithm_time))
    with open(path_w+'/algo_time.csv', mode='w') as f:
	writer=csv.writer(f, lineterminator='\n')
	for val in Algorithm_time:
		writer.writerow([val]) 

    print("End")
