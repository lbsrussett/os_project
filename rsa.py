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
		if self.test_prime():
			pk = (3,self.p)
			sk = (1,self.q)
		else:
			return 'There was an error'

		return [pk, sk]

	def encrypt(self, message):
		msg = message
		return msg

	def decrypt(self, message):
		msg = message
		return msg
