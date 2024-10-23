# ----------------------------------------------------
# pi = 3
# a, b, c = 2, 3, 4
# for i in range(0, 15):
#     pi += 4 / (a * b * c) * (-1) ** i
#     a, b, c = a + 2, b + 2, c + 2
# print(pi)
# ----------------------------------------------------
# text = input('Enter text:  ')
# n = 15
# for i in text:
#     if i == 'X':
#         print('A', end='')
#     elif i == 'Y':
#         print('B', end='')
#     elif i == 'Z':
#         print('C', end='')
#     else:
#         print(chr(ord(i) + n), end='')
# ----------------------------------------------------
# text = input('Enter text:  ')
# print(text == text[::-1])

# text = 'flee to me remote elf'
# text = text.replace(' ', '')
# print(text == text[::-1])


# x = int(input("Enter boys count: ")) # 6
# y = int(input("Enter girls count: ")) # 3
# if y < x/2:
#     print("xndiry lucum chuni")
# else:
#     for i in range(0, (max(x,y)+1)):
#         if x > 0:
#             x-=1
#             print ("B", end = '')
#         if y > 0:    
#             y-=1
#             print("G", end = '')
#         if x > 0:    
#             x-=1
#             print ("B", end = '')
# print(x,y)


# a = int(input("mutqagrel qarakusu koxmy: " )) 
# S1 = 144 
# S2 = a**2
# if S2 > S1:
#     print("namaky chi texavorvum crari mej anhrajesht e calel ")

# for i in range(0,8):   
#     S2 = (1/(2**i))*a**2
#     print(S2)
#     if S2 <= S1:
#         print("namaky texavorvel e crari mej")
#         print(f"namaky calvel e {i} angam")
#         break

# s = 1
# a = 2
# n = int(input('Enter n: '))
# for i in range(0, n):
#     s -= (1 / a) * (-1) ** i
#     a *= 2
# print(s)

# -------------------------------------------------
# b = int(input('b:  '))
# g = int(input('g:  '))
# s = ''
# if b > 2 * g:
#     print('ERROR')
# elif g == b:
#     for i in range(g):
#         s += 'BG'
# else:
#     for i in range(g):
#         s += 'BG'
#     n = b - g
#     temp = ''
#     s_copy = s
#     for i in range(n):
#         index_ = s_copy.index('G')
#         temp += s[:index_ + 1]
#         temp += 'B'
#         s_copy = s_copy[index_ + 1:]
#     s = temp + s_copy
# print(s)
# -------------------------------------------------
# i = 0
# while i < 6:
#     print(i)
#     i += 1


# n = int(input('Enter n: ')) # 50
# count = 0
# while n > 12:
#     n = n / 2 # 6.25
#     count = count + 2
# print(count)


# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         continue


# summ = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         number = int(number)
#         summ += number
# print(summ)


# number = int(input('Enter decimal number: '))
# s = ''
# while number > 1:
#     s += str(number % 2)
#     number //= 2
# print('1' + s[::-1])


# text1 = 'abc'
# text2 = '123'
# for i in text1: # i = ''
#     for j in text2: # j = '1', j = '2', j = '3'
#         print(i + j, end=' ')
#     print('$')

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>4}', end='')
#     print()


# n = int(input('Enter n:  '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()


# n = 7
# for i in range(n + 1):
#     print('i', end=' ')
#     for j in range(n + 1):
#         print('j', end=' ')
#     print()