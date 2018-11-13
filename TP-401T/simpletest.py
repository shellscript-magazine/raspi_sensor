#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

from TP401T import TP401T

sensor = TP401T()

try:
	sensor.start()
	print('待機中です')
	while sensor.state == TP401T.WAITING:	# 測定開始待ち
		time.sleep(3)
	
	while True:
		if sensor.state == TP401T.NORMAL:
			print('空気は正常です')
		else:
			print('汚染されています!!')
		
		time.sleep(3)
		
except KeyboardInterrupt:
	sensor.stop()	# センサー停止
