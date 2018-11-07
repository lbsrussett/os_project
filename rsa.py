import person
#encrypt function
#decrypt function
#gcd
#test_prime
#calc_congruence

class RSA:
	# key_length = 3

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

	def calc_congruence(self, e):
		x = e
		return x

	def calc_keys(self):
		modulus = self.p * self.q 
		totient = (self.p - 1) * (self.q - 1) 
		exponent = 65537

		# check that gcd of exponent and totient is 1
		while (self.gcd(exponent, totient) != 1):
			exponent += 1

		# set the public key 
		pk = (exponent, modulus)

		# calculate the private key 
		d = 1
		while(self.gcd(exponent*d, totient) != 1):
			d += 1

		sk = (d, modulus)

		return (pk, sk)

	def encrypt(self, message, key):
		msg = message

		# convert to ascii 
		msg = ''.join(str(ord(c)) for c in msg)
		msg = int(msg)
		exponent, modulus = key 
		cipher_text = msg ** exponent % modulus 
		return cipher_text

	def decrypt(self, message, key):
		msg = message
		d, modulus = key 
		plain_text = msg ** d % modulus 
		plain_text = [plain_text[i:i+3] for i in range(0, len(plain_text), 3)]
		plain_text = [chr(i) for i in plain_text]
		return msg
