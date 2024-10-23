# odd_count = 0
# even_count = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f'Even count -> {even_count}\nOdd count -> {odd_count}')
# ----------------------------------------------------------------

# n1, n2 = 0, 1
# for i in range(40):
#     print(n1)
#     n1, n2 = n2, n1 + n2
# ----------------------------------------------------------------
# text = input('Enter text: ')
# digit_count = 0
# letter_count = 0
# char_count = 0
# for i in text:
#     if i.isdigit():
#         digit_count += 1
#     elif i.isalpha():
#         letter_count += 1
#     else:
#         char_count += 1
# print(f'In {text}\n{digit_count}(digits), {letter_count}(letters) and {char_count}(chars)')
# ----------------------------------------------------------------
# number = int(input('Enter number: '))
# summ = 0
# for i in str(number):
#     summ += int(i)
# print(summ)
# ----------------------------------------------------------------
# count = 0
# for _ in range(10):
#     number = int(input('Enter number:  '))
#     if number >= 0 and number % 2 == 0:
#         count += 1
# print(count)
# ----------------------------------------------------------------
# summ = 0
# for i in range(1, 13):
#     salary = float(input(f'Enter {i} year salary: '))
#     summ += salary
# print(summ / 12)

# ----------------------------------------------------------------
# n = int(input('Students count: '))
# count_3 = 0
# count_4 = 0
# count_5 = 0
# for i in range(n):
#     point = int(input('ENter 3 or 4 or 5: '))
#     if point == 3:
#         count_3 += 1
#     elif point == 4:
#         count_4 += 1
#     elif point == 5:
#         count_5 += 1

# if count_3 > count_4 > count_5:
#     print('Max 3 min 5')
# elif count_4 > count_3 > count_5:
#     print('Max 4 min 5')
# elif count_5 > count_3 > count_4:
#     print('Max 5 min 4')
# elif count_3 > count_5 > count_4:
#     print('Max 3 min 4')
# ----------------------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# count = 0
# summ = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         summ += i
#         count += 1
# print(summ / count)
# ----------------------------------------------------------------
# 15 % 10 = 5
# 15 // 10 = 1
# 1 * 5 * 3 = 15

# 24
# 2 * 4 * 3 = 24
# for i in range(10, 100):
#     if (i % 10) * (i // 10) * 3 == i:
#         print(i)
# ----------------------------------------------------------------
# n = 5
# 1 + 2 + 3 + 4 + 5 = 15

# 2 + 1 +  4  + 5 = 12

# n = int(input('Enter number: '))
# full_sum = 0
# for i in range(1, n + 1):
#     full_sum += i
# summ = 0
# for i in range(1, n):
#     qart = int(input('Enter cart number: '))
#     summ += qart
# print(full_sum - summ)
# ----------------------------------------------------------------
# text = "programming"

# l = len(text)
# for i in range(0, 2*l-1):
#     if i < l:
#         print(text[:i+1]) 
#     elif  i >=l:
#         print(text[:(2*l-1)-i])

# text = input('Enter text:  ')
# for i in range(1, len(text) + 1):
#     print(text[:i])
# for i in range(len(text) - 1, 0, -1):
#     print(text[:i])
# ----------------------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# summ = 0
# count = 0
# for i in range(a, b + 1):
#     if i % c == 0:
#         summ += i
#         count += 1
# print(summ / count)
# ----------------------------------------------------------------
# n = int(input('N: '))
# summ = 0
# for i in range(0, n + 1, 5):
#     price = int(input(f'No -> {i} enter price: '))
#     summ += price
# print(summ)


# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# for x in range(a, b + 1):
#     print(x ** 3 + 2 * x ** 2 - 4 * x + 1)

# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# "BAREV"
# "EDU"
# ord(68)
# chr('a')
# index
# []
# for
# if
# range


# n = int(input('Enter n: '))
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         print('Bazadryal')
#         break
# else:
#     print('Parz')

