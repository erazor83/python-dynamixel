#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

import python_dynamixel.zmq_bus

myBus=python_dynamixel.zmq_bus.Bus()

myBus.open('tcp://localhost:5555')

print(myBus.echo([1,"asdsa",3,4]))

myBus.close()
