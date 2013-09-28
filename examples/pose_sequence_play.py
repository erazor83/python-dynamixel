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


poses={
	0:[512,512],
	1:[700,700],
}
sequence=[0,2000,1,6000,0,2000]

rc=myBus.pypose_load_poses(poses)
print(rc)

rc=myBus.pypose_load_sequence(sequence)
print(rc)


rc=myBus.pypose_play_sequence(False)
print(rc)
myBus.close()
