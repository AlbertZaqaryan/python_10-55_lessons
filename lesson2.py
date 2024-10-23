# --------------------------------------
# x = 10
# y = 3
# x + y
# print(x - 3)
# --------------------------------------
# qart = 0
# amis1 = qart + 150
# amis2 = amis1 + 150
# print(amis2)
# --------------------------------------
# qart = 0
# qart = qart + 150
# qart = qart + 150
# print(qart)
# --------------------------------------
# qart = 0
# qart += 150
# qart -= 5
# qart *= 3
# qart /= 10
# qart //= 3
# qart %= 2
# qart **= 5
# print(qart)
# --------------------------------------
# ------------------------ string methods ----------------------------
# text = 'python programming'
# print(text[-1])
# print(len(text))

# slice
# [start:stop:step]
# print(text[1:4])
# print(text[:4])
# print(text[3:])
# print(text[3:len(text)])
# print(text[2:10:2])
# print(text[-1:-4:-1])
# print(text[-4:-1])
# print(text[5:2:-1])
# print(text[-1:5:-1])
# print(text[5:-2])
# print(text[1:])
# print(text[::-1])
# --------------------------------------

# text = 'python programming'

# --------------------------------------

# x = 5 # int
# print(x.isdigit()) # ERROR
# --------------------------------------

# x = '5' # digit
# x = 'a' # alpha
# --------------------------------------

# x = 'a'
# print(x.isdigit())
# --------------------------------------

# x = 'b'
# print(x.isalpha())
# --------------------------------------

# text = 'python312'
# print(text.isdigit())
# print(text.isalpha())
# print(text.isalnum())
# --------------------------------------

# text = 'BAREV'
# text = 'anun azganun'
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# --------------------------------------
# text = input('Enter text: ')
# print(text.isupper())
# print(text.islower())
# --------------------------------------
# text = 'p y t h o n'
# text = text.replace(' ', '')
# print(text)
# --------------------------------------
# text = 'p y t h o n'
# print(text.count(' '))
# print(text.index('t'))
# --------------------------------------
# --------------------- ASCII --------------------------
# text = 'p'
# print(ord(text))

# text1 = 'Hello'
# text2 = 'Harev'
# print(text1 < text2)

# print(5 & 6)
# print(5 | 6)
# print(5 ^ 6)

# print(5 > 4 and 10 <= 3)
#      1 and 0 = 0

# print(5 > 4 or 10 <= 3)
#      True or False = True

# letter = 'p'
# print('p' not in 'python')
# print('tpy' in 'python')

# x = 5
# y = 5
# print(x is not y)

# print(5 is 5)

# x = int(5)
# x = 5

# text = 'barevbarevbarev'
# print(text * 3)
# print(text + " Sergo")

# ---------------- exercises ---------------------
# --------- ex 1 ------------
# celsus = float(input('Enter celsus value: '))
# print(f'Far = {celsus * 9/5 + 32}(F)')
# print('Far = ', celsus * 9/5 + 32,'(F)')
# --------------------------------------
# --------- ex 2 ------------
# far = float(input('Enter far value:  '))
# print(f'Celsus = {5 * (far - 32) / 9}(C)')
# --------------------------------------
# --------- ex 3 ------------
# min_ = float(input('Enter minutes: '))
# sec_ = min_ * 60
# print(f'Second = {min_ * 60}')
# print('Second =', min_ * 60)
# --------------------------------------
# --------- ex 4 ------------
# day = int(input('Enter day: '))
# h = day * 24
# m = h * 60
# s = m * 60
# print(f'{day}(day) = {h}(h) or {m}(m) or {s}(s)')
# --------------------------------------
# --------- ex 5 ------------
# angle1 = int(input('Enter angle1:  '))
# angle2 = int(input('Enter angle2:  '))
# print(angle1 + angle2 <= 90)
# --------------------------------------
# --------- ex 6 ------------
# angle1 = int(input('Enter angle1: '))
# angle2 = int(input('Enter angle2: '))
# print(f'angle3 = {180 - angle1 - angle2}')
# --------------------------------------
# --------- ex 7 ------------
# number = int(input('Enter number: '))
# print(number >= 100)
# --------------------------------------
# --------- ex 8 ------------
# number = int(input('Enter number: '))
# print(number % 400 == 0)
# --------------------------------------
# --------- ex 9 ------------
# r = int(input('Enter circle radius:  '))
# print(f'S = {5 * 2 * 3.14 * r}')
# --------------- book exercises -------------------
#  N 33
# number1 = int(input('Enter number1: '))
# number2 = int(input('Enter number2: '))
# number3 = int(input('Enter number3: '))
# min_number = min(number1, number2, number3)
# max_number = max(number1, number2, number3)
# sum_numbers = number1 + number2 + number3
# mean_number = sum_numbers - max_number - min_number
# print(min_number, mean_number, max_number)
# --------------------------------------

#  N 32
# number = 4892
# number4 = number % 10
# number3 = number // 10 % 10
# number2 = number // 100 % 10
# number1 = number // 1000
# print(number4 + number3 + number2 + number1)

# number = 4892
# number4 = number % 10
# number //= 10 
# number3 = number % 10
# number //= 10 
# number2 = number % 10
# number //= 10 
# number1 = number % 10

# number = 4892
# number = str(number)
# print(int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]))
# --------------------------------------
# a = 5
# b = 7
# # b = a + b # 12
# a = a + b # 12
# b = a - b # 5
# a = a - b # 7
# a, b = b, a
# print(a, b)
# --------------------------------------
# x = int(input('Enter x: '))
# print(5 - x)
# --------------------------------------