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

	def test_prime(self, x, y):
		return True

	def calc_congruence(self, e):
		x = e
		return x

	def calc_keys(self):
		pk = (,)
		sk = (,)

		return {pk, sk}

	def encrypt(self, message):
		msg = message
		return msg

	def decrypt(self, message):
		msg = message
		return msg
