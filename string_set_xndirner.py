# x1 = '((())[][])'
# y1 = [')']
# def fun(x):
#     y = []
#     while len(x):
#         try:
#             i = x[0]
#             if i == '(':
#                 y.append(')')
#             elif i == ')':
#                 y.pop(y.index(')'))
#             elif i == '[':
#                 y.append(']')
#             elif i == ']':
#                 y.pop(y.index(']'))
#             elif i == '{':
#                 y.append('}')
#             elif i == '}':
#                 y.pop(y.index('}'))
#         except ValueError:
#             return False
#         x = x[1:]
#     if not len(y):
#         return True
#     else:
#         return False
# print(fun(x1))





# def fun(x):
#
#     if len(x) == 0:
#         return print('no')
#
#     sum_kruglie = 0
#     sum_kvadrat = 0
#     sum_figur = 0
#
#     j = 0
#     while j < len(x):
#
#         i = j+1
#         if i == '(':
#             sum_kruglie += 1
#         elif i == ')':
#             sum_kruglie -= 1
#             if sum_kruglie == 0:
#
#
#             # x = '((())[{}]())'
#             # x = '((()))[{}]'
#             if sum_figur == sum_kvadrat == 0:
#                 sum_kruglie -= 1
#             else:
#                 return False
#
#         elif i == '[':
#             sum_kvadrat += 1
#         elif i == ']':
#             # x = '((()))[{}]'
#             # x = '((())[{}])'
#             if sum_figur == sum_kruglie == 0:
#                 sum_kvadrat -= 1
#             else:
#                 return False
#
#
#         elif i == '{':
#             sum_figur += 1
#         elif i == '}':
#             # x = '((()))[{}]'
#             # x = '((())[{}])'
#             if sum_kruglie == sum_kvadrat == 0:
#                 sum_figur -= 1
#             else:
#                 return False
#
#         if sum_figur < 0 or sum_kvadrat < 0 or sum_kruglie < 0:
#             return False
#
#     if sum_figur == sum_kruglie == sum_kvadrat == 0:
#         return True
#     else:
#         return False
#
#
# x1 = '((())[{}])'
# # print(fun(x1))
#





# d = {'(': '123', ')': '321', '[': '456', ']': '654', '{': '789', '}': '987'}
#
# print(d['('] == d[')'][::-1])
#
# y = ''
# for i in x:
#     y += d[i]
# print(y)
#
#
# # x = '((()))[{}]'
# x = '((())[{}])'
#
# i = 0
# while i < len(x):




# # print(fun(x1))
#
# print(ord('('))
# print(ord(')'))
# print(ord('['))
# print(ord(']'))
# print(ord('{'))
# print(ord('}'))
#
# x = [4,5,6,5,4]
# print(x == x[::-1])

# Given an expression string x.
# Examine whether the pairs and the orders of {,},(,),[,]
# are correct in exp.
# For example, the function should
# return 'true' for exp = [()]{}{[()()]()}
# and 'false' for exp = [(]).
# Note: The drive code prints "balanced" if function return true,
# otherwise it prints "not balanced".
# Example 1:
# Input:
# {([])}
# Output:
# true
# Explanation:
# { ( [ ] ) }. Same colored brackets can form
# balanced pairs, with 0 number of
# unbalanced bracket.


# def fun(x):
#     d = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
#     i = 0
#     while i < len(x)-1:
#         if d[x[i]] + d[x[i+1]] == 0 and d[x[i]] > d[x[i+1]]:
#             x = x[:i] + x[i+2:]
#             if i > 0:
#                 i -= 1
#         else:
#             i += 1
#     return len(x) == 0
# x1 =  '{[]}()()((())[])'
# print(fun(x1))

# 1. Write a Python program to find a list of integers
# with exactly two occurrences of nineteen
# and at least three occurrences of five.
# Return True otherwise False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

# def fun(x):
#     return x.count(19) == 2 and x.count(5) > 2
# print(fun([19, 19, 19, 15, 5, 3,5,5, 5, 2]))




# 3. Write a Python program that accepts an integer !!!!!!!!!!!!!!!!!!!
# and determines whether it is greater than 4^4
# and which is 4 mod 34.

# 3. Напишите программу на Python,
# которая принимает целое число и определяет,
# больше ли оно 4 ^ 4 и что равно 4 по модулю 34.

# Input:
# 922
# Output:
# True
# Input:
# 914
# Output:
# False
# Input:
# 854
# Output:
# True
# Input:
# 854
# Output:
# True


# 4. We are making n stone piles! The first pile has n stones.
# If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones.
# Each pile must more stones than the previous pile but
# as few as possible. Write a Python program to find the number
# of stones in each pile.


# 4. Мы делаем n каменных свай!
# В первой куче n камней. Если n четно,
# то во всех кучах четное количество камней.
# Если n нечетно, то во всех кучах нечетное количество камней.
# В каждой куче должно быть больше камней, чем в предыдущей,
# но как можно меньше. Напишите программу на Python,
# чтобы найти количество камней в каждой куче.

# Input: 2
# Output:
# [2, 4]
# Input: 10
# Output:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# Input: 3
# Output:
# [3, 5, 7]
# Input: 17
# Output:
# [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


