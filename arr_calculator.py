class Calculator:

	def __init__(self, init_values):
		self.value = init_values

	def sum(self):
		total = 0
		for val in self.value:
			total += val

		return total

	def avg(self):
		total = self.sum()
		size = len(self.value)

		if size == 0:
			return 0

		return total / size


cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())  # 15 출력
print(cal1.avg())  # 3.0 출력

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())  # 40 출력
print(cal2.avg())  # 8.0 출력