import msgpack
import zmq

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
		self._socket.send(msgpack.packb([1, 2, 3]))
		return msgpack.unpackb(self._socket.recv())
