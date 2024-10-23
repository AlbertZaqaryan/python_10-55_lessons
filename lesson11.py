# list1=[]
# while len(list1) < 4:
#     number=int(input('Enter numbers:   '))
#     list1.append(number)  
# list1.remove(min(list1)) 
# list1.remove(max(list1)) 
# print(list1)


# list1=[]
# while True:
#     word = input('Enter text:   ')
#     if word == '':
#         break
#     else:
#         if word not in list1:
#             list1.append(word)
# print(list1)

# for number in range(1, 10001):
#     mylist = []
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             mylist.append(i)
#     if sum(mylist) == number:
#         print(number)


# mylist = [1, 2, 3, 4]
# x = [1, 3]
# newlist = [[]]
# for i in range(1, len(mylist) + 1):
#     for j in range(i):
#         newlist.append(mylist[j:i])
# newlist.sort(key=len)
# if x in newlist:
#     print(True)
# else:
#     print(False)

# import math

# print(math.log2(8000000000))


# dict_ = {
#     'a':1,
#     'b':2,
#     'c':3
# }

# print(dict_['b'])
# print(dict_.values())
# print(dict_.keys())
# print(dict_)
# print(dict_.items())

# data = [
#     ('a', 1),
#     ('c', 10),
#     ('b', -5)
# ]
# print(dict(data))

# dict_ = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }
# dict_['a'] = 22
# dict_['o'] = 77
# print(dict_)

# print(dict_['e'])
# print(dict_.get('a', 'Չկա'))
# mykeys = sorted(dict_)
# newdict = {}
# for i in mykeys:
#     newdict[i] = dict_[i]
# print(newdict)


# dict_ = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }
# my_keys = sorted(dict_, key=dict_.get)
# newdict = {}
# for i in my_keys:
#     newdict[i] = dict_[i]
# print(newdict)

# dict_ = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get)})

# dict_ = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }
# dict_.popitem()
# print(dict_)
# dict_.pop('a')

# del dict_['a']
# print(dict_)


# dict_ = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }
# dict_.setdefault('e', 11)
# dict_['e'] = 11
# print(dict_)

# dict_1 = {
#     'a':5,
#     'c':0,
#     'b':-3,
# }

# dict_2 = {
#     'e':5,
#     'u':0,
#     'o':-3,
# }
# dict_1.update(dict_2)
# print(dict_1)

# dict_1.clear()
# print(dict_1)


# dict_1 = {
#     'a':5,
#     'c':0,
#     'b':0,
# }
# print('a' in dict_1)
# for i in dict_1:
#     print(i, dict_1[i])

# import random

# print(random.randrange(1, 50, 6))


# students = {
#     'Ando':2,
#     'Tigran':7,
#     'Boris':8,
#     'Sergo':1,
#     'Alik':9,
#     'Margo':5,
#     'Mushegh':4,
#     'Suren':6,
#     'Alfred':7,
#     'Yuri':3
# }
# summ = 0
# for i in students:
#     summ += students[i]
# mean_score = summ / len(students)

# good_students = []
# bad_students = []

# for i in students:
#     if students[i] >= mean_score:
#         good_students.append(i)
#     else:
#         bad_students.append(i)
# print(f'Good students = {good_students}\nBad students = {bad_students}')

# s = 'a,2,b,5,c,8,a,4,e,11'
# {'a':6, 'b':5, 'c':8, 'e':11}

# erudit = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10:"QZ",
# }
# text = input('Enter text: ').upper()
# summ = 0
# for i in text:
#     for j in erudit:
#         if i in erudit[j]:
#             summ += j
# print(summ)

# text = 'Sergo likes kentron girls'
# print({i:text.count(i) for i in text if i != ' '})
# mydict = {}
# for i in text:
#     if i in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# print(mydict)

# bar1 = input('Mutq bar1: ').lower()
# bar2 = input('Mutq bar2: ').lower()
# print({i:bar1.count(i) for i in bar1} == {i:bar2.count(i) for i in bar2})

