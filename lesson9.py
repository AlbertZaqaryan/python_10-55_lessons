# ---------------------------------------------
# factor = 2
# n = int(input('Enter n: '))
# while factor <= n:
#     if n % factor == 0:
#         print(factor)
#         n = int(n / factor)
#     else:
#         factor += 1
# ---------------------------------------------
# bin_code = input('Enter binary code: ')
# bin_code = bin_code[::-1]
# summ = 0
# for i in range(0, len(bin_code)):
#     if bin_code[i] in '01':
#         summ += int(bin_code[i]) * 2 ** i
#     else:
#         print('Wrong input')
#         break
# print(summ)
# ---------------------------------------------
# x = (1, 2, 3)
# y = [1, 2, 3]
# print(type(x))
# print(type(y))
# print(x.__sizeof__())
# print(y.__sizeof__())

# -----------------------------------------------
# list1 = list()
# list2 = []
# print(list1)
# print(list2)

# x = 110
# tuple_ = (x, '1', '4', 7, True)


# list_ = [7, 8, -10, 6, 9]
# list_.sort(reverse=True)
# print(list_)

# list_ = ['b', 'd', 'a']
# list_.sort()
# print(list_)

# list_ = ['barev', 'Hello', 'py', 'Python', 'php']
# list_.sort()
# list_.sort(key=len, reverse=True)
# print(list_)

# list_ = ['a', 'b', 'c']
# list_.append('o')
# print(list_)

# list_ = ['a', 'b', 'c']
# list_.insert(1, 'o')
# print(list_)

# list_ = ['a', 'b', 'c']
# list_.remove('b')
# list_.pop(1)
# del list_[1:]
# print(list_)

# list1 = ['a', 'b', 'c']
# list2 = list1.copy()
# list2.append('k')
# print(list1)

# a = 10
# b = a
# b += 5
# print(a)


# list1 = ['a', 'b', 'c']
# print(list1.index('b'))
# print(list1.count('b'))


# list1 = ['a', 'b', 'c']
# list1.clear()
# print(list1)

# list1 = ['a', 'b', 'c']
# list2 = ['k', 'f']
# list3 = list1 + list2
# print(list3)
# list1.extend(list2)
# print(list1)

# text = 'python'
# print(list(text))

# text = 'p y t h o n'
# text = text.split(' ')
# print(text)


# mylist = ['b', 'a', 'r']
# text = '$'.join(mylist)
# print(text)

# mylist = [1, 2, 3, 4]
# print([i ** 2 for i in mylist])
# newlist = []
# for i in mylist:
#     newlist.append(i ** 2)
# print(newlist)

# l = [None]
# print(10 * l)

# mylist = [7, 4, 8, 5, 6, 9, 7, 1, 2, 3]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

# mylist = [7, 4, 8, 5, 6, 9, 7, 1, 2, 3]
# print([i for i in mylist if i % 2 == 0])

# mylist = [7, 4, 8, 5, 6, 9, 7, 1, 2, 3]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append('EVEN')
#     else:
#         newlist.append('ODD')
# print(newlist)

# mylist = [7, 4, 8, 5, 6, 9, 7, 1, 2, 3]
# print(['EVEN' if i % 2 == 0 else 'ODD' for i in mylist])

# mylist = ['barev', 'Ando', 'jan']
# max_len = 0
# max_word = ''
# for i in mylist:
#     if len(i) > max_len:
#         max_len = len(i)
#         max_word = i
# print(max_word)

# mylist.sort(key=len)
# print(mylist[-1])

# mylist = [7, 7, 7, 7, 7, 4, 4, 4, 5, 7, 7, 7, 7, 1, 2, 3, 5, 5, 5, 5, 6, 6, 6]
# mylist = [7, 4, 5, 1, 2, 3, 6]
# for
# if
# count
# remove
# copy
# for i in mylist.copy():
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# mylist.sort()
# print(mylist)


# users = ['Ando', 'Karen', 'Hayk', 'Sahak', 'Boris']
# 'Hayk' - 'Sahak'
# 'Ando' - 'Boris'
# 'Karen' - 'Hayk'
# 'Sahak' - 'Ando'
# 'Boris' - 'Karen'


# text = 'barev=python'
# text = text.split('=')
# text = text.partition('=')
# print(list(text))

# x = (10, )
# print(x)

# list1 = []
# list2 = []
# list3 = []
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         print(list1 + list2 + list3)
#         break
#     else:
#         number = int(number)
#         if number < 0:
#             list1.append(number)
#         elif number == 0:
#             list2.append(number)
#         else:
#             list3.append(number)