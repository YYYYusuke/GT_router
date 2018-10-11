import pandas as pd 
import numpy as np
import psutil
import commands
import time
import os
from datetime import datetime

"""
State_recorder.py is used for the purpose of tracking CPU ulilization, CPU temperature, and Fan rotation speed.
Dynamic load balancing is based on uptime and IPMItool command. However this script also gets internal server's state 
via Psutil command as well.
"""

path_w = os.getcwd()

def GetCPUtemp():
	cpu_temp=commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
	CPU_temp=cpu_temp.split(",")
	SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
	cpu_temp=SumOfCPUtemp/2
	
	with open(path_w + '/CPU_temp_test.csv', mode='a') as f:
		f.write(str(cpu_temp) +'\n')

	return cpu_temp

def GetFanRotation():
	fan_rotation=commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
	Fan_rotation=fan_rotation.split(",")
	SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
	fan_speed=SumOfFan/2

	with open(path_w + '/FANtest.csv', mode='a') as f:
		f.write(str(fan_speed) +'\n')

	return fan_speed

def GetCPUutil():
	uptime=commands.getoutput("uptime")
	Load_avg=uptime.split(":")
	LoadAvg=Load_avg[-1].split(",")
	cpu_util=float(LoadAvg[0])

	with open(path_w + '/CPU_util_test.csv', mode='a') as f:
		f.write(str(cpu_util) +'\n')

	return cpu_util

def GetPSutil():
	PS=psutil.cpu_percent(interval=1)

	with open(path_w + '/PStest.csv', mode='a') as f:
		f.write(str(PS) +'\n')

	return PS


if __name__ == '__main__':
	print("Start recording server's state")
	
	for i in range(2):
	
		print(datetime.now().second)
		
	"""
	#print("CPU temperature:", GetCPUtemp())
	for i in range(3):
		GetCPUtemp()
		GetFanRotation()
		GetPSutil()
		GetCPUutil()
	"""
