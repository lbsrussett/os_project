import rsa

#create_person
#set_keys
#create_message
#send_message
#receive_message


class Person:

	def __init__(self, name, p, q):
		self.name = name
		self.rsa = rsa.RSA(p, q)

	def set_keys(self):
		keys = self.rsa.calc_keys()
		print('Public Key for ' + self.name + ' = ' + str(keys[0]))
		print('Secret Key for ' + self.name + ' = ' + str(keys[1]))
		

	def create_message(self):
		msg = ''
		return msg

	def send_message(self):
		msg = self.create_message('Test')
		self.rsa.encrypt(msg)


	def receive_message(self, msg):
		self.rsa.decrypt(msg)