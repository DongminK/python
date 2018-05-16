class Calculator:

	def __init__(self):
		self.value = 0

	def add(self, add):
		self.value += add

class UpgradeCalculator(Calculator):

	def minus(self, minus):
		self.value -= minus


class MaxLimitCalculator(Calculator):

	def add(self, add):
		self.value += add
		if self.value > 100:
			self.value = 100

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


maxCal = MaxLimitCalculator()
maxCal.add(50)
maxCal.add(60)

print(maxCal.value)