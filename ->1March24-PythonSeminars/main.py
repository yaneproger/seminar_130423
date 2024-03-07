import random

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
# k = 4
# data1 = []
# for i in range(len(data)):
#     # data1[i] = data[i%k]
#     data1.append(data[i-k+1])
# print(data1)
