from Queue import Queue

# For static round robin balancing

Jobs_queue = Queue()
Kid_queue = Queue()

class RR:
    
    def SayHello(self):
            print("Hi I am RR!!")
    
    def All_Enqueue(self, Jobs):
        for i in Jobs:
            global Jobs_queue
            Jobs_queue.put(i)
        return Jobs_queue

    def Six_Enqueue(self, Jobs):
        Jobs_queue = Queue()
        for i in Jobs:
            Jobs_queue.put(i)
        return Jobs_queue


    def Enqueue(self, KID_queue, q):
      if q.empty():
        print("Empty")
      else:
        KID_queue=q.get()
        return(KID_queue)

    def Enqueue_TO_KID(self,Kid_queue, q):
      if q.empty():
        print("Empty")
      else:
        tmp=q.get()
        Kid_queue.put(tmp)
        return(Kid_queue)

    def Dequeue(self, q):
      if q.empty():
        #break
        print("Empty")
      else:
        i = q.get()
        #print("Dequeue:%d" %i)
      return i

    def rr(self):
      while not Jobs_queue.empty():
        
        Enqueue_TO_KID1(Jobs_queue)
        Enqueue_TO_KID3(Jobs_queue)
        Enqueue_TO_KID5(Jobs_queue)
      
      print("Done round robing")
      print("KID1 queue size is %d" % Kid1_queue.qsize())

