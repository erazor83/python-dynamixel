import msgpack
import zmq

import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import common

class Bus():
	"""
		Bus-Access via ZeroMQ using dynamixel_zmq
		TODO: add timeouts
	"""
	
	_zmqctx=None
	_socket=None
	
	def open(self,uri="tcp://127.0.0.1:5000"):
		self._zmqctx = zmq.Context()
		self._socket = self._zmqctx.socket(zmq.REQ)
		self._socket.connect(uri)
	
	def close(self):
		self._socket.close()
	
	def ping(self,dynamixel_id):
		self._socket.send(msgpack.packb([common.DYNAMIXEL_RQ_PING,dynamixel_id]))
		return msgpack.unpackb(self._socket.recv())
	
	def echo(self,data):
		self._socket.send(msgpack.packb([common.DYNAMIXEL_RQ_ZMQ_ECHO]+data))
		return msgpack.unpackb(self._socket.recv())
	
	def sync_write(self,reg_start,id_count,p_count,data):
		self._socket.send(msgpack.packb(
			[common.DYNAMIXEL_RQ_SYNC_WRITE,reg_start,id_count,p_count]+data
		))
		return msgpack.unpackb(self._socket.recv())

	def sync_write_words(self,reg_start,id_count,w_count,data):
		self._socket.send(msgpack.packb(
			[common.DYNAMIXEL_RQ_SYNC_WRITE_WORDS,reg_start,id_count,w_count]+data
		))
		return msgpack.unpackb(self._socket.recv())
		
	def read_data(self,dynamixel_id,reg_start,p_count):
		self._socket.send(msgpack.packb(
			[common.DYNAMIXEL_RQ_READ_DATA,dynamixel_id,reg_start,p_count]
		))
		return msgpack.unpackb(self._socket.recv())
