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

i=0
while True:
	i=i+1
	t_start=time.time()
	print(myBus.echo([1,2,3,4,i]))
	print('delay:', (time.time()-t_start)*1000,'ms')
	time.sleep(0.1)
	
myBus.close()
