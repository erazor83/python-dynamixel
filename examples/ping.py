#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

import python_dynamixel.zmq_bus
URI='tcp://10.254.2.2:5555'

myBus=python_dynamixel.zmq_bus.Bus()

myBus.open(URI)

while True:
	print(myBus.ping(1))
	#time.sleep(0.2)

myBus.close()
