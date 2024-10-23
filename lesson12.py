# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(dict_, key=dict_.get, reverse=True)[:3]
# newdict = {}
# for i in keys:
#     newdict[i] = dict_[i]
# print(newdict)
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get, reverse=True)[:3]})
# ----------------------------------------------------------------------
# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')
# newdict = {}
# for i in range(0, len(s), 2):
#     if s[i] in newdict:
#         newdict[s[i]] += int(s[i + 1])
#     else:
#         newdict[s[i]] = int(s[i + 1])
# print(newdict)
# ----------------------------------------------------------------------
# word = input('Enter word: ')
# print({i:word.count(i) for i in word})
# ----------------------------------------------------------------------
# import random

# numbers = {
#     2:0,
#     3:0,
#     4:0,
#     5:0,
#     6:0,
#     7:0,
#     8:0,
#     9:0,
#     10:0,
#     11:0,
#     12:0,
# }

# for i in range(1000):
#     zar1 = random.randint(1, 6) # 3
#     zar2 = random.randint(1, 6) # 4
#     numbers[zar1 + zar2] += 1
# for i in numbers:
#     print(i, numbers[i] / 10, "%")
# ----------------------------------------------------------------------
# phone = {
#     '1': '.,?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' ',
# }
# word = input('Enter word:  ').upper() # HELLO
# for i in word:
#     for j in phone:
#         if i in phone[j]:
#             print(j * (phone[j].index(i) + 1), end='')

# ----------------------------------------------------------------------
# MORSE_CODE_DICT = { 
#     'A':'.-', 'B':'-...',
#     'C':'-.-.', 'D':'-..', 'E':'.',
#     'F':'..-.', 'G':'--.', 'H':'....',
#     'I':'..', 'J':'.---', 'K':'-.-',
#     'L':'.-..', 'M':'--', 'N':'-.',
#     'O':'---', 'P':'.--.', 'Q':'--.-',
#     'R':'.-.', 'S':'...', 'T':'-',
#     'U':'..-', 'V':'...-', 'W':'.--',
#     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#     '1':'.----', '2':'..---', '3':'...--',
#     '4':'....-', '5':'.....', '6':'-....',
#     '7':'--...', '8':'---..', '9':'----.',
#     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#     '?':'..--..', '/':'-..-.', '-':'-....-',
#     '(':'-.--.', ')':'-.--.-'
#     }
# text = input('Enter text: ').upper().replace(' ', '')
# for i in text:
#     print(MORSE_CODE_DICT[i], end='')
# ----------------------------------------------------------------------
# text = 'Hello, World!'
# text_dict = {i:0 for i in text}
# print(len(text_dict))
# ----------------------------------------------------------------------
mylist = ['flower', 'flow', 'flight']
mylist.sort(key=len)
# ['flow', 'flower', 'flight']
index = 1
while index < len(mylist):
    if mylist[0] == mylist[index][:len(mylist[0])]:
        index += 1
    else:
        mylist[0] = mylist[0][:-1]
print(mylist[0])
# ----------------------------------------------------------------------
