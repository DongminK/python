class Data:

	def __init__(self, text):
		split_text = text.split("|")
		self.name = split_text[0]
		self.age = split_text[1]
		self.grade = split_text[2]

	def print_age(self):
		print(self.age)

	def print_grade(self):
		print("%s 님의 점수는 %s 입니다" % (self.name, self.grade))


data = Data("김동민|36|A+")
data.print_age()
data.print_grade()

