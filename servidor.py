import socket
import threading
import sys
import pickle

class Servidor():
	"""docstring for Servidor"""
	def __init__(self,host="localhost",port=3000):
		self.clientes=[]
		self.sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockt.bind((str(host), int(port))) #se enlaza el socket
		self.sockt.listen(10) #max de instrucciones a escuchar 
		self.sockt.setblocking(False)

		aceptar = threading.Thread(target=self.aceptarCon)	#hilo para	aceptar conexiones
		procesar = threading.Thread(target=self.procesarCon)	#hilo para	procesar conexiones


		aceptar.daemon = True
		aceptar.start()	#se ponen a correr

		procesar.daemon = True
		procesar.start()

		while True:
			msg = input('->')
			if msg == 'salir':
				self.sockt.close()
				sys.exit()
			else:
				pass	


	def msg_a_todos(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente: #verifica que el cliente que se le envia el mensaje sea distinto de quien lo escribio
					c.send(msg)
			except:
				self.clientes.remove(c)


	def aceptarCon(self):
		print("aceptarCon iniciado")
		while True:
			try:
				con, dire = self.sockt.accept()
				con.setblocking(False) #que no se bloquee la conexion
				self.clientes.append(con)
			except:
				pass


	def procesarCon(self):
		print("ProcesarCon iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024) #verificamos que haya recibido un mensaje 
						if data:
							self.msg_a_todos(data,c) #envie el msj a todos
					except: 
						pass

s=Servidor()