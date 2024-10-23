# -------------------------------------------------------------
# my_list =["Hp", "Asus", "Dell", "Mac", "Lenovo"]
# print("Mac" in my_list)
# -------------------------------------------------------------
# while True:
#     char_count = 0
#     number_count = 0
#     password = input('Enter password: ')
#     if len(password) < 8:
#         print('Your password is not strong: ')
#     else:
#         if password[0].isupper():
#             for i in password:
#                 if i.isdigit():
#                     number_count += 1
#                 elif i.isalpha():
#                     continue
#                 else:
#                     char_count += 1
#         else:
#             print('Your password is not strong: ')
#     if char_count >= 2 and number_count >= 2:
#         print('Your password is strong')
#         break
# -------------------------------------------------------------
# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# print(link[link.index('=') + 1:])
# link = link.split('=')
# print(link[1])
# link = link.partition('=')
# print(link[2])

# for i in range(0, len(link)):
#     if link[i] == '=':
#         print(link[i + 1:])
#         break

# index = 0
# while True:
#     if link[index] == '=':
#         print(link[index + 1:])
#         break
#     else:
#         index += 1
# -------------------------------------------------------------
# text = input('Enter word: ')
# print(text == text[::-1])
# -------------------------------------------------------------
# text = 'python'
# print(list(text))
# -------------------------------------------------------------
# numbers = input('Enter 5 numbers:  ').split(' ')
# for i in numbers:
#     if int(i) % 2 == 0:
#         print(i)
# -------------------------------------------------------------
# mylist = [7, 8, 4, 5, 1, 2, 3, 6, 6, 5, 8, 9, 7, 7, 7, 7, 5, 1, 1, 2, 2, 2, 2]
# for i in mylist.copy():
#     if i % 2 == 0:
#         mylist.remove(i)
# print(mylist)
# -------------------------------------------------------------
# mylist = [7, 8, 4, 5, 1, 2, 3, 6, 6, 5, 8, 9, 7, 7, 7, 7, 5, 1, 1, 2, 2, 2, 2]
# for i in mylist.copy():
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# print(mylist)
# -------------------------------------------------------------
# import random

# users1 = ['Boris', 'Hayk', 'Sergo', 'Ando', 'Narek']
# users2 = ['Boris', 'Hayk', 'Sergo', 'Ando', 'Narek']
# final_result = []
# while len(final_result) < 5:
#     u1 = random.choice(users1)
#     u2 = random.choice(users2)
#     if len(users1) == 1 == len(users2) and users1 == users2:
#         users1 = ['Boris', 'Hayk', 'Sergo', 'Ando', 'Narek']
#         users2 = ['Boris', 'Hayk', 'Sergo', 'Ando', 'Narek']
#         final_result = []
#     if u1 != u2:
#         final_result.append(f'{u1} ----> {u2}')
#         users1.remove(u1)
#         users2.remove(u2)
#     else:
#         continue
# for i in final_result:
#     print(i)
# -------------------------------------------------------------
# mylist = [7, 4, 1, 2, -30, 6, 0, 15]
# for i in range(len(mylist)):
#     for j in range(len(mylist) - 1):
#         if mylist[j] > mylist[j + 1]:
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
# print(mylist)
# -------------------------------------------------------------
# import array

# x = array.array(1, 2, 3)

# print(x)


# x = [1, 2, 3, , , , , , , ,]

# mylist = [5, 7, 9, 10, 15, 19, 25, 34, 49, 50, 60, 78, 125, 136, 148, 170, 190, 200, 214, 226, 334, 569, 780, 1256]
# n = 569
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if mylist[mid] == n:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1
# ------------------------------------
# import random

# mast = ['♥', '♦', '♣', '♠']
# kart = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# xaxacoxner = ['Sergo', 'Ando', 'Rafo', 'Karo']
# kalod = [i + j for i in mast for j in kart]
# nor_kalod = []
# while kalod != []:
#     patahakan_kart = random.choice(kalod)
#     nor_kalod.append(patahakan_kart)
#     kalod.remove(patahakan_kart)
# for i in xaxacoxner:
#     print(i, nor_kalod[:8])
#     nor_kalod = nor_kalod[8:]

# ------------------------------------
# n = int(input('Enter number: '))
# mylist = []
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         mylist.append(i)
# print(mylist)
# ------------------------------------
# text = "Contr.actions include:!!! ?.don’t, isn’t, and wouldn’t."
# text = text.split(' ')
# newlist = []
# for i in text:
#     while True:
#         if i[0].isalpha() and i[-1].isalpha():
#             break
#         if not i[0].isalpha():
#             i = i[1:]
#         if not i[-1].isalpha():
#             i = i[:-1]
#     newlist.append(i)
# print(' '.join(newlist))
# ------------------------------------

