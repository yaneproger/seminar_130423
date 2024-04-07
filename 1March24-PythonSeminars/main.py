# import random

# Задача 1.
# Общее обсуждение За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750 Output: 2

# n = int(input("speed: "))
# m = int(input("distance: "))

# res = (m+n-1)//n

# temp = int(bool(m % n))
# print(temp)
# res = m//n + temp

# print(res)


# Задание Пример Задача 2:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

# number = int(input("enter 3digit number : "))
# summ = number % 10+((number//100) % 10)+((number//10) % 10)
# print(summ)


# number = int(input("enter 3digit number : "))
# summ = ((number//100) % 10)+((number//10) % 10)+(number % 10)

# print(summ)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали
# одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# (x+x)+((x+x)*(x+x))=s
# 6x=s
# x=s/6

# Summ = int(input("enter number of toys"))
# print(Summ//6, Summ//6*4, Summ//6)


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes 123456 -> no

# number = ()
# while len(number) != 6:
#     number = input("enter 6 digit  number: ")
# digits = int(number)
# first = digits // 100000
# print(first)
# second = (digits % 100000) // 10000
# print(second)
# third = (digits % 10000) // 1000
# fourth = (digits % 1000) // 100
# fifth = (digits % 100) // 10
# sixth = (digits % 10)
# print(sixth)
# print(first+second+third)
# print(fourth+fifth+sixth)
# if (first+second+third == fourth+fifth+sixth):
#     print("U'r lucky")
# else:
#     print("try one more time")


# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes 3 2 1 -> no

# m = int(input("enter one side's size :"))
# n = int(input("enter other side's size :"))
# k = int(input("enter needed squares quantity :"))
# # res = m*n/k

# if (k % m == 0 or k % n == 0) and k < m*n:
#     print("yes")
# else:
#     print("no")


# Binary search

# def binary_search(list, item):

#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low+high)//2
#         print(f'mid{mid}')
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid-1
#             print(f'high{high}')
#         else:
#             low = mid+1
#             print(f'low{low}')
#     return None


# my_list = [1, 3, 5, 7, 9, 13, 14, 16, 18, 23, 25, 27,
#            29, 31, 34, 36, 37, 39, 41, 43, 44, 46, 47, 49]

# # print(binary_search(my_list, 3))
# # print(binary_search(my_list, 45))
# print(binary_search(my_list, 49))


# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

# num = int(input())
# max_wheit = 0
# min_wheit = 30001
# for i in range(num):
#     mellon = int(input())
#     if max_wheit < mellon:
#         max_wheit = mellon
#     if min_wheit > mellon:
#         min_wheit = mellon
# print(max_wheit, min_wheit)

# Задача №15. Решение в группах 15.
# Иван Васильевич пришел
# на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много
# и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input:
# 5 ->
# 5 1 6 5 9
# Output: 1 9

# n = int(input("Пользователь вводит одно число N - количество арбузов : "))
# arbuz_list = []
# for i in range(n):
#     arbuz_list.append(int(input("vvedite ves arbuza : ")))
#     max_arbuz = arbuz_list[0]
#     min_arbuz = arbuz_list[0]
# for arbuz_mass in arbuz_list:
#     if arbuz_mass > max_arbuz:
#         max_arbuz = arbuz_mass
#     if arbuz_mass < min_arbuz:
#         min_arbuz = arbuz_mass
# print(f'max_arbuz :{max_arbuz}')
# print(f'min_arbuz :{min_arbuz}')
# print(f'arbuz_list {arbuz_list}')


# Задача №13. Общее обсуждение
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов
# Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых
# дней (1 ≤ N ≤ 100). В следующих строках располагается N целых
# чисел. Каждое число – среднесуточная температура в соответствующий
# день. Температуры – целые числа и лежат в диапазоне
# от –50 до 50
# Input:
# 6 ->
# -20 30 -40 50 10 -10
# Output: 2
# import random
# n = int(input("общее количество рассматриваемых дней (1 ≤ N ≤ 100) : "))
# arbuz_list = []
# counter = 0
# max_days = 0
# for i in range(n):
#     # arbuz_list.append(
#     # int(input("vvedite целые числа в диапазоне от -50 до 50 : ")))
#     numbers = random.randint(-50, 50)

