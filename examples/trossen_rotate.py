#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

URI='tcp://10.254.0.171:5555'
sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

import python_dynamixel.zmq_bus as zmq_bus
import python_dynamixel.common as common

class myBusClass(zmq_bus.Bus,zmq_bus.Trossen_Commands):
	pass

myBus=myBusClass()

myBus.open(URI)


time.sleep(1)
rc=myBus.cmd(right_V=127,right_H=100,left_V=127,left_H=127,buttons=0)
time.sleep(2)
rc=myBus.cmd(right_V=127,right_H=148,left_V=127,left_H=127,buttons=0)
time.sleep(2)
rc=myBus.cmd(right_V=127,right_H=127,left_V=127,left_H=127,buttons=0)

myBus.close()
