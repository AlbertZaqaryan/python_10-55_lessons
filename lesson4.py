# -------------- if, elif, else ---------------
# x = int(input('Enter number: '))

# if x >= 4:
#     print('> 4 ic')

# if x >= 4: # True
#     print('mec e 4 ic')
# else:
#     print('poqr e 4 ic')

# -------------------------------------------------

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a > b:
#     print('a is max')
# elif a == b:
#     print('Equal')
# else:
#     print('b is max')

# -------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# if a > b:
#     print('a is max')
# elif a == b:
#     print('Equal')
# else:
#     print('b is max')

# if x > y:
#     print('x is max')
# elif x == y:
#     print('Equal')
# else:
#     print('y is max')


# ----------------------------------
# text = input('Enter text: ')
# if 'a' in text:
#     print('Կա')
# else:
#     print('Չկա')
# ----------------------------------
# '5'
# 'a'
# 5 - int

# x = input('Enter let: ')
# if x.isdigit():
#     print('Number')
# elif x.isalpha():
#     print('Letter')
# else:
#     print('Char')
# ----------------------------------
# dzaynavorner = 'aeiou'
# tar = input('Mutqagreq tar: ')
# if tar in dzaynavorner:
#     print('Dzaynavor')
# else:   
#     print('Baxadzayn')
# ----------------------------------
# import random


# user_points = 0
# pc_points = 0
# pc = random.randint(0, 5)
# user = int(input('Enter number in range(0, 5):  '))
# # ##################### round1 #######################
# if user == pc: # user = 1, pc = 0
#     user_points += 1
#     print(f'---> Win user <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#     # ##################### round2 #######################
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0, 5):  '))
#     if user == pc: # user = 2, pc = 0 END GAME WIN USER
#         user_points += 1
#         print(f'---> Win user <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         print('############# WIN USER END GAME #################')
#     else: # user = 1, pc = 1
#         pc_points += 1
#         print(f'---> Win pc <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         # ##################### round3 #######################
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # user = 2, pc = 1 END GAME WIN USER
#             user_points += 1
#             print(f'---> Win user <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('############# WIN USER END GAME #################')
#         else: # user = 1, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---> Win pc <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('############# WIN PC END GAME #################')
# # ##################### round1 #######################
# else: # user = 0, pc = 1
#     pc_points += 1
#     print(f'---> Win pc <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#     # ##################### round2 #######################
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0, 5):  '))
#     if user == pc: # user = 1, pc = 1
#         user_points += 1
#         print(f'---> Win user <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         # ##################### round3 #######################
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # user = 2, pc = 1 END GAME WIN USER
#             user_points += 1
#             print(f'---> Win user <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('############# WIN USER END GAME #################')
#         else: # user = 1, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---> Win pc <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('############# WIN PC END GAME #################')
#     else: # user = 0, pc = 2 END GAME WIN PC
#         pc_points += 1
#         print(f'---> Win pc <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         print('############# WIN PC END GAME #################')
# ----------------------------------
# dog_age = int(input('Enter dog age: '))
# if dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# else:
#     print(f'Human age = {21 + (dog_age - 2) * 4}')
# ----------------------------------
# year = int(input('Enter year: '))
# if year % 4 == 0:
#     print('Leep year')
# else:
#     print('No Leep year')
# ----------------------------------
# number = int(input('Enter number: '))
# if number % 2 == 0:
#     print('Even number')
# else:
#     print('Odd number')
# ----------------------------------
# import random


# pc_followers = random.randint(1000, 1000000)
# user_followers = int(input('Enter user followers: '))
# if user_followers + user_followers * 20 / 100 > pc_followers:
#     print('User is Blogger')
# elif pc_followers + pc_followers * 20 / 1000 > user_followers:
#     print('Pc is Blogger')
# else:
#     print('Sergo is Blogger')
# ----------------------------------
# s = 12000
# t_pc = 180
# t_user = t_pc + t_pc * 10 / 100
# v_user = s / t_user
# print(round(v_user, 2), '(m/s)')
# ----------------------------------
# import random

# pc = random.choice(('Rock', 'Paper', 'Scissors'))
# user = input('Enter choice (Rock or Paper or Scissors): ')
# if user == 'Rock' and pc == 'Scissors' or user == 'Paper' and pc == 'Rock' or user == 'Scissors' and pc == 'Paper':
#     print('Win user')
#     print(f'pc -> {pc}')
# elif pc == 'Rock' and user == 'Scissors' or pc == 'Paper' and user == 'Rock' or pc == 'Scissors' and user == 'Paper':
#     print('Win pc')
#     print(f'pc -> {pc}')
# else:
#     print('Equal')
#     print(f'pc -> {pc}')
# ----------------------------------
# number = int(input('Enter 4 numbers: '))
# print(f'{number % 10}{number // 10 % 10}{number // 100 % 10}{number // 1000}')

# number = int(input('Enter 4 numbers: '))
# print(str(number)[::-1])
# '1234' '4321'
# ----------------------------------