# print(numbers)
# # for arbuz_mass in arbuz_list:
# for i in range(len(arbuz_list)):
#     # if arbuz_mass > 0 and arbuz_mass+1 > 0:
#     if arbuz_list[i] > 0:
#         counter += 1
#         if max_days < counter:
#             max_days = counter
#     else:
#         counter = 0
# print(f'count of warm days :{counter}')
# print(f'count of max warm days :{max_days}')


# n = int(input("enter digits quantity : "))
# digit_list = []
# s4et = 0
# max_value = 0
# for i in range(n):
#     digit = random.randint(-50, 50)
#     digit_list.append(digit)
#     if digit > 0:
#         s4et += 1
#         if max_value < s4et:
#             max_value = s4et
#     else:
#         s4et = 0
# if max_value < s4et:
#     max_value = s4et

# print(digit_list)
# print(max_value)


# Задача №19.
# Решение в группах Дана последовательность
# из N целых чисел и число K. Необходимо
# сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [4, 5, 1, 2, 3]

# data = [1, 2, 3, 4, 5]
# print(data)
# k = 3
# # data1 = []
# # for i in range(len(data)):
# #     # data1[i] = data[i%k]
# #     data1.append(data[i-k+1])
# # print(data1)
# for i in range(k):
#     temp1 = data.pop(len(data)-1)
#     data.insert(0, temp1)
# print(data)
#
#
#
#


# Задача №21.
# Общее обсуждение Напишите программу для
# печати всех уникальных значений в словаре.
# Input:
# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#  {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# data1 = []
# for dictn in data:
#     print(*dictn.keys())
#     print(*dictn.values())
#     for val in dictn:
#         data1.append(dictn.get(val))
#     dict_set = set(data1)
# print(dict_set)

# res = set()
# for d in data:
#     for element in d.values():
#         res.add(element)
# print(res)

# res = set()
# for d in data:
#     res = res.union(set(d.values()))
# print(res)


# Задача 12:
# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# d = s**2 - 4*p
# x = int((s - d**(0.5))//2)
# y = int((s + d**(0.5))//2)
# print(x, y)


# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# n = '1 1 1 0 0 0'
# data = n.split(" ")
# print(data)
# print(f'len-data : {len(data)}')
# zeros4et = 0
# positives4et = 0
# for i in data:
#     # print(f'i : {i}')
#     if int(i) == 0:
#         # print(data[i])
#         # print(f'i 1  : {i}')
#         zeros4et += 1
#         # print(f'zeros4et 1 {zeros4et}')
#     else:
#         positives4et += 1

# if zeros4et == len(data) or positives4et == len(data):
#     print("no need  in any moves {0}")
# elif zeros4et < positives4et:
#     print(f'zeros4et  {zeros4et}')
# elif positives4et < zeros4et:
#     print(f'positives4et  {positives4et}')
# else:
#     print("they are equals u can select any of 1 or 0's")

# print(coins.count(min(coins, key=coins.count)))


# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input("enter a numer : "))
# for i in range(n):
#     res = 2**i
#     if res <= n:
#         print(res)


# Задача №17.
# Общее обсуждение Дан список чисел.
# Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# data = [1, 1, 2, 0, -1, 3, 4, 4]
# data1 = set(data)
# print(len(data1))


# Задача №23.
# Решение в группах Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input:
# [0, -1, 5, 2, 3]
# Output:
# 2 (-1 < 5, 2 < 3)
# Примечание:
# Пользователь может вводить значения списка или список задан изначально.
# list_1 = [0, -1, 5, 2, -1]
# count = 0
# for i in range(len(list_1)):
#     if list_1[i] > list_1[i - 1]:
#         count += 1
# print(count)


# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:
# # list_1 = [1, 2, 3, 4, 5]
# k = 3
# # # 1
# data = [1, 2, 3, 4, 5, 3]
# print(sum([1 for i in data if i == k]))


