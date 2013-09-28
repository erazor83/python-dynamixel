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

	def write_data(self,dynamixel_id,register,data):
		self._socket.send(msgpack.packb([common.DYNAMIXEL_RQ_WRITE_DATA,dynamixel_id,register,len(data)]+data))
		return msgpack.unpackb(self._socket.recv())

	def reg_write(self,dynamixel_id,register,data):
		self._socket.send(msgpack.packb([common.DYNAMIXEL_RQ_REG_WRITE,dynamixel_id,register,len(data)]+data))
		return msgpack.unpackb(self._socket.recv())

	def reg_action(self,dynamixel_id):
		self._socket.send(msgpack.packb([common.DYNAMIXEL_RQ_REG_ACTION,dynamixel_id]))
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

	def pypose_load_poses(self,poses):
		for pose_id in poses:
			#set pose-size
			self._socket.send(msgpack.packb(
				[common.PYPOSE_SET_POSESIZE,common.PYPOSE_ID,len(poses[pose_id])]
			))
			ret=msgpack.unpackb(self._socket.recv())
			print(ret)
			#set pose
			pose_data=[]
			for item in poses[pose_id]:
				pose_data.append(item&0xff)
				pose_data.append((item>>8)&0xff)
				
			self._socket.send(msgpack.packb(
				[common.PYPOSE_LOAD_POSE,common.PYPOSE_ID,pose_id]+pose_data
			))
			ret=msgpack.unpackb(self._socket.recv())
			print(ret)
			
	def pypose_load_sequence(self,seq_data):
		idx=0
		data=[]
		for item in seq_data:
			idx=idx+1
			data.append(item&0xff)
			if (idx%2)==0:
				data.append((item>>8)&0xff)
				
		self._socket.send(msgpack.packb(
			[common.PYPOSE_LOAD_SEQUENCE,common.PYPOSE_ID]+data
		))
		ret=msgpack.unpackb(self._socket.recv())
		return ret
		
	def pypose_play_sequence(self,loop=False):
		if loop:
			self._socket.send(msgpack.packb(
				[common.PYPOSE_LOOP_SEQUENCE,common.PYPOSE_ID]
			))
		else:
			self._socket.send(msgpack.packb(
				[common.PYPOSE_PLAY_SEQUENCE,common.PYPOSE_ID]
			))
		ret=msgpack.unpackb(self._socket.recv())
		print(ret)
		
			