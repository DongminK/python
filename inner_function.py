
for i, name in enumerate(["test", "kimdongmon", "insoft"]):
	print(i, name)


def positive(value):
	return value > 0

print(list(filter(positive, [23, 0, -1, 10])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

class Person:
	pass


a = Person()

print(isinstance(a, Person))


def two_times(x):
	return x*2


print(list(map(two_times, [1,2,3,4])))



print(list(map(lambda x: x + 1, [1,2,3,4])))

#open binary mode check


a = [1,5,34,56,5]
print(sorted(a))
print(a)
a.sort()
print(a)


print(all([1, 2, abs(-3)-3]))

print(chr(ord('a')) == 'a')

dic = {}
for i, name in enumerate(['a', 'b', 'c']):
	dic[i] = name

print(dic)


print(list(filter(lambda x: x> 0, [1, -2, 3, -5, 8, -3])))

print(int('0xea', 16))


print(list(map(lambda  x:x*3,  [1, 2, 3, 4] )))

val = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(val) + max(val))



print(round(17 / 3, 4))

print(list(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])))


