import person
import numpy as np 

class RSA(object):
	def __init__(self, p, q):
		self.p = p
		self.q = q

	def gcd(self, x, y):
		while(y):
			x, y = y, x%y
		return x

	def test_prime(self):
		if self.gcd(self.p, self.q) == 1:
			return True
		else:
			return False
	
	def egcd(self, a, b):
		if a == 0:
			return (b, 0, 1)
		else:
			g, x, y = self.egcd(b % a, a)
			return (g, y - (b // a) * x, x)

	def calc_keys(self):
		modulus = self.p * self.q 
		totient = (self.p - 1) * (self.q - 1) 

		# check that gcd of exponent and totient is 1
		exponent = np.random.randint(3, 100000)
		while (self.gcd(exponent, totient) != 1):
			exponent = np.random.randint(3, 100000)
		
		assert exponent < modulus 

		# set the public key 
		pk = (exponent, modulus)

		# calculate the private key 
		ans = self.egcd(exponent, totient)
		d = int(ans[1] % totient)
		assert (d * exponent) % totient == 1
		sk = (d, modulus)

		return (pk, sk)

	def encrypt(self, msg, key):
		exponent, modulus = key 
		cipher_text = pow(int(msg), exponent, modulus)
		return cipher_text

	def decrypt(self, msg, key):
		d, modulus = key 
		plain_text = pow(msg, d, modulus)
		return plain_text
