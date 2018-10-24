from multiprocessing import Pool
import multiprocessing as multi 
import time
import sys 
import psutil
import threading 
from mypool import MyPool

class Process:
	def __init(self):
	    pass

	def SayHello(self):
	    print("Hello from process class!!")

	def process(self, i):
	    return [{'id' : j, 'sum': sum(range(i*j))} for j in range(500)]
	
	def f(self, x):
	    return x*x

	def usemulti(self, required_cores, job_intensity):
	    s=time.time()
	    p=MyPool(multi.cpu_count() if required_cores < 0 else required_cores)
	    result=p.map(self.process, range(job_intensity))
	    #p.close()
	    print("Processing with "+ str(required_cores) +" cores is Done")
	    elapsed=time.time() -s
	    print('time: {0} [sec]'.format(elapsed))
	    return elapsed
