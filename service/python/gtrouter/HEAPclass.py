import heapq

class HEAP:

	def heapsort(self, iterable):
	    h=[]
	    for value in iterable:
	       heapq.heappush(h, value)
	    return [heapq.heappop(h) for i in range(len(h))]

	def heapsort_tupple(self, iterable):
	    h=[]
	    i=1
	    for value in iterable:
		heapq.heappush(h, [value, 'KID'+str(i)])
		i+=1
	    return [heapq.heappop(h) for i in range(len(h))]

	def heap_route(self, CPU_temp_state, CPU_cores):

		State=self.heapsort_tupple(CPU_temp_state)
		Cores=self.heapsort(CPU_cores)
		ReCores=[]

		for j in (reversed(Cores)):
		    ReCores.append(j)
		
		print("State:", State)
		print("Cores:", ReCores)
		
		for k in range(len(State)):
		    State[k][0]=ReCores[k]
		
		New_state=sorted(State, key=lambda x:x[1])
		Queue=[New_state[m][0] for m in range(len(New_state))]

		return Queue
