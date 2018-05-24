import sys

total = 0
length = len(sys.argv)

for arg in range(1, length):
	total += arg

print(total)