# Требуется найти в массиве list_1
# самый близкий по значению элемент
# к заданному числу k и вывести его.
# Считать, что такой элемент может
# быть только один. Если значение
# k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5
# print(type(list_1))


# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8


# list_1 = [1, 12, 6, 7, 8, 15]

# k = 11

# print([i if i == k else i == k + 1 or i == k-1 for i in list_1])


#
#
#
#


# При использовании if / else используйте их перед циклом
# [x if x in 'aeiou' else '*' for x in 'apple']

# data = [i if i == k else i == k -
# 1 for i in [i for i in list_1 if i == k or i == k-1]]


# print([i if i == k else i == k-1 for i in [i for i in list_1 if i == k or i == k-1]])

# print(max([list_1[i] if i == k else i == k-1 for i in range(len(list_1))]))


# wordsdict = {"A": "1", "E": "1", "I": "1", "O": "1", "U": "1", "L": "1", "N": "1",
#              "S": "1", "T": "1", "R": "1", "D": "2", "G": "2", "B": "3",
#              "C": "3", "M": "3", "P": "3", "F": "4", "H": "4", "V": "4",
#              "W": "4", "Y": "4", "K": "5", "J": "8", "X": "8", "Q": "10", "Z": "10",

#              "А": "1", "В": "1", "Е": "1", "И": "1", "Н": "1", "О": "1",
#              "Р": "1", "С": "1", "Т": "1",
#              "Д": "2", "К": "2", "Л": "2", "М": "2", "П": "2", "У": "2",
#              "Б": "3", "Г": "3", "Ё": "3", "Ь": "3", "Я": "3",

#              "Й": "4", "Ы": "4",

#              "Ж": "5", "З": "5", "Х": "5", "Ц": "5", "Ч": "5",
#              "Ш": "8", "Э": "8", "Ю": "8",
#                             "Ф": "10", "Щ": "10", "Ъ": "10"

#              }


# k = 'ноутбук'
# word = k.split()
# print(word)
# wordcost = 0
# data = []
# wordsdict = {"A,E,I,O,U,L,N,S,T,R,B,C,M,P": "1",
#              "D,G": "2",
#              "B,C,M,P": "3",
#              "F,H,V,W,Y": "4",
#              "K": "5",
#              "J,X": "8",
#              "Q,Z": "10",
#              "А,В,Е,И,Н,О,Р,С,Т": "1",
#              "Д,К,Л,М,П,У": "2",
#              "Б,Г,Ё,Ь,Я": "3",
#              "Й,Ы": "4",
#              "Ж,З,Х,Ц,Ч": "5",
#              "Ш,Э,Ю": "8",
#              "Ф,Щ,Ъ": "10"

#              }
# for key in wordsdict:
# for el in k.upper():
#     for element in wordsdict.keys():

#         print(element)
# print(wordsdict.get(el))
# if el in element:
# print(el.values())
# print(wordsdict.get(el))
# wordcost = wordcost+int(wordsdict.get(el))


# print(data)
# print(wordcost)

# "1", : "1", "I": "1", "O": "1", "U": "1", "L": "1", "N": "1",
#              "S": "1", "T": "1", "R": "1", "D": "2", "G": "2", "B": "3",
#              "C": "3", "M": "3", "P": "3", "F": "4", "H": "4", "V": "4",
#              "W": "4", "Y": "4", "K": "5", "J": "8", "X": "8", "Q": "10", "Z": "10"


# data1 = []
# for dictn in data:
#     print(*dictn.keys())
#     print(*dictn.values())
#     for val in dictn:
#         data1.append(dictn.get(val))
#     dict_set = set(data1)
# print(dict_set)

# res = set()
# for d in data:
#     for element in d.values():
#         res.add(element)
# print(res)

# res = set()
# for d in data:
#     res = res.union(set(d.values()))
# print(res)


# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква,
# а значение - код буквы.
# Напишите преобразование в одну строку.


# numbers = 'abc bcd abc bcd wwe qwe wwe qwe eeq'

# numbers_dict = {i: ord(i) for i in numbers}

# print(numbers_dict)


