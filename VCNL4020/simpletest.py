#!/usr/bin/env python3
import time
import threading
from  VCNL4020 import  VCNL4020

term = False
sensor = VCNL4020()

def prox():
	global term
	
	while term == False:
		if sensor.proximity > 4000:
			print('センサーに何かが接近しています')
		time.sleep(0.1)
	

t = threading.Thread(target=prox)
t.start()

try:
	while True:
		print('明るさ: ' + str(sensor.luminance) +' lux')
		time.sleep(0.1)
except KeyboardInterrupt:
	term = True


