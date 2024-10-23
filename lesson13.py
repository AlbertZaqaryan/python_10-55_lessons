# text = input('Enter text:  ')
# dict_ = {i:None for i in text}
# print(dict_)

# text1 = 'William Shakespeare'.replace(' ', '').lower()
# text2 = 'I ama weakish speller'.replace(' ', '').lower()
# dict1 = {i:text1.count(i) for i in text1}
# dict2 = {i:text2.count(i) for i in text2}
# print(dict1 == dict2)
# ------------------------------------------------------------
# import msvcrt
# import random
# import os


# animal = '🦛'
# food = '🍉'

# size1 = 20
# size2 = 20
# animal_i = random.randint(0, size1 - 1)
# animal_j = random.randint(0, size2 - 1)
# food_i = random.randint(0, size1 - 1)
# food_j = random.randint(0, size2 - 1)
# wrong_i = random.randint(0, size1 - 1)
# wrong_j = random.randint(0, size2 - 1)
# wrong_animal_i = random.randint(0, size1 - 1)
# wrong_animal_j = random.randint(0, size1 - 1)
# wrong_animal = '🐍'
# wrong = '🌵'
# game_points = ''
# h = '♥♥♥'
# while True:
#     for i in range(0, size1):
#         for j in range(0, size2):
#             if i == animal_i and j == animal_j:
#                 print(animal, end=' ')
#             elif i == food_i and j == food_j:
#                 print(food, end=' ')
#             elif i == wrong_i and j == wrong_j:
#                 print(wrong, end=' ')
#             elif i == wrong_animal_i and j == wrong_animal_j:
#                 print(wrong_animal, end=' ')
#             else:
#                 print(' .', end=' ')
#         print()
#     input_ = msvcrt.getwch()
#     if input_ == 'w':
#         animal_i -=1
#     elif input_ == 's':
#         animal_i += 1
#     elif input_ == 'd':
#         animal_j += 1
#     elif input_ == 'a':
#         animal_j -= 1
#     else:
#         break
#     random_step = random.choice('wasd')
#     if random_step == 'w':
#         wrong_animal_i -= 1
#     elif random_step == 's':
#         wrong_animal_i += 1
#     elif random_step == 'd':
#         wrong_animal_j += 1
#     elif random_step == 'a':
#         wrong_animal_j -= 1
#     if animal_i == size1:
#         animal_i -= size1
#     elif animal_i == -1:
#         animal_i += size1
#     elif animal_j == size2:
#         animal_j -= size2
#     elif animal_j == -1:
#         animal_j += size2
#     if animal_i == food_i and animal_j == food_j:
#         game_points += food
#         food_i = random.randint(0, size1 - 1)
#         food_j = random.randint(0, size2 - 1)
#         size1 -= 1
#         size2 -= 1
#     if animal_i == wrong_i and animal_j == wrong_j:
#         game_points = game_points[:-1]
#         wrong_i = random.randint(0, size1 - 1)
#         wrong_j = random.randint(0, size2 - 1)
#     if animal_i == wrong_animal_i and animal_j == wrong_animal_j:
#         h = h[:-1]
#     if h == '':
#         print('GAME OVER')
#         break
#     os.system('cls')
#     print(f'Your points = {game_points}\n{h}')
# ------------------------------------------------------------
# x = set()
# print(type(x))
# ------------------------------------------------------------
# x = {'a':1}
# y = {1, 2}
# print(type(x))
# print(type(y))
# ------------------------------------------------------------
# set1 = {1, 2, 3, 1, 1, 2, 3, 5, 6}
# print(set1)
# set1 = {1, 2, 3}
# set2 = {7, 6, 2}
# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.isdisjoint(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# ------------------------------------------------------------
# set1 = {7, 4, 5, 6, 16, 1, 2}
# set1.add(8)
# set1.discard(16)
# print(set1)
# ------------------------------------------------------------
