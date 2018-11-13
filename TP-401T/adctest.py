#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from MCP3424 import MCP3424

adc = MCP3424()

try:
	while True:
		print( 'ch0 voltage:' + str(adc.ch0) )
		print( 'ch1 voltage:' + str(adc.ch1) )
		print( 'ch2 voltage:' + str(adc.ch2) )
		print( 'ch3 voltage:' + str(adc.ch3) )
		time.sleep(1)
except KeyboardInterrupt:
	pass

