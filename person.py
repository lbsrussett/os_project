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
		self.pk = (0,0)
		self.sk = (0,0)

	def set_keys(self):
		self.pk, self.sk = self.rsa.calc_keys()
		# print('Public Key for ' + self.name + ' = ' + pk)
		# print('Secret Key for ' + self.name + ' = ' + sk)
		

	def send_message(self, msg):
		cipher_text = self.rsa.encrypt(msg, self.pk)
		return cipher_text

	def receive_message(self, cipher_text):
		plain_text = self.rsa.decrypt(cipher_text, self. sk)
		return plain_text
