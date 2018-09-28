from Queue import Queue

# For static round robin balancing

Jobs =[1,2,2,3,4,4,15,12,21,16,12,12,15,18,19,24]
Jobs_queue = Queue()
Kid1_queue = Queue()
Kid3_queue = Queue()
Kid5_queue = Queue()

class RR:
    
    def SayHello(self):
            print("Hi I am RR!!")
    
    def All_Enqueue(self, Jobs):
        for i in Jobs:
            global Jobs_queue
            Jobs_queue.put(i)
            #print("Enqueue:%d" %i)
        #print("All Jobs size is %d" % Jobs_queue.qsize())
        #print("KID1 queue size is %d" % Kid1_queue.qsize())
        return Jobs_queue

    def Enqueue(self, KID_queue, q):
      if q.empty():
        print("Empty")
      else:
        KID_queue=q.get()
        return(KID_queue)

    def Enqueue_TO_KID1(self, q):
      if q.empty():
        print("Empty")
      else:
        global Kid1_queue
        tmp=q.get()
        Kid1_queue.put(tmp)
        return(Kid1_queue)

    def Enqueue_TO_KID3(self, q):
      if q.empty():
        print("Empty")
      else:
        global Kid3_queue
        tmp=q.get()
        Kid3_queue.put(tmp)
        return(Kid3_queue)

    def Enqueue_TO_KID5(self, q):
      if q.empty():
        print("Empty")
      else:
        global Kid5_queue
        tmp=q.get()
        Kid5_queue.put(tmp)
        return(Kid5_queue)


    def Dequeue(self, q):
      if q.empty():
        #break
        print("Empty")
      else:
        i = q.get()
        print("Dequeue:%d" %i)
      return i

    def rr(self):
      while not Jobs_queue.empty():
        
        Enqueue_TO_KID1(Jobs_queue)
        Enqueue_TO_KID3(Jobs_queue)
        Enqueue_TO_KID5(Jobs_queue)
      
      print("Done round robing")
      print("KID1 queue size is %d" % Kid1_queue.qsize())

      """
        Enqueue(Kid1_queue, Jobs_queue)
        Enqueue(Kid2_queue, Jobs_queue)
        Enqueue(Kid3_queue, Jobs_queue)
      """
