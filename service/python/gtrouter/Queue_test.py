from Queue import Queue
import copy

# For static round robin balancing

Jobs =[1,2,2,3,4,4,15,12,21,16,12,12,15,18,19,24]

Jobs_queue = Queue()
Kid1_queue = Queue()
Kid3_queue = Queue()
Kid5_queue = Queue()


def All_Enqueue(Jobs):
  for i in Jobs:
    global Jobs_queue
    Jobs_queue.put(i)
    #print("Enqueue:%d" %i)

def Enqueue(KID_queue, q):
  if q.empty():
    print("Empty")
  else:
    KID_queue=q.get()
    print(KID_queue)

def Enqueue_TO_KID(Kid_queue, q):
  if q.empty():
    print("Empty")
  else:
    tmp=q.get()
    Kid_queue.put(tmp)

def Dequeue(q):
  if q.empty():
    #break
    print("Empty")
  else:
    i = q.get()
    print("Dequeue:%d" %i)
  return i

def Contents_confir(queue):
    Contents=[]
    queue_copy=Queue()
    queue_copy.queue=copy.deepcopy(queue.queue)
    for i in range(queue.qsize()):
        tmp=queue_copy.get()
        Contents.append(tmp)
    return Contents

def Test():
  while not Jobs_queue.empty():

    Enqueue_TO_KID(Kid1_queue, Jobs_queue)
    Enqueue_TO_KID(Kid3_queue, Jobs_queue)
    Enqueue_TO_KID(Kid5_queue, Jobs_queue)

if __name__ == '__main__':
  
  print(Jobs)

  All_Enqueue(Jobs) # Making Jobs_queue
  print("ALL Jobs size is %d" % Jobs_queue.qsize())
  print("KID1 queue size is %d" % Kid1_queue.qsize())
  
  print("---------------------------------------------------")
 
  Test()

  print("KID1 queue size is %d" % Kid1_queue.qsize())
  print("KID3 queue size is %d" % Kid3_queue.qsize())
  print("KID5 queue size is %d" % Kid5_queue.qsize())
  
  global queue_monitor 
  print([Contents_confir(Kid1_queue), Contents_confir(Kid3_queue), Contents_confir(Kid5_queue)])
  print("KID1 queue size is %d" % Kid1_queue.qsize())
  print("KID3 queue size is %d" % Kid3_queue.qsize())
  print("KID5 queue size is %d" % Kid5_queue.qsize())

