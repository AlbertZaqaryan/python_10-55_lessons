# -----------------------------------------------------------------
# xy = input("mutqagreq notan: ") 
# # #oktavanery C0-ic c8, notanery C0, D0, E0, F0, G0, A0, B0
# x = xy[0]
# y = int(xy[1:])

# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392.00
# A4 = 440.00
# B4 = 493.88

# n = 'nman oktava ev nota goyutyun chuni'

# if x == 'C'and y <=8:
#     n = C4 / 2 **(4 - y)
# elif x == 'D' and y <=7:
#     n = D4 / 2 **(4 - y)
# elif x == 'E' and y <=7:
#     n = E4 / 2 **(4 - y)
# elif x == 'F' and y <=7:
#     n = F4 / 2 **(4 - y)
# elif x == 'G'and y <=7:
#     n = G4 / 2 **(4 - y)
# elif x == 'A'and y <=7:
#     n = A4 / 2 **(4 - y)
# elif x == 'B'and y <=7:
#     n = B4 / 2 **(4 - y)
# print(n)
# -----------------------------------------------------------
# cord = input('Enter cord: ')
# let, number = cord[0], int(cord[1])
# if let in 'aceg' and number % 2 != 0 or let in 'bdfh' and number % 2 == 0:
#     print('Black')
# else:
#     print('White')
# -----------------------------------------------------------
# n = int(input('Enter n: '))
# if n == 3:
#     print('Erankyun')
# elif n == 4:
#     print('Qarankyun')
# -----------------------------------------------------------
# iterable

# x = 'barev'
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])


# (1, 2, 3)
# [3, 5, 6]
# {}


# x = 785
# print(x[0])


# range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(3, 10)
# [3, 4, 5, 6, 7, 8, 9]


# range(-10, -3)
# [-10, -9, -8, -7, -6, -5, -4]


# range(-3, -10, -1)
# [-3, -4, -5, -6, -7, -8, -9]

# range(5, 1, -1)
# [5, 4, 3, 2]


# range(start, stop, step)
# [start, + step -> stop)
# ---------------------------------------


# for num in range(-5, 15):
#     print(num)

# ---------------------------------------

# start = int(input('Enter start range: '))
# stop = int(input('Enter stop range: '))
# for i in range(start, stop):
#     print(i)

# ---------------------------------------

# break
# continue
# pass
# ---------------------------------------

# for i in range(1, 100):
#     if i > 5:
#         break
#     else:
#         print(i)

# ---------------------------------------

# for i in range(1, 10):
#     if i == 5:
#         continue
#         print(i)
#     else:
#         print(i)

# ---------------------------------------

# for i in range(1, 10):
#     if i == 5:
#         pass
#     else:
#         print(i)

# ---------------------------------------

# for i in range(1, 10):
#     if i == 6:
#         print('Gta banalin')
#         break
# else:
#     print('Chka')
# ---------------------------------------
# count = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         count += 1
# print(count)
# ---------------------------------------
# text = 'Sergo like fubol'
# for i in text:
#     if i == ' ':
#         continue
#     else:
#         print(i)
# ---------------------------------------
# text = 'Sergo like fubol'
# count = 0
# for i in text:
#     if i == 'o':
#         count += 1
# print(count)
# ---------------------------------------

# text = 'python'
# 'py'
# 'yt'
# 'th'
# 'ho'
# 'on'
# print(text[0] + text[1])
# print(text[1] + text[2])
# print(text[2] + text[3])
# print(text[3] + text[4])
# print(text[4] + text[5])
# ---------------------------------------

# text = 'python'
# for i in range(len(text) - 3): # i = 1 text[1] <=> text[1 + 1]
#     print(text[i] + text[i + 1] + text[i + 2] + text[i + 3]) 
# ---------------------------------------
# a = 965412
# b = 125478
# for i in range(965412 ,a * b + 1):
#     if i % 125478 == 0 and i % 965412 == 0:
#         print(i)
#         break
# ---------------------------------------
# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))
# if a > b:
#     for i in range(a, a * b + 1, a):
#         if i % b == 0:
#             print(i)
#             break
# elif a < b:
#     for i in range(b, a * b + 1, b):
#         if i % a == 0:
#             print(i)
#             break
# else:
#     print(a)
# ---------------------------------------
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz-Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
# ---------------------------------------
# for i in range(1, 101, 10):
#     print(f'{i}(C) = {i * 9/5 + 32}(F)')
# ---------------------------------------
# for c in range(1, 101, 10):
#     print(c, c * 9/5 + 32)
# ---------------------------------------
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# ---------------------------------------
# n = int(input('Enter number: '))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)
# ---------------------------------------
# text = input('Enter text: ')
# 'p'
# 'py'
# 'pyt'
# 'pyth'
# 'pytho'
# 'python'
# 'pytho'
# 'pyth'
# 'pyt'
# 'py'
# 'p'

# 'j'
# 'ja'
# 'jav'
# 'java'
# 'jav'
# 'ja'
# 'j'
# ---------------------------------------
