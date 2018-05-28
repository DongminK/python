## 1.이름분석
'''
names = ["이의덕", "이재명", "권종수", "이재수", "박철호", "강동희", "이재수", "김지석", "최승만", "이성만", "박영희", "박수호", "전경식", "송우환", "김재식", "이유정"]

kim_count = 0
park_count = 0
leejs_count = 0

no_dup = {}

for name in names:
	if name.startswith("김"):
		kim_count += 1
	if name.startswith("박"):
		park_count += 1
	if name == "이재수":
		leejs_count += 1

	no_dup[name] = name

print("김씨와 박씨는 각각 몇몇인가? 김:%d 박:%d" % (kim_count, park_count))
print("이재수란 이름이 몇번 반복되나? %d" % (leejs_count))
print("중복을 제거한 이름을 출력하시오")  ## 확인필요
print(no_dup.keys())
print("중복을 제거한 이름을 오름차순으로 정렬하여 출력하시오")

sort_list = list(no_dup.keys())
sort_list.sort()
print(sort_list)
'''

## 2. 합의 제곱과 제곱의 합의 차
'''
sum_pow = 0
pow_sum = 0
last_idx = 100

for i in range(1, last_idx + 1):
	pow_sum += i ** 2
	sum_pow += i

sum_pow = sum_pow ** 2

print("제곱의 합 : %d" % (pow_sum))
print("합의 제곱 : %d" % (sum_pow))
print("합의 제곱과 제곱의 합의 차이 : %d" % (sum_pow - pow_sum))
'''

## 3. 1부터 100까지의 각 숫자의 갯수 구하기
'''
start = 1
end = 100
str_cnt = {}

for i in range(start, end + 1):
	str_num = str(i)
	str_len = len(str_num)

	for p_str in range(0, str_len):
		cnt = str_cnt.get(str_num[p_str])

		if cnt == None:
			str_cnt[str_num[p_str]] = 1
		else:
			str_cnt[str_num[p_str]] = cnt + 1

print(str_cnt)

'''


## 4. DashInsert
'''
sign = {0: "*", 1: "-"}

value = 4546793
str_value = str(value)

translate = ""
prev_sign = -1
for str_val in str_value:

	curr_sign = int(str_val) % 2

	if prev_sign == -1:
		translate = str_val
	else:
		if prev_sign == curr_sign:
			translate = translate + sign[curr_sign] + str_val
		else:
			translate = translate + str_val

	prev_sign = curr_sign

print("입력 : %d" % value)
print("출력 : %s" % translate)

'''

## 5. 문자열 압축하기

'''
value = "aaabbcccccca"
prev_value = ""
complete_value = ""
count = 0

for val in value:
	if prev_value == "":
		prev_value = val
		count = 1
	else:
		if prev_value == val:
			count += 1
		else:
			complete_value = complete_value + prev_value + str(count)
			prev_value = val
			count = 1

complete_value = complete_value + prev_value + str(count)


print("입력 : %s" % value)
print("출력 : %s" % complete_value)
'''


## 6. Duplicate Numbers
'''
def checkDuplicate(value):
	dup = {}
	is_finish = False

	for val in value:
		cnt = dup.get(val)

		if cnt == None:
			dup[val] = 1
		else:
			dup[val] = cnt + 1

	for num in range(0, 10):

		cnt = dup.get(str(num))

		if cnt == None or dup[str(num)] != 1:
			print("False")
			is_finish = True
			break

	if not is_finish:
		print("True")

checkDuplicate("0123456789")
checkDuplicate("01234")
checkDuplicate("01234567890")
checkDuplicate("6789012345")
checkDuplicate("012322456789")

'''

## 7. 모스 부호 해독
'''
mos = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J",
       "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U",
       "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"}

mos_codes = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
ch = ""
decode_code = ""

for code in mos_codes:

	if code != " ":
		ch = ch + code
	elif ch == "":
		decode_code = decode_code + " "
	else:
		decode_code = decode_code + mos[ch]
		ch = ""

if len(ch) > 0:
	decode_code = decode_code + mos[ch]

print(decode_code)

'''


### 8. 정규식1
