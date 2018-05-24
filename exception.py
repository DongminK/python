try:
	a  = [1,2]
	print(a[3])
	4/0
except ZeroDivisionError as z:
	print("0으로 나눌수 없습니다. %s" % z)
except IndexError as i:
	print("인덱싱 할수 없습니다. %s" % i)


class Bird:
	def fly(self):
		raise NotImplementedError

class Eagle(Bird):
	def fly(self):
		print("very fast")

bird = Eagle()
bird.fly()

class MyError(Exception):

	def __str__(self):
		return "허용되지 않는 별명입니다."

def say_nick(nic):
	if nic == '바보':
		raise MyError()
	print(nic)


try:
	say_nick("천재")
	say_nick("바보")
except MyError as e:
	print("허용되지 않는 별명입니다. %s" % e)


a = [1, 2, 3]

try:
    result = a[-3]
    print(result)
except:
    print("error")
else:
    print("no error")


result = 3

try:
    result += 1
except:
    result += 2
else:
    result += 3
finally:
    result += 4

print(result)


result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
else:
    result += 4
finally:
    result += 5

print(result)



