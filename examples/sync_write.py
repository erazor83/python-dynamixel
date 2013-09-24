#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

URI='tcp://10.254.2.2:5555'
sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

import python_dynamixel.zmq_bus as zmq_bus
import python_dynamixel.common as common

myBus=zmq_bus.Bus()

myBus.open(URI)

rc=myBus.sync_write(
	common.DYNAMIXEL_R_GOAL_POSITION_L,
	2,
	4,
	[1,0x00,0x02,0x64,0x00]+
	[2,0x00,0x02,0x64,0x00]
)
print(rc)
myBus.close()
