import rsa
import person
import sys

class Cryptosystem:



	if __name__ == '__main__':

		p1 = person.Person('Alice',373,709)
		p2 = person.Person('Bob',307, 653)

		p1.set_keys()
		p2.set_keys()

		encrypted_message = p1.send_message('This is a test message.\n')
		print(encrypted_message)

		decrypted_message = p2.receive_message(encrypted_message)
		print(decrypted_message)