# class Prod:
#     def fun(self, x):
#         return [x+2 * i for i in range(x)]
# print(Prod().fun(3))






# 5. Write a Python program to check the
# nth-1 string is a proper substring of the nth string
# in a given list of strings.

# 5. Напишите программу на Python для проверки того, !!!!!!!!!!!!!!!!!!!!!!!!
# что n-я строка-1 является правильной подстрокой
# n-й строки в заданном списке строк.

# Input:
# ['a', 'abb', 'sfs', 'oo', 'de', 'lde']
# Output:
# True
# Input:
# ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# Output:
# True



# 6. Write a Python program to test a
# list of one hundred integers between
# 0 and 999, which all differ by ten from
# one another. Return True otherwise False.

# 6. Напишите программу на Python
# для тестирования списка из ста целых
# чисел в диапазоне от 0 до 999, которые все
# отличаются друг от друга на десять.
# Возвращает значение True,
# в противном случае значение False.

# Input:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
# Output:
# True
# Input:
# [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]
# Output:
# False

# 1
# x = list(map(int,input('x = ').split()))
# print(x)
# if all(x[i]-x[i+1] == -10 for i in range(len(x)-1)):
#     print(True)
# else:
#     print(False)

# 2
# print(list(range(0,1000,10)))



# 8. Write a Python program to split a
# string of words separated by commas
# and spaces into two lists, words and separators.

#8. Напишите программу на Python для
# разделения строки слов, разделенных
# запятыми и пробелами, на два списка,
# слова и разделители.


# Input: W3resource Python, Exercises.
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: The colors in my studyroom are blue, green, and yellow.
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
# Click me to see the sample solution


# def fun(x):
#     import  re
#     k = re.split(r"([ ,])+",x)
#     return [k[::2],k[1::2]]
#     #
#     # i = j = 0
#     # y = [[],[]]
#     # if len(x) == 0:
#     #     return print('None')
#     # while j < len(x):
#     #     t = True
#     #     if not x[j].isalpha() and not x[j].isdigit():
#     #         if x[j] == '.'and j == len(x)-1:
#     #             y[0].append(str(x[i:]))
#     #         elif len(str(x[i:j])) > 0:
#     #             y[0].append(str(x[i:j]))
#     #         t = False
#     #
#     #         y[1].append(str(x[j]))
#     #         i = j+1
#     #         j = i
#     #     else:
#     #         j += 1
#     # else:
#     #     if t and len(str(x[i:j])):
#     #         y[0].append(str(x[i:j]))
#     # print(y)
#
# x1 = 'The dance, held in the school gym, ended at midnight.'
# # x1 = 'W3resource Python, Exercises.'
# # x1 = '...00.0...'
# print(fun(x1))


# 9. Write a Python program to find a list
# of integers containing exactly four distinct values,
# such that no integer repeats twice consecutively
# among the first twenty entries.

# 9. Напишите программу на Python,
# чтобы найти список целых чисел,
# содержащий ровно четыре различных значения,
# таким образом, чтобы ни одно целое число не
# повторялось дважды подряд среди первых двадцати записей.

# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

# def fun(x):
#     i = 0
#     j = 3
#     while j < len(x):
#         if len(set(x[i:j+1])) != 4:
#             print('false')
#             break
#         i = j+1
#         j += 4
#     else:
#         print('True')
#
# x1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# # x1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# fun(x1)






# 4. Write a Python program to
# construct the following pattern,
# using a nested for loop.

#4. Напишите программу на Python для
# построения следующего шаблона,
# используя вложенный цикл for.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



# k = 5
# for i in range(1,2*k):
#     if i <= k:
#         print('* '*i)
#     else:
#         print('* '*(2*k-i))

# def fun(x,k):
#     if x == k+1:
#         return
#     else:
#         print('* '*x)
#         return fun(x+1,k), print('* '*(x-1))
# k = 6
# fun(1,k)

# def fun(x,k):
#     if x == k+1:
#         return
#     else:
#         print((str(x) + ' ') * x)
#         return fun(x+1,k), print((str(x-1) + ' ') * (x-1)) if x > 1 else ''
# k = 7
# fun(1,k)



# 9. Write a Python program to get the
# Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found
# by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# 9. Напишите программу на Python, чтобы получить ряд
# Фибоначчи в диапазоне от 0 до 50.
# Примечание: Последовательность Фибоначчи - это ряд чисел :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Каждое следующее число определяется
# путем сложения двух чисел перед ним.
# Ожидаемый результат : 1 1 2 3 5 8 13 21 34



# def fun(a1,a2,x,y=[]):
#     if a1 + a2 >= x:
#         return y
#     else:
#         y.append(a1)
#         y.append(a2)
#         a1, a2 = a2, a1 + a2
#         return fun(a2,a1+a2,x,y)
#
# x1 = 10
# print(fun(0,1,x1))




# for i in range(50):
#     if i % 5 == 0 and i % 3 == 0:
#         print('fizzbuzz')
#         continue
#     elif i % 3 == 0:
#
#         print('fizz')
#
#     elif i % 5 == 0:
#         print('buzz')
#         continue
#     else:
#         print(i)


#
# reg in gmail, zadat dannie ,  y sozdat bezopasniy porol, povtorit, (yes/no)
#
# taza beri, enter mail u porol ,
#

































































