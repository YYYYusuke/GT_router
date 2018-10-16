import pandas as pd 
import numpy as np
import psutil
import commands
import time
import os
from threading import Thread
from datetime import datetime
import re
"""
State_recorder.py is used for the purpose of tracking CPU ulilization, CPU temperature, and Fan rotation speed.
Dynamic load balancing is based on uptime and IPMItool command. However this script also gets internal server's state 
via Psutil command as well.
"""

class Record:
	def __init__(self):

		self.path_w='/nethome/ynakajo6/local_logs'

	def GetCPUtemp(self):
		cpu_temp=commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
		CPU_temp=cpu_temp.split(",")
		SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
		cpu_temp=SumOfCPUtemp/2
		
		with open(self.path_w + '/CPU_temp_test.csv', mode='a') as f:
			#f.write(str(datetime.now().microsecond) + ',' + str(cpu_temp) +'\n')
			f.write(str(time.time()) + ',' + str(cpu_temp) +'\n')
		return cpu_temp

	def GetSensors(self):
		core_temp=commands.getoutput("sensors | grep Core")
		tmp=re.split('[()]', core_temp)
		Hoge=[]
		for i in range(0, len(tmp)-1, 2):
			A=re.split('[+C]', tmp[i])
			Hoge.append(float(A[2]))
		cpu_temp=sum(Hoge)/len(Hoge)

		with open(self.path_w + '/CPU_temp_sensorstest.csv', mode='a') as f:
			#f.write(str(datetime.now().microsecond) + ',' + str(cpu_temp) +'\n')
			f.write(str(time.time()) + ',' + str(cpu_temp) +'\n')
		return cpu_temp
	

	def GetFanRotation(self):
		fan_rotation=commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
		Fan_rotation=fan_rotation.split(",")
		SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
		fan_speed=SumOfFan/2

		with open(self.path_w + '/FANtest.csv', mode='a') as f:
			#f.write(str(datetime.now().microsecond) + ',' + str(fan_speed) +'\n')
			f.write(str(time.time()) + ',' + str(fan_speed) +'\n')
		return fan_speed

	def GetCPUutil(self):
		uptime=commands.getoutput("uptime")
		Load_avg=uptime.split(":")
		LoadAvg=Load_avg[-1].split(",")
		cpu_util=float(LoadAvg[0])

		with open(self.path_w + '/CPU_util_test.csv', mode='a') as f:
			#f.write(str(datetime.now().microsecond) + ',' + str(cpu_util) +'\n')
			f.write(str(time.time()) + ',' + str(cpu_util) +'\n')
		return cpu_util

	def GetPSutil(self):
		PS=psutil.cpu_percent(interval=1)

		with open(self.path_w + '/PStest.csv', mode='a') as f:
			#f.write(str(datetime.now().microsecond) + ',' + str(PS) +'\n')
			f.write(str(time.time()) + ',' + str(PS) +'\n')
		return PS

	def GetCPUtempLoop(self, is_continued):
		while is_continued:
			self.GetCPUtemp()

	def GetFanLoop(self, is_continued):
		while is_continued:
			self.GetFanRotation()

	def GetCPUutilLoop(self, is_continued):
		while is_continued:
			self.GetCPUutil()

	def GetPSLoop(self, is_continued):
		while is_continued:
			self.GetPSutil()

	def GetSensorsLoop(self, is_continued):
		while is_continued:
			self.GetSensors()

