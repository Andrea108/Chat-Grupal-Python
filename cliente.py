import socket
import threading
import sys
import pickle

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host="localhost", port=3000):

		self.sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #variable que almacenara el socket
		self.sockt.connect((str(host), int(port))) #conexion socket

		msg_recibido = threading.Thread(target=self.msg_recibido)
		msg_recibido.daemon = True
		msg_recibido.start()

		while True:
			msg = input('->')
			if msg != 'salir':
				self.msg_enviar(msg) #se envia el msj
			else:
				self.sockt.close() #se cierra la conexion
				sys.exit()


	def msg_recibido (self):
		while True:
			try:
				data = self.sockt.recv(1024) #si el socket recibe un msj
				if data:
					print(pickle.loads(data))
			except:
				pass


	def msg_enviar(self, msg):
		self.sockt.send(pickle.dumps(msg)) #le dice al socket que enviara un msj

c = Cliente() #inicializar el cliente

    		    


		