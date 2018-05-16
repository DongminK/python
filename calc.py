class FourCal:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def setdata(self, a, b):
		self.a = a
		self.b = b

	def sum(self):
		return self.a + self.b

	def mul(self):
		return self.a * self.b

	def sub(self):
		return self.a - self.b

	def div(self):
		return self.a / self.b

class MoreFourCal(FourCal):

	def pow(self):
		return self.a ** self.b

class SafeFourCal(MoreFourCal):

	def div(self):
		if self.b == 0:
			return 0

		return self.a / self.b

a = SafeFourCal(4, 0)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())
