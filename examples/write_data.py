#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

URI='tcp://10.254.2.2:5555'
sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

import python_dynamixel.zmq_bus as zmq_bus
import python_dynamixel.common as common

myBus=zmq_bus.Bus()

myBus.open(URI)

positions=[400,500,600,500]

while True:
	for pos in positions:
		rc=myBus.write_data(
			1,
			common.DYNAMIXEL_R_GOAL_POSITION_L,
			[pos&0xff,(pos>>8)&0xff]
		)
		print(rc)
		time.sleep(2)
myBus.close()