# 1. Дано натуральное число *N* и последовательность из *N* элементов.
#   Требуется вывести эту последовательность в обратном порядке.

# ***Примечание.*** В программе запрещается объявлять массивы
#  и использовать циклы (даже для ввода и вывода).


# def reverse_num(number):
#     if number < 1:
#         return 1
#     digit = int(input("Enter a number :"))
#     # print(count, end="")
#     reverse_num(number-1)
#     print(digit, end=":")


# counter = int(input("Enter counter : "))
# reverse_num(counter)


# import sys
# from PyQt5.QtCore import *

# from PyQt5.QtWidgets import *
# from PyQt5.QtMultimediaWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и,
# при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество
# элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел


# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.


# list_1 = [2, 2, 2]

# print(sum([list_1.count(i) % 2 for i in set(list_1)   ]))


# print(sum([1 for i in list_1 if list_1.count(i) // 2 == 0]))

# print(sum([list_1.count(i) % 2 for i in set(list_1) if list_1.count(i) // 2 == 0]))


# def champ(arr):
#     count = 0
#     for i in range(len(list_1)):
#         for j in range(i+1, len(list_1)):
#             if list_1[j] == list_1[i]:
#                 count += 1
#     return count


# print(champ(list_1))


# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# count = 0
# max1 = 0
# for i in range(len(arr)):
#     count = arr[i-2] + arr[i-1] + arr[i]
#     if count > max1:
#         max1 = count
# print(max1)


# def countdown(i):
#     print('Obratniy otschet')
#     print(i)
#     if i <= 0:  # .... Базовый случай
#         return
#     else:    # --<· ·· ······ Рекурсивный случай

#         countdown(i-1)

# countdown(5)


# Напишите функцию f,
# которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить,
# только возвращать значение.

# a = 3
# b = 5


# def f(a, b):
#     if b == 1:
#         return a

#     return a*f(a, b-1)


# print(f(a, b))


# Напишите рекурсивную функцию
# sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел.
# Из всех арифметических операций
# допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Функция не должна ничего выводить,
# только возвращать значение.

# a = 3
# b = 5

# def sum(a, b):
#     if b == 0:
#         return a

#     return b+sum(a, b-b)


# print(sum(a, b))


# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1
# и границы диапазона в виде чисел min_number, max_number.
# Пример
# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:
# 1# 2# 3# 6# 7# 9# 10# 11# 13# 14# 16# 19

# ([print(i) for i in range(len(list_1))
#   if list_1[i] >= 0 and list_1[i] <= 10])


# Арифметическая прогрессия
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент a1 ,
# разность d и количество элементов
# n будет задано автоматически.
# Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Пример
# На входе:# a1 = 2# d = 3# n = 4
# На выходе:# 2# 5# 8# 11


# # enumerate funciton working principe
# # print(list(enumerate(['a', 'b', 'c'], start=1)))
# #  output will be : [(1, 'a'), (2, 'b'), (3, 'c')]


# toreturn copy of  an initial list
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# data = [[1, 2, 3], [1, 2, 3], c]
# transformed_data = list(map(lambda x: x, data))
# print(transformed_data)


# Задача №49. Решение в группах Ввод:
# Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты
# самой далекой планеты. Каждая
# орбита представляет из себя кортеж из пары чисел
# - полуосей ее эллипса. Площадь эллипса вычисляется
# по формуле S = pi*a*b, где a и b - длины полуосей эллипса.


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# def find_farthest_orbit(orbits):
#     return (max(orbits, key=lambda x: x[0]*x[1] if x[0] != x[1] else 0))


# print(find_farthest_orbit(orbits))

import sys
import os


def characteristics(func1, data):
    return all(list(map(func1, data)))
    # return any(set(map(func1, data)))
# def same(characteristics: callable, elements: list) -> bool:
#     pass


elements1 = [0, 0, 0, 0]
# elements1 = [2, 4, 6, 8, 9]
elements2 = [1, 2, 3, 4]

elements3 = [1, 3, 5, 7]

# print(same(is_odd, elements1))

print(characteristics(lambda x: x % 2 == 0, elements2))
