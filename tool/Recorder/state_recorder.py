import pandas as pd 
import numpy as np
import psutil
import commands
import time
import os
from threading import Thread
from datetime import datetime

"""
State_recorder.py is used for the purpose of tracking CPU ulilization, CPU temperature, and Fan rotation speed.
Dynamic load balancing is based on uptime and IPMItool command. However this script also gets internal server's state 
via Psutil command as well.
"""

#path_w = os.getcwd()
path_w = '/nethome/ynakajo6/GT_router/tool/Recorder'
is_continued = True


def GetCPUtemp():
	cpu_temp=commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
	CPU_temp=cpu_temp.split(",")
	SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
	cpu_temp=SumOfCPUtemp/2
	
	with open(path_w + '/CPU_temp_test.csv', mode='a') as f:
		#f.write(str(datetime.now().microsecond) + ',' + str(cpu_temp) +'\n')
		f.write(str(time.time()) + ',' + str(cpu_temp) +'\n')

	return cpu_temp

def GetFanRotation():
	fan_rotation=commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
	Fan_rotation=fan_rotation.split(",")
	SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
	fan_speed=SumOfFan/2

	with open(path_w + '/FANtest.csv', mode='a') as f:
		#f.write(str(datetime.now().microsecond) + ',' + str(fan_speed) +'\n')
		f.write(str(time.time()) + ',' + str(fan_speed) +'\n')

	return fan_speed

def GetCPUutil():
	uptime=commands.getoutput("uptime")
	Load_avg=uptime.split(":")
	LoadAvg=Load_avg[-1].split(",")
	cpu_util=float(LoadAvg[0])

	with open(path_w + '/CPU_util_test.csv', mode='a') as f:
		#f.write(str(datetime.now().microsecond) + ',' + str(cpu_util) +'\n')
		f.write(str(time.time()) + ',' + str(cpu_util) +'\n')
	return cpu_util

def GetPSutil():
	PS=psutil.cpu_percent(interval=1)

	with open(path_w + '/PStest.csv', mode='a') as f:
		#f.write(str(datetime.now().microsecond) + ',' + str(PS) +'\n')
		f.write(str(time.time()) + ',' + str(PS) +'\n')

	return PS

def RecordingLoop():
	while is_continued:
		GetCPUtemp()
		GetFanRotation()
		GetPSutil()
		GetCPUutil()

if __name__ == '__main__':
	print("Start recording server's state")
	try:
		os.remove(path_w+"/PStest.csv")
	except:
		print("PStest is already deleted")
	try:
		os.remove(path_w+"/CPU_util_test.csv")
	except:
		print("CPU_util is already deleted")
	try:
		os.remove(path_w+"/FANtest.csv")
	except:
		print("FAN is already deleted")
	try:
		os.remove(path_w+"/CPU_temp_test.csv")
	except:
		print("CPU_Temp is already deleted")
	thread = Thread(target=RecordingLoop)
	thread.start()
	time.sleep(10)
	is_continued = False
	print("Done recording server's state")
