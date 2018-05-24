import calendar
import glob
import os
import random
import webbrowser

# webbrowser.open("http://www.naver.com")
import shutil

import time

import sys
from collections import namedtuple

print(os.environ)

os.system("dir")

# shutil.copy(src, dst)

print(glob.glob("C:\IN-SOFT\*"))

print(time.time())

print(time.localtime(time.time()))

print(time.localtime(time.time()).tm_year)

print(time.asctime(time.localtime(time.time())))

print(time.ctime())

print(calendar.calendar(2015))

###################################

total = 0
length = len(sys.argv)

for arg in range(1, length):
	total += arg

print(total)

###################################

os.chdir("D:\Study\python")
var = os.system("dir")
print(var)

###################################

print(glob.glob("D:/Study/python/*.py"))

###################################

print(time.strftime("%x",time.localtime(time.time())))

###################################

data = []

for i in range(1, 46):
	data.append(i)

print(data)

for i in range(6):
	var = random.choice(data)
	data.remove(var)
	print(var)

###################################

Student = namedtuple("Student", {"name", "score"})

a = Student("홍길동", 30)

print(a)
print(a.name)
print(a.score)

