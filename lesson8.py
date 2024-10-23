# n = int(input("Mutqagrel Piramidai erkarutyuny: "))
# for i in range(0, n):
#     for j in range(0, 2*n):
#         if j >= (n-1) - i and j <= (n-1) +i:
#             print("#", end='')
#         else:
#             print(' ', end='')    
#     print()


# n = int(input("Mutqagrel Piramidai erkarutyuny: "))
# a=1
# for i in range(0, n):
#     for j in range(0, 2*n):
#         if j >= (n-1) - i and j <= (n-1) +i and i % 2 == j % 2:
#             print(f'{a:>2}', end= ' ')
#             a+=2
#         else:
#             print(' ', end=' ')    
#     print()


# n = int(input('Enter n:  '))

# for i in range(0,n):
#     for j in range(0,2*n):
#         if j > i and j <= ((2*n)-2) - i:
#             print(".", end= '')
#         else:
#             if j >= n:
#                 print(j -n+1, end='')
#             else:
#                 print(n-j, end='')

#     print() 


# ---------------------------------------------
# for i in range(6):
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>3}', end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter number: '))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter n: '))
# for i in range(0, n + 1):
#     for j in range(0, n + 1):
#         if j == 0 or i == 0 and j == n or j == n:
#             print('|', end=' ')
#         elif i == 0 or i == n:
#             print('-', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter n: '))
# for i in range(n):
#     for j in range(2 * n):
#         if j <= i:
#             print(n - j, end='')
#         elif j >= 2 * n - 1 - i:
#             print(j - n + 1, end='')
#         else:
#             print('.',end='')
#     print()


# count = int(input('Enter numbers: '))
# prime_counts = 0
# for _ in range(count):
#     number = int(input('Enter number: '))
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             break
#     else:
#         prime_counts += 1
# print(prime_counts)


# n = int(input('Enter n: '))
# summ = 0
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     summ += fact
# print(summ)


# n = int(input('Enter count: '))
# max_sum = 0 # 18
# max_number = 0 # 99
# print('------------------------------------------------------')
# for _ in range(n):
#     number = int(input('Enter number: ')) # 99
#     summ = 0 # 18
#     for i in str(number):
#         summ += int(i)
#     if summ > max_sum: # 18 > 8
#         max_sum = summ
#         max_number = number
# print(max_number)
    

# import random

# max_number = random.randint(1, 100)
# print(max_number)
# for i in range(99):
#     number = random.randint(1, 100)
#     if number > max_number:
#         print(number, 'Update')
#         max_number = number
#     else:
#         print(number)

# kassa = 0
# while True:
#     age = input('Enter age: ')
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 3 > age > 0:
#             continue
#         elif 12 > age >= 3:
#             kassa += 14
#         elif 65 > age >= 12:
#             kassa += 18
#         else:
#             kassa += 23
# print(kassa)

import random

# s = ''
# while True:
#     s += random.choice('OP')
#     if len(s) >= 3 and s[-1] == s[-2] == s[-3]:
#         print(s)
#         break

# for _ in range(10):
#     count_O = 0
#     count_P = 0
#     while True:
#         char = random.choice('OP')
#         if count_O == 3 or count_P == 3:
#             break
#         if char == 'O':
#             count_O += 1
#             count_P = 0
#         else:
#             count_P += 1
#             count_O = 0
#         print(char, end='')
#     print()


if 0:
    print('Good')