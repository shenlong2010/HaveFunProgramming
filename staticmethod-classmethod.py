class A:
	@staticmethod
	def sample(self):
		print("static method")

	@classmethod
	def sample(self):
		print("class method")

A.sample()