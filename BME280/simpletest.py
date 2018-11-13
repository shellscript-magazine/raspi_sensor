#!/usr/bin/env python3
#
# apt install python3-pip
# sudo pip3 install RPi.BME280
#

import time
import smbus2
import bme280

from EbOled import EbOled

BME280_ADDR = 0x76
BUS_NO = 1

# BME280
i2c = smbus2.SMBus(BUS_NO)
bme280.load_calibration_params(i2c, BME280_ADDR)

try:
	while True:
		now = time.localtime()
		print(str(now.tm_hour)+'時'+str(now.tm_min)+'分'+str(now.tm_sec)+'秒')
		data = bme280.sample(i2c, BME280_ADDR)
		print('気温 :' + str(round(data.temperature,1)) + '度')
		print('湿度 :' + str(round(data.humidity,1)) + '％')
		print('気圧 :' + str(round(data.pressure,1)) + 'hPa')
		time.sleep(1)
except KeyboardInterrupt:
	pass
