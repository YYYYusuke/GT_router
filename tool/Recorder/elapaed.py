
import time


if __name__ == '__main__':
	start = time.time()
	for i in range(0,11):
		print 'a'
	elapsed_time = time.time() - start
	print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
