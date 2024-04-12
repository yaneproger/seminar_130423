

"""

# import abc


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# town = input("Enter your town: ")
# print(name,age,town)
# print(name.find('a'))

"""
"""
def new_func(name, town):
    print(name.upper(),town)

name = input("Enter your name: ")
town = input("Enter your town: ")
new_func(name, town)


#print(dir(name))
#print(dir(int))


import math


def my_name(name1):
      print(name1)


my_name('Eldar')


#my_name('Eldar')

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
var1 = input ("enter number:" )

print(bar(var1))



my_list = [1, 2, 3, 4]

print(my_list)


a = 10


def new_fn():
    print('Hello', 'Eldar')  # comments

    # this
    # is
    # comments

# this   - Ctrl + / makes auto comment
# is   - use Ctrl + / - to disable comment
#  comment


new_fn()       # This is inline comment

print(10)


print(print(10+5))

print(input("Enter ur name: "))

print(def my_fn():
      print('Eldar'))

print(if True print(10))

import datetime
print(print(10+5))


print(datetime.MAXYEAR)
print(datetime.MINYEAR)
"""

"""
# print(import datetime)


# import datetime


# def time(self: datetime.
#          datetime(year=2023, month=03, day=22,
#                   hour=07, minute=27, second=10)):

#     print(datetime.date(),
#           datetime.time())


# time

"""


"""

def newfn(a, b, c):
    var = print(a/b/c)
    return var


def my_fn(x, y):
    name = print(x+x*y)
    return name


# print(my_fn(x=10, y=10))
# print(newfn(a=1, b=2, c=5))
newfn(1, 2, 5)  # newfn(a=1, b=2, c=5)
my_fn(1, 2)

{abba: 1, betta: 2}

my_list = [1, 2, 3, 4, 5]


def new_fn():
    print('Hello!')
    x = 1
    y = 2
    z = 3
    return x + y + z


print(new_fn)


print(my_list)
print(my_dict)

my_first_logical_type = True

print(my_first_logical_type)

x = 11


def test_log_type():
    if x > 10:
        return True


print(test_log_type())


my_first_variable_number = 1

print(my_first_variable_number)
my_first_variable_string = 'String1'

print(my_first_variable_string)


my_dictionary = {'abba': 1, 'betta': 2, 'name': 'Eldar'}
print(my_dictionary)
my_number = 10
print(my_number)



def print_name(name):
    print(name)


print_name('Eldar')

# print_name = 10


print(print_name('Eldar'))


a = 1
b = 100
c = 20
d = 40
e = 150
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(max)

my_name = 'Eldar'
print(id(my_name))


my_num = 100

print(id(my_num))

other_num = my_num
print(id(other_num))

"""
"""
# max number from five numbers
a = 1
b = 8
c = 3
d = 2
e = 6
max = a

if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(max)

# even numbers summ 1to15
I = 2
N = 0
while I <= 15:
    N = N+I
    I = I+2
print(N)


"""
"""
# calculate even numbers from entered to 15
s = 0
i = int(input("add entered even number to another 15 times :"))
if i > 15:
    print(i, 'enter number under 15')
# i = 0
# positive_float = float('inf')
if i % 2 == 0:
    while i <= 15:
        s = s+i
        i = i+2
else:
    print(i, 'is an odd number')
print(s)
"""
"""


"""


"""
# min value from four number

A = 1
B = 2
C = 3
D = 4
Min = A
if B < Min:
    Min = B
if C < Min:
    Min = C
if D < Min:
    Min = D
print(Min)

"""
"""
# to find arith mean from 4 numb
a = 1
b = 25
c = 30
d = 4
mean = (a+b+c+d)/4
print(mean)

# positive_float = float('inf')
"""
"""
n = 0
f = 0
d = int(input("enter desired number"))

if d == 0:
    f = 1
    print('the factorial of 0 defined as')

while n != d:
    f = n*(n-1)
    n = n+1
print(f)

"""
"""
my_name = 'Eldar'
print(id(my_name))
my_num = 100
print(id(my_num))
other_num = my_num
print(id(other_num))
my_numbers = [1, 2, 3, 4, 5]
print(len(my_numbers))
print(my_numbers[-1])
my_numbers[2] = 33
print(my_numbers)
my_numbers[-3] = 333
print(my_numbers)
del my_numbers[2]
print(len(my_numbers))
print(my_numbers)
my_numbers.insert(2, 3)
print(my_numbers)
my_numbers.append(6)
print(my_numbers)
my_numbers.insert(6, 7)
print(my_numbers)
new_array = [8, 9, 10]
new_array1 = my_numbers+new_array
print(new_array1)

users_array = [{'user1': 123, 'user2': 456, 'user3': 234}]
print(users_array)
print(users_array[0])
users_array.insert(2, {'pogoda': 'xoroshaya', 'skoro': 'leto'})
print(users_array)
print(len(users_array))
users_array.insert(99, {'a1': '12ya', 'so': '344'})
print(len(users_array))
print(users_array[2]['a1'])
print(users_array)
print(users_array[2]['so'])
"""
"""
numbers = [1, 2, 3, 4, 5]
size = (len(numbers))
index = 0
mean = 0
while index < size:
    mean = mean+numbers[index]
    print(mean)
    index = index+1
mean = mean/size
# print('arithmetic mean =', mean)
print(mean)
# print(len(numbers))
"""
"""
# from Geekbrains arithmeticMean-Avg

numbers = [1, 2, 3, 4, 5]
size = 5
index = 0
sum = 0
avg = 0
while index < size:
    sum = sum+numbers[index]
    index = index+1
avg = sum/size
print(avg)

"""
"""
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers)
numbers[0] = 11
print(numbers[0])
print(numbers)
print(numbers.index(11))
print(numbers.index(2))
"""
"""
# to find indexes of max and min values
# input(int(numbers=[]))
numbers = [1, 20, 3, 4, 5, 2, 10]
size = len(numbers)
index = 0
min = numbers[0]
max = numbers[0]
n_min = 0
n_max = 0
while index < size:
    if numbers[index] < min:
        min = numbers[index]
        n_min = index
    if numbers[index] > max:
        max = numbers[index]
        n_max = index
    print(min)
    print(max)
    index = index+1
print('min index=', n_min, 'min value=', min)
print('max index=', n_max, 'max value=', max)
"""

"""
# to reverse array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_new = []
index = 0
size = len(numbers)
new_symbol = 0
while index < size:
    new_symbol = numbers[(len(numbers)-1)]-index
    array_new.append(new_symbol)
    index = index+1
    # print(new_symbol)
print(numbers)
print(array_new)

"""
"""
# skalar product and array
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 20, 30, 40, 50, 60, 70, 80, 90]
c = []
index = 0
size = len(a)
skal = 0
print(size)
while index < size:
    skal = skal+(a[index]*b[index])
    c.append(a[index]*b[index])
    index = index+1
# c.remove(10)
# c.pop(1)
print(skal, c)

"""
"""
n = [1, 2, 3]
size = len(n)
index = 0
max = n[0]
i_max = 0
max2 = n[0]
while index < size:
    if n[index] > max2:
        max2 = n[index]
        if n[index] > max:
            max = n[index]
            i_max = i_max+1
        # index = index+1

    index = index+1

n.remove(max)

print(max2)
print(max)

# print(i_max)
"""


"""
# to find second max element
x = [50, 80, 75, 55]
first = 0
second = 0
i = 0
size = len(x)
for i in range(size):
    print("the value of the index i, equals ", x[i])
    if x[i] > first and x[i] > second:
        print(first)
        print(second)
        print('x[i] element', x[i],
              ' is more than 1st and 2nd, write - MOVE! -> 1st value to -> 2nd and xi ->value to ->1st')
        second = first
        # print(first)
        print('second', second, 'first', first)
        first = x[i]
        print('end of 1st if')
    if x[i] < first and x[i] > second:
        print('x[i] element', x[i],
              ' is lower than 1st and more than 2nd, write', x[i], 'value to 2nd')
        second = x[i]
        print('second', second)
        print('end of 2nd if')
    if x[i] < first and x[i] < second:
        print(x[i], "is lower, than 1st and 2nd, dont write any")
        print('end of last if')
print("1st", first, "second", second)

"""
"""

# to find summ of values between indexes of max and min values

numbers = [1, 5, 2, 70, 3, 4]
size = len(numbers)
index = 0
min = numbers[0]
max = numbers[0]
n_min = 0
n_max = 0
old_max = 0
tempsum = 0
sum = 0
for index in range(size):
    print(min)
    print(max)
    print("the value of the index i, equals ", numbers[index])
    if numbers[index] < min:
        min = numbers[index]
        n_min = index
        print('min is', min)
    if numbers[index] > max:
        old_max = max
        print('old_max is', old_max)
        max = numbers[index]
        n_max = index
        print('max is', max)
    if numbers[index] > min and old_max < max:
        print('tempsum index', numbers[index])
        tempsum = tempsum+numbers[index]
    print('min', min)
    print('max', max)
    print('tempsum', tempsum)
index = index+1
sum = tempsum-max
print('sum', sum)
# print('min index=', n_min, 'min value=', min)
# print('max index=', n_max, 'max value=', max)

"""


"""
# to find second max element
x = [1, 2, 3, 4]
first = 0
second = 0
i = 0
min_value = 0
max_value = 0
size = len(x)
for i in range(size):
    print("the value of the index i, equals ", x[i])
    if x[i] > first and x[i] > second:
        print(first)
        print(second)
        print('x[i] element', x[i],
              ' is more than 1st and 2nd, write - MOVE! -> 1st value to -> 2nd and xi ->value to ->1st')
        second = first
        # print(first)
        print('second', second, 'first', first)
        first = x[i]
        max_value = x[i]
        print('end of 1st if')
    if x[i] < first and x[i] > second:
        print('x[i] element', x[i],
              ' is lower than 1st and more than 2nd, write', x[i], 'value to 2nd')
        second = x[i]
        print('second', second)
        print('end of 2nd if')
    if x[i] < first and x[i] < second:
        print(x[i], "is lower, than 1st and 2nd, dont write any")
        min_value = x[i]
        print('end of last if')
print("1st", first, "second", second)
"""
"""
n = [1, 2, 3, 4333, 555, 23000, 45]
size = len(n)
index = 0
max = 0
i_max = 0
while index < size:
    if n[index] > max:
        max = n[index]
        print(index)
        i_max = index
    index = index+1
print(max, i_max)

"""


"""
# to find indexes of max and min values
# input(int(numbers=[]))
numbers = [1, 200, 3, 4, 5, 7, 888, 65, 87, 1045, 99, 345, 555]
size = len(numbers)
index = 0
min = numbers[0]
max = numbers[0]
middle = 0
n_min = 0
n_max = 0
n_middle = 0
while index < size:
    if numbers[index] < min:
        print('MinIFIndex=', index, 'MinIFValue', numbers[index])
        min = numbers[index]
        n_min = index
    if numbers[index] > max:
        print('MaxIFIndex=', index, 'MaxIFValue', numbers[index])
        max = numbers[index]
        n_max = index
        print('n_max', n_max)
    if numbers[index] < max and numbers[index] > min:
        print('MiddleIFIndex=', index, 'MiddleIFValue', numbers[index])
        middle = numbers[index]
        n_middle = index
        print('middle', middle, 'n_middle', n_middle)
    print(min)
    print(max)
    index = index+1
print('min index=', n_min, 'min value=', min)
print('max index=', n_max, 'max value=', max)
"""

"""
# to find indexes of max and min values
# input(int(numbers=[]))
numbers = [1, 20, 3, 40, 5, 200, 10]
size = len(numbers)
index = 0
min = numbers[0]
max = numbers[0]
n_min = 0
n_max = 0
while index < size:
    if numbers[index] < min:
        min = numbers[index]
        n_min = index
    if numbers[index] > max:
        max = numbers[index]
        n_max = index
    print(min)
    print(max)
    index = index+1
print('min index=', n_min, 'min value=', min)
print('max index=', n_max, 'max value=', max)

"""
"""

numbers = [2, 5, 13, 7, 6, 4]
size = 6
sum = 0
avg = 0
index = 0
while index < size:
    sum = sum+numbers[index]
    index = index+1
avg = sum/size
print(avg)

"""
"""
# to move max number to rigth end of array

numbers = [2, 5, 13, 7, 6, 4]
size = 6
index = 0
max_idx = 0
max = numbers[max_idx]
while index < size:
    if numbers[index] > max:
        max_idx = index
        max = numbers[index]
    index = index+1
numbers[max_idx] = numbers[size-1]
numbers[size-1] = max

print(numbers)

"""
"""
# to using "bubble sorting" to move max number to rigth end of array

numbers = [2, 5, 13, 7, 6, 4]
size = 6
index = 0
max_idx = 0
max = numbers[max_idx]
while index < size:
    if numbers[index] > max:
        max_idx = index
        max = numbers[index]
    index = index+1
    # while index < size:
    max_idx = index+1
    max = numbers[index+1]

print(numbers)
"""
"""

numbers = [1, 8, 3, 8, 2, 6, 8, 8]
index = 0
maximum = numbers[index]
count_maximal = 0
last_max_index = 0
first_max_index = 0
while index < len(numbers):
    if numbers[index] > maximum:
        second_max = maximum
        maximum = numbers[index]
        count_maximal = 1
        first_max_index = index
    else:
        if numbers[index] == maximum:
            count_maximal = count_maximal+1
            last_max_index = index
    index = index+1
print('MaxElementsValue', count_maximal, 'ArraySize', len(numbers),
      'first_max_index', first_max_index, 'last_max_index', last_max_index)

"""


"""






# Алгебра логики(Булевская Алгебра) True(1) False(0)

# конъюнкция(логическое умножение) - and
# дизъюнкция(логическое сложение) - or
# отрицание(обратное значение) - not

# print(7 > 5 and 10 < 0)
# #      1  *   0 = 0(False)

# print(1 > 2 or 5 > -1)
# #      0    +    1 = 1

# print(3 > 2 or 5 > 2)
# #      1    +    1 = 1

# print((3 > 2 or 5 > 3) and 2 < 0)





/*



# #  Задача 1 За день машина проезжает n километров. Сколько
#  # дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

*/

"""

# Задача 1

# n = int(input("Сколько за день проезжает машина? - "))
# m = int(input("Общее расстояние: "))
# # # 750 : 700 = 1(ост. 50) + 1
# # # 2100 : 700 = 3 (ост. 0) + 0
# print((m + n - 1) // n)


# (m + n - 1) // n
# (1401 + 700 - 1) // 700 == 3
# print(-12 % 5) # 15 - 12 = 3
# print(-14 % 6) # 18 - 14
# print(-7 % 3) # 9 - 7


# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
# a = 20
# b = 21
# c = 22
# res = a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2
# print(res)
"""

# Вагоны в электричке пронумерованы натуральными числами, 
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
#  это зависит от того, в какую сторону едет электричка). 
#  В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
#  что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
#    Напишите программу, которая будет это делать или сообщать, 
#    что без дополнительной информации это сделать невозможно. 

#    j+i-1

#    if j=i  это сделать невозможно. 


#    Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES


# if (n%4&&n%400 ==0) 
# else n%100 !=0


# year = int(input("Введите год: "))
# print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


"""


# n = int (input("Enter a number"))
# print(    n%4==0 and n%400 ==0  or n%100 !=0        )
# number = int(input("enter number :"))
# if number % 2 == 0:
#     print(number, (' четное число'))
# else:
#     print(number, (' нечетное число'))
#     # else:
# #     print(number, ('четное число'))
# print(-12 % 5) # 15 - 12 = 3
# print(-14 % 6) # 18 - 14
# print(-7 % 3) # 9 - 7


# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
# print(str(45.56) * 2)

# n = int (input("Enter a number : "))
# result = 0
# while (n>0)  :
#    result = result + n%10
#    n=n//10
# print(result)


#############

# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

# Пример:


# n = 456

# # Введите ваше решение ниже

# res = ((n//100)%10)+((n//10)%10)+(n%10)
#
# n = 123
# res = 0
# while (n>0):
#    res = res + n%10
#    n=n//10
# print(res)
# print(f'n = {n} -> res = {res} ({n[0]} + {n[1]} + {n[2]})')


# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов,
# сделанных Петей, Катей и Сережей.

# n = x + x + (x + x)*2
# n = 2*x + 4*x
# x = (n//6)*4

# n = 60

# print (n//6, (n//6)*4, n//6)


# # Вы пользуетесь общественным транспортом? Вероятно,
#  вы расплачивались за проезд и получали билет с номером.
# # Счастливым билетом называют такой билет
# с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# # Вам требуется написать программу,
# которая проверяет счастливость билета
# с номером n и выводит на экран yes или no.

# # Пример:

# # n = 385916 -> yes
# # n = 123456 -> no

# n = int (input("Enter a number : "))
# a = n//100000
# b = (n//10000)%10
# c = (n//1000)%10
# d = (n//100)%10
# e = (n//10)%10
# f = (n%10)

# if n>=1000000 or n<100000:
#     print('enter 6 digit')
# else:

#         print(a,b,c,d,e,f)
#         if a + b + c == d + e + f:
#             print('yes')
#         else:
#             print('no')


# Определите, можно ли от шоколадки
# размером a × b долек отломить c долек,
# если разрешается сделать один разлом
# по прямой между дольками (то есть разломить
#  шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

# Пример:

# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

# a = int(input("Введите кол-во долек одной стороны: "))
# b = int(input("Введите кол-во долек другой стороны: "))
# c = int(input("Введите кол-во долек которое нужно получить: "))

# # a = 3
# # b = 2
# # c = 4

# # Введите ваше решение ниже

# if (c % a == 0  or c % b == 0) and c < a * b : # znachenie c - doljno bit kratno - "%"
#     # odnomu iz cisel - ili - a , ili - b
# # to est kratno odnoi iz storon wokoladki
# # esli u nas wokoladka 3 na 2 , to posle razloma  polu4im ili 2 na 2,  ili 3 na 1 ,
# # to est 4 dolki
#     print ('yes')
# else :
#     print  ('no')


# n = int(input("Введите кол-во элементов списка: "))
# data = []
# for i in range(n):
#     data.append(int(input("Введите число: ")))
#     # insert(position, element)
# print(data)


# # Задача 17
# # print([i for i in range(5)])
# # print([(i, i ** 2) for i in range(5)])

# # print([i for i in range(11) if i % 2 == 0])
# # input() ->   "-10 23 5 4 89 23"
# # input().split() -> ["-10", "23", "5", "4", "89", "23"]
# # for i in input().split():
# #     print(int(i) * 2)

# # data = [int(i) for i in input("Введите числа: ").split()]
# # print(len(set(data)))
# data = ["-10", "23", "5", "4", "89", "23"]
# print(" !! ".join(data))


# k = k % len(data)


# # informatics
# # e-olymp(vpn)
# # acmp


# list = [1,2,3,4,5,6,7]
# k = 2
# n = len

# if n == 0 or k%n==0
#   shift = list
# else:
#  k = k%n
#  shift = list[-k:] + list[:-k]


# data = [int(i) for i in input("Введите числа: ").split()]
# k = int(input("Введите кол-во сдвигов: ")) % len(data)
# for i in range(k):
#     data.insert(0, data.pop(-1))
#     # [5, 1, 2, 3, 4] k = 2
#     # data.pop(-1) -> 4
#     # data.insert(0, 4)
#     # [4, 5, 1, 2, 3]
# print(data)


# count_zero = 0
# count_one = 0
# for i in coins:
#     if i == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_zero < count_one:
#     print(count_zero)
# else:
#     print(count_one)


# 21


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V ":"S009"}, {"VIII":"S007 "}]
# # print(data[0]["V"])
# result = set()  # = {} dictionary
# for d in data:
#     for key in d:
#         result.add(d[key])
# print(result)


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# # Задача 23
# data = [int(i) for i in input("Введите числа: ").split()]
# result = [data[i - 1] < data[i] for i in range(1, len(data))]
# print(sum(result)) # складываем все элементы списка
# # range(len(data)) = 0 1 2 3 4
# # range(5) = 0 1 2 3 4


# Монетки

# Инструкция по использованию платформы

# На столе лежат n монеток.
# Некоторые из монеток лежат вверх решкой,
# а некоторые – гербом.
# Ваша задача - определить минимальное количество монеток,
# которые нужно перевернуть,
# чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins,
# где coins[i] равно 0, если i-я монетка лежит гербом вверх,
# и равно 1, если i-я монетка лежит решкой вверх.
# Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число -
# - минимальное количество монеток, которые нужно перевернуть.

# Пример использования
# На входе:

# coins = [0, 1, 0, 1, 1, 0]
# На выходе:

# 3
# coins = [int(i) for i in input("Введите числа: ").split()]
# print(coins)

# sum1=0
# sum2=0
# i=0

# for i in range(0, len(coins)):
#     print (f'len(coins) {len(coins)}')

#     if coins[i]==0:
#                     #  sum1=sum1+1
#                      sum1+=1
#                      print(f'sum1 {sum1}')
#     else :
#      if coins[i]==1:
#                     sum2+=1
#                     # sum2=sum2+1
#                     print(f'sum2 {sum2}')

# if (sum1==len(coins) or sum2==len(coins) ):
#       print (f'Zero {0}')
# else:
#     if sum1<sum2:
#         print (f'Rsum1 {sum1}')

#     else:
#         if  sum1>sum2:  print (f'Rsum2 {sum2}')

#         else:  print (f'sum1=sum2 {sum1}')


# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

# Пример


# n=16

# #Вывод
# 1
# 2
# 4
# 8
# 16

# n = int(input('enter a number : '))
# res = 0
# for i in range(n+1):
#     res = 2**i
#     # print(2**i)
#     if res <= n:
#         print(res)

# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Примечание: числа S и P задавать не нужно,
# они будут передаваться в тестах.

# В результате вы должны вывести
# все возможные пары чисел X и Y через пробел,
# такие что X <= Y.

# Пример

# На входе:

# s = 12
# p = 27
# На выходе:

# 3 9
# Import math Library
# import math

# s = int(input('Enter + number : '))
# p = int(input('Enter * number : '))

# # c = a + b
# # d = a * b
# # e = 0

# # for a in range(1, c//2+1):
# #     for b in range(1, c//2+1):

# for a in range(1, 1000+1):
#     for b in range(1, 1000+1):
#         if s == (a + b) and p == (a * b) and a <= b:
#             print(f'{a} {b}')

# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:

# list_1 = [3, 2, 3, 4, 5]
# k = 3

# sum = 0
# i = 0
# while i < len(list_1):
#     if list_1[i] == k:
#         sum += 1
#     i += 1
# print(sum)

# Требуется найти в массиве list_1
# самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5, 6]
# k = 6
# 5

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

# res = 0
# res1 = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         res = list_1[i]
#     else:
#         if list_1[i] == k+1 or list_1[i] == k-1:
#             res1 = list_1[i]
# if k == res:
#     res = res
# else:
#     res = res1

# print(res)


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу,
# которая вычисляет стоимость
# введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Пример:

# k = 'ноутбук'
# # # 12

# # word = []
# # print(type(word))
# # k = 'lizard'
# # a = k.upper()
# # print(a)
# # k = [str(i.upper()) for i in input("Введите slovo: ")]
# print(k)
# # k = 'ноутбук'
# # k = input("Введите slovo: ").upper()
# print(type(k))
# wordsCost = 0
# # for i in k:
# #     print(i)
# #     word.append(i)
# # print(word)
# # print(type(word))

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
# print(type(wordsdict))

# data = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1,
#         "D, G, Д, К, Л, М, П, У": 2,
#         "B, C, M, P, Б, Г, Ё, Ь, Я": 3,
#         "F, H, V, W, Y, Й, Ы": 4,
#         "K, Й, Ы": 5,
#         "J, X Ш, Э, Ю": 8,
#         "Ф, Щ, Ъ Q, Z": 10
#         }
# print(type(data))

# for el in k:
#     for key in data:
#         if el.upper() in key:
#             #   if el in wordsdict:
#           # print(el)
#           # wordsCost = wordsCost + int(wordsdict.get(el))
#             wordsCost = wordsCost + int(data[key])
# print(wordsCost)


# Пересечение двух неупорядоченных наборов целых чисел

# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества
# через пробел в виде строки. ! Писать input() не надо

# var1 = '5 4'  # количество элементов первого и второго множества
# var2 = '222 8 1 345 5 99 7 9'  # элементы первого множества через пробел
# var3 = '222 8 2 99 345 4 5'  # элементы второго множества через пробел
# r2 = {int(i) for i in var2.split()}
# r3 = {int(i) for i in var3.split()}
# var4 = {}
# print(r2)
# print(r3)
# for element in r2:
#     if element in r3:
#         var4[element] = element
# print(var4)
# for el in sorted(var4):
#     print(el, end=' ')


# Черника

# В фермерском хозяйстве в Карелии выращивают чернику.
# Черника растет на круглой грядке,
# и кусты черники высажены по окружности грядки.
# Каждый куст черники имеет урожайность,
# которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена
# в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля
# и нескольких собирающих модулей.
# Каждый собирающий модуль
# может собрать ягоды с одного куста и с двух соседних кустов.
# Собирающий модуль находится перед определенным кустом,
# и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу,
# которая определит максимальное число ягод,
# которое может собрать один собирающий модуль за один заход,
# находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr,
# где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники.
# Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число -
# максимальное количество ягод,
# которое может собрать собирающий модуль,
# находясь перед некоторым кустом грядки.

# Пример использования
# На входе:

# arr = [5, 8, 6, 4, 9, 2, 7, 3]

# arr = [2, 4, 10, 4, 2]

# arr = [1001, 8, 6, 4, 2]
# # На выходе:


# data = set({})
# # print(type(arr))
# # i = 0
# # print(len(arr)+1)
# # 19
# i = 0
# if arr[i] >= 1 and arr[i] <= 1000 and len(arr) <= 1000:

#     for i in range(3):
#         # print(arr)

#         arr.insert(0, arr.pop(-1))
#         # print(arr)

#         for i in range(len(arr)-2):

#             sum = arr[i]+arr[i+1]+arr[i+2]
#         # print(sum)
#             data.add(sum)

# # print(data)

#     print(max(data))
# else:
#     print('element size >1000')

# while i <= 1000:

# if arr[i] >= 1 and arr[i] <= 1000:


# print(sum)

# arr=[1, 2, 3, 4, 5, 6, 7, 8]

# SelectionSort - from grokhing algoritms book p58

# def FindSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index


# def SelectionSort(arr):
#     resultarr = []
#     for i in range(len(arr)):
#         smallest = FindSmallest(arr)
#         resultarr.append(arr.pop(smallest))
#     return resultarr


# print(SelectionSort([31, 23, 35, 49, 50, 6, 7, 8]))


# def count(i):
#     if i <= 0:
#         return
#     print(f'i-1:{i}')
#     count(i-1)
#     print(f'i-2:{i}')


# i = 10
# count(i)

# arr = [11, 22, 31, 45]
# print(len(arr))

# print(arr)

# summ = 0


# def sum(arr):

#     if arr == []:
#         return 0
#     else:
#         print(len(arr))

#         summ = summ+sum(arr[len(arr)-1])

#         # summarr = summarr+sum(arr[len(arr)-1])

#     # return summarr


# print(sum(arr))


# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет
# оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# marks = [int(i) for i in input("Введите оценки: ").split()]
# print(*[min(marks) if i == max(marks) else i for i in marks])
# min(marks)  # -  поиск минимального числа списка
# max(marks)  # -  поиска максимального числа списка


# data = [int(i) for i in input("Введите числа: ").split()]
# print([min(data) if i == max(data) else i for i in data])

# print([min(data) if i == max(data) else data for i in data])

# for i in range(len(data)):
#     if data[i] == max(data):
#         data[i] = min(data)
# print(data)


# def maximum(data):
#     maxel = data[0]
#     for i in range(len(data)):
#         if data[i] > maxel:
#             maxel = data[i]
#     return maxel


# def minimum(data):
#     minel = data[0]
#     for i in range(len(data)):
#         if data[i] < minel:
#             minel = data[i]
#     return minel


# for i in range(len(data)):
#     print(data[i])
#     if data[i] == maximum(data):
#         data[i] = minimum(data)
# print(data)


# Задача №35. Решение в группах
# Напишите функцию, которая принимает
# одно число и проверяет, является ли
# оно простым Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1  и n(само число)
# Input: 5 Output: yes

# def is_prime(n):
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return 'no'
#     return 'yes'

# print(is_prime(int(input("Введите число: "))))


# Задача №37. Решение в группах 15 минут
# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту последовательность
# в обратном порядке. Примечание. В программе запрещается
# объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4 Output: 4 3

# N = int(input("Введите число: "))


# def recursion(n):
#     if n <= 0:
#         return "zero"

#     print(n)

#     return print(recursion(((n)+2)-1))


# print(recursion(N))
# # b = input("Введите число: ")
# c = input("Введите число: ")


# Напишите функцию f, которая на вход
# принимает два числа a и b, и возводит
# число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только
# возвращать значение.

# Пример:

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# Введите ваше решение ниже

# a = 2
# b = 3


# def f(a, b):

#     if b == 0:
#         return a**0

#     return a*f(a, b-1)


# print(f(a, b))


# def square(a, b):
#     res = 1
#     for i in range(b):
#         res = res*a
#     return res


# print(square(2, 2))


# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# sum(2, 2)
# # 4

# a = 2
# b = 6


# def sum(a, b):
#     print(f'1st - a:{a}')
#     print(f'1st - b:{b}')
#     if b == 0:
#         print(f'2nd - a:{a}')
#         print(f'2nd - b:{b}')

#         return a

#     print(f'3rd - a:{a}')
#     print(f'3rd - b:{b}')

#     return b+sum(a, b-b)


# print(sum(a, b))


# Seminar 6     ******************************************************************

# Задача №39. Решение в группах Даны два массива чисел.
# Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод: 7 3 3 2 12 3 1 3 4 2 4 12 6 4 15 43 1 15 1


# Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M -
# количество элементов во втором массиве. Затем элементы второго массива


# print([i**2 if i % 2 != 0 else 0 for i in sp])

# sp1 = [3, 1, 3, 4, 2, 4, 12]
# sp2 = [4, 15, 43, 1, 15, 1]

# print([i for i in sp1 if i not in sp2])
# print([i for i in sp1 if i not in set(sp2)])


# Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых два соседних и, при этом,
# оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


# def find_champ(sp, index):
#     if sp[index] > sp[index+1] and sp[index] > sp[index-1]:
#         return True
#     return False


# def find_champ2(sp, index):
#     if sp[index] > sp[(index+1) % len(sp)] and sp[index] > sp[index-1]:
#         return True
#     return False


# sp1 = [1, 2, 3, 4, 5]  # 0

# print(sum([1 for i in range(len(sp1)-1) if find_champ(sp1, i)]))

# sp1 = [1, 5, 1, 5, 1]  # 2

# print(sum([1 for i in range(len(sp1)-1) if find_champ(sp1, i)]))

# # закольцовываем список

# sp1 = [1, 2, 3, 4, 5]  # 1

# print(sum([1 for i in range(len(sp1)) if find_champ2(sp1, i)]))


# Задача №43. Решение в группах Дан список чисел. Посчитайте,
# сколько в нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа
# списка находятся на разных строках. Ввод: Вывод: 1 2 3 2 3 2


# sp = [5, 6, 7, 6, 7, 7, 7]
# for i in sp:
#     print(sp.count(i)//2)

# # print(sum([i//2 for i in set(sp) if sp.count(i) // 2 == 0]))

# print(sum([sp.count(i)//2 for i in set(sp)]))

# print(set(sp))


# sp1 = [1, 2, 3, 4, 5]  # 1

# sp = [1, 2, 3, 2, 3, 3, 3, 3]  # 2

# print(sp.count(3))
# print(sum([1 for i in sp if sp.count(i) % 2 == 0]) / 2)
# print(sum([sp.count(i) // 2 for i in set(sp)]))


# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое
# из которых не превосходит k. Программа получает на вход одно натуральное число k,
# не превосходящее 105. Программа должна вывести  все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает). Ввод: Вывод: 300 220 284


# def summa_dels(num):
#     res = 0
#     for i in range(1, num):
#         if num % i == 0:
#             res += i
#     return res


# k = int(input("До какого числа будем анализировать "))

# res = []

# for m in range(1, k+1):
#     n = summa_dels(m)
#     if summa_dels(n) == m and n > m:
#         res.append((n, m))

# print(res)


# print([(m, n) for m in range(1, k+1) if summa_dels(n := summa_dels(m)) == m and n > m])

# print([(m, n) for m in range(1, k+1) if summa_dels(n := summa_dels(m)) == m and n > m])


# print([(m, summa_dels(m)) for m in range(1, k+1)
#       if summa_dels(summa_dels(m)) == m and summa_dels(m) > m])


# def del_sum(num: int) -> int:
#     count = 1
#     for i in range(2, int(num**0.5)):
#         if num % i == 0:
#             count += (i + num//i)
#     return count


# def friendly_num(k: int) -> set:
#     set_num = {}
#     for i in range(220, k):
#         del_num = del_sum(i)
#         if (i == del_num) or (i in set_num or del_num in set_num):
#             continue
#         if del_sum(del_num) == i:
#             set_num.update({i: del_num})
#     return set_num


# ***************************************************************************************
# семинары Урок 6. Повторение списков


# Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M -
# количество элементов во втором массиве. Затем элементы второго массива

# sp1 = [3, 1, 3, 4, 2, 4, 12]
# sp2 = [4, 15, 43, 1, 15, 1]

# print([i for i in sp1 if i not in sp2])
# print([i for i in sp1 if i not in set(sp2)])

# Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых два соседних и, при этом,
# оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# def find_champ(sp, index):
#     if sp[index] > sp[index+1] and sp[index] > sp[index-1]:
#         return True
#     return False

# def find_champ2(sp, index):
#     if sp[index] > sp[(index+1) % len(sp)] and sp[index] > sp[index-1]:
#         return True
#     return False


# sp1 = [1,2,3,4,5]  # 0

# print(sum([1 for i in range(len(sp1)-1) if find_champ(sp1,i) ]))

# sp1 = [1,5,1,5,1] # 2

# print(sum([1 for i in range(len(sp1)-1) if find_champ(sp1,i)  ]))

# #закольцовываем список

# sp1 = [1,2,3,4,5]  # 1

# print(sum([1 for i in range(len(sp1)) if find_champ2(sp1,i) ]))

# Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

# sp = [1,2,3,2,3,3,3,3] #2

# # print(sp.count(3))
# # print(sum([1 for i in sp if sp.count(i) % 2 == 0]) / 2)
# print(sum( [sp.count(i) // 2 for i in set(sp) ]  ))


# Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 10000.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить
# по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает). Ввод: 300 Вывод:  220 284

# def summa_dels(num):
#     res = 0
#     for i in range(1,num):
#         if num % i == 0:
#             res += i
#     return res


# print(test := 5)

# print(test + 10)

# k = int(input("До какого числа будем анализировать "))

# res = []

# for m in range(1, k+1):
#     n = summa_dels(m)
#     if summa_dels (n) == m and n > m:
#         res.append( (n,m) )

# print(res)

# print(res2 := [ (m,n)  for m in range(1, k+1) if summa_dels (n := summa_dels(m)) == m and n > m  ])


# print( [ (m,summa_dels(m))  for m in range(1, k+1) if summa_dels (summa_dels(m)) == m and summa_dels(m) > m  ])
# print(res2)


# ***********************************************


# Определить индексы элементов массива
# (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1
# и границы диапазона в виде чисел min_number, max_number.

# Пример

# На входе:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10


# ([print(i) for i in range(len(list_1))if list_1[i] >= min_number and list_1[i] <= max_number])


# Арифметическая прогрессия
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент a1 , разность
# d и количество элементов n будет задано
# автоматически. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.

# Пример
# На входе:
# a1 = 2
# d = 3
# n = 4
# # На выходе:
# # 2
# # 5
# # 8
# # 11


# a = [((a1 + (n-1-i) * d)) for i in range(0, n)]
# a.reverse()
# for i in a:
#     print(i)


# **********************************************
# Урок 4. Функции высшего порядка, работа с файлами  (лекции)

# list = [1, 2, 3, 5, 8, 15, 23, 38]

# list1 = []
# # print(len(list1))

# print([list1.append((el, el**2)) for el in list if el % 2 == 0])
# print(list1)


# def evenpairs(list):
#     for el in list:
#         if el % 2 == 0:
#             list1.append((el, el**2))
#     return list1


# print(evenpairs(list))


# reduce , enumerate

# Ниже представлен пример лямбда-функции,
# удваивающей вводимое значение.

# double = lambda x: x*2
# print(double(5))
# Вывод:
# 10
# В вышеуказанном коде
# lambda x: x*2 — это лямбда-функция.
# Здесь x — это аргумент,
# а x*2 — это выражение,
# которое вычисляется и возвращается.


# ************************************************


# **********************************
# семинары  Урок 7. Функции высшего порядка


# Задача №47.
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation=lambda x: x * 1
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# # # или любой другой список
# transormed_values = list(map(lambda x: x * 1, values))
# print(transormed_values)


# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна


# Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод: 2.5 10


# def find_farthest_orbit(orbits):
#     squares_list = [(i[0] != i[1]) * i[0] * i[1] for i in orbits]
#     return orbits[squares_list.index(max(squares_list))]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# print(find_farthest_orbit(orbits))


# Задача №51. Решение в группах Напишите функцию
# same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой
# характеристики, и возвращают True, если это так. Если
# значение характеристики для разных объектов отличается
# - то False. Для пустого набора объектов, функция должна
# возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Ввод:  values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
#           else: print(‘different’)

# Вывод:  same

# def same_by(characteristic, objects):
#     return len(set(list(map(characteristic, objects)))) in (0, 1)

# values = [3, 6, 9, 12, 15, 16]
# if same_by(lambda x: x % 3, values):
#     print('same')
# else:
#     print('different')

# *****************************************

# my_nums = (10, 5, 100, 0)
# print(type(my_nums))
# # my_nums[1] = 7
# del my_nums[1]


# mult = lambda a,b : a*b
# print(mult(10,5))


# def greeting(greet):
#     return lambda name: f" {name}, {greet} !"

# privet = greeting('privet')
# morning_greeting = greeting("Good Morning")
# print(morning_greeting('Bogdan'), ('good'), ('work'))
# print(morning_greeting(1))
# print(privet('Eldar'))


# evening_greeting = greeting("Good Evening")
# print(evening_greeting('Bogdan'))

# ****************************************


# print_operation_table

# Напишите функцию print_operation_table
# (operation, num_rows, num_columns), которая
# принимает в качестве аргумента функцию, вычисляющую
# элемент по номеру строки и столбца.
# По умолчанию номер столбца и строки = 9.

# Аргументы num_rows и num_columns указывают
# число строк и столбцов таблицы, которые
# должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется
# любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# Между элементами должен быть 1 пробел,
# в конце строки пробел не нужен.

# Пример

# На входе:

# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:

# 1 2 3
# 2 4 6
# 3 6 9


# Задача 34:
# Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать
# программу. Винни-Пух считает, что ритм есть, если число
# слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами. Фразы отделяются
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в
# программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом
# все не в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам


# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'
# Ожидаемый ответ:Количество фраз должно быть больше одной!

# stroka = 'пара-ра-рам рам-пам-папам-па-дам па-ра'
# Ожидаемый ответ:Пам парам

# stroka = 'со-лнце-гре-ет ве-сной'
# Ожидаемый ответ:Пам парам

# stroka = 'Пух'
# Ожидаемый ответ:Количество фраз должно быть больше одной!

# stroka = 'по-русски говорят'
# Ожидаемый ответ:Парам пам-пам

# stroka = 'мо-локо и мёд'
# Ожидаемый ответ:Пам парам

# stroka = 'как ве-тер сме-ёт лис-ти'
# Ожидаемый ответ:Пам парам

#  Гласных букв - десять: «а» «у» «о» «и» «э» «ы» «я» «ю» «е» «ё».

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# stroka = 'пара-ра-рам рам-пам-папам-па-дам па-ра'

# def RythmCount(stiwok):
#     # print(f'len = {len(str.split())}')
#     data = []
#     if len(stiwok.split()) <= 1:
#         print('Количество фраз должно быть больше одной!')
#     else:
#         # print(str)
#         for s in stiwok.split():
#             # print(s)

#            # temp = []
#            # temp1 = list(map(s.count, ['а', 'е', 'о', 'ю',
#            #                            'у', 'э', 'ё', 'и', 'ы', 'я']))
#            # temp.append(temp1)
#            # print(f'temp{temp}')

#             res1 = sum(
#                 map(s.count, ['а', 'е', 'о', 'й', 'ю', 'у', 'э', 'ё', 'и', 'ы', 'я']))
#             # print(res1)
#             data.append(res1)
#         if len(set(data))==1:
#         # if min(data) == max(data):
#         # if count(set(data)) >  1
#         # if min(data) % 2 == 0 or sum(data) % 2 == 0 :
#             print('Парам пам-пам')
#         else:
#             print('Пам парам')

# RythmCount(stroka)


# stroka = 'пара-ра-рам рам-пам-папам-па-дам па-ра'


# def RythmCount(stiwok):
#     data = []
#     if len(stiwok.split()) <= 1:
#         print('Количество фраз должно быть больше одной!')
#     else:
#         for s in stiwok.split():
#             res1 = sum(
#                 map(s.count, ['а', 'е', 'о', 'й', 'ю', 'у', 'э', 'ё', 'и', 'ы', 'я']))
#             data.append(res1)
#         if len(set(data)) == 1:
#             print('Парам пам-пам')
#         else:
#             print('Пам парам')


# RythmCount(stroka)


# Задача 36:
# Напишите функцию print_operation_table
# (operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например,
# у операции умножения.
# Ввод:
# Вывод:
# print_operation_table(lambda x, y: x * y)

# 1         2         3        4        5       6
# 2         4         6        8       10      12
# 3         6         9       12       15      18
# 4         8        12       16       20      24
# 5        10        15       20       25      30
# 6        12        18       24       30      36


# https://colab.research.google.com/drive/1nfapiAATvu4A-xpJPxEB1KuyKivpkH-w?usp=sharing


# Определить среднюю стоимость дома

# Дан файл california_housing_train.csv.
# Определить среднюю стоимость дома ,
# где количество людей от 0 до 500
# (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

# Введите ваше решение ниже

# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')
# df.head() # первые 5 строк

# avg=df[(df['population'] > 0) & (df['population']<= 500) ]['median_house_value'].mean()

# avg=df.loc[(df['population'] > 0) & (df['population'] <= 500)], df['median_house_value'].median

# df[(df['population'] > 0) & (df['population']<= 500) ]['median_house_value'].median()


# Максимальная households

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной
# "households" в зоне минимального
# значения переменной min_population
# и сохраните это значение в переменную
# max_households_in_min_population.
# Используйте модуль pandas.

# Введите ваше решение ниже

# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')
# # df.head() # первые 5 строк
# # df[df['population'] == df['population'].min()] ['households'].max()
# max_households_in_min_population=df[df['population'] == df['population'].min()] ['households'].max()

#

#

#


#  #   Генераторы

#  Вывести числа 1 списка, которых нет во 2-ом

# sp1 = [3, 1, 3, 4, 2, 4, 12]
# sp2 = [4, 15, 43, 1, 15, 1]

# print([i for i in sp1 if i not in sp2])

# print([i for i in sp1 if i not in set(sp2)])


#  # Найти число в списке, которое одновременно больше Обеих соседних

# sp = [1, 5, 1, 5, 1, 2, 3, 4, 5, 4]
# sp = [1, 2, 3, 4, 5]


# print(sum([1 for i in range(len(sp)-1) if sp[i] > sp[i+1] and sp[i] > sp[i-1]]))


# def MaxDigit(sp, index):
#     if sp[index] > sp[index+1] and sp[index] > sp[index-1]:
#         return True
#     return False

# print(sum([1 for i in range(len(sp)-1) if MaxDigit(sp, i)]))

# #  loop the list -  закольцовываем список для index+1

#  #   чтобы в списке  sp = [1, 2, 3, 4, 5],определить число 5 ,
# как большее между 1-м элементом и предпоследним элементом массива

# sp = [1, 5, 1, 5, 1, 2, 3, 4, 5, 4]
# sp = [1, 2, 3, 4, 5]


# def MaxDigit(sp, index):
#     if sp[index] > sp[(index+1) % len(sp)] and sp[index] > sp[index-1]:
#         return True
#     return False


# print(sum([1 for i in range(len(sp)) if MaxDigit(sp, i)]))

# sp = [1, 2, 3, 2, 3, 2, 3, 1, 2, 3, 2, 1]


# print(sum([1/2 for i in sp if sp.count(i) > 1])//2)  # ne pravilnoe

# print(sum([sp.count(i)//2 for i in set(sp)]))


# Задача


# print_operation_table


# Напишите функцию print_operation_table(operation,
# num_rows, num_columns),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# По умолчанию номер столбца и строки = 9.

# Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# Пример

# На входе:


# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:


# 1 2 3
# 2 4 6
# 3 6 9

# def operation(x, y):
#     return lambda x, y: x * y


num_rows = 3
num_columns = 3


def print_operation_table(function, num_rows, num_columns):
    massive = [[]]
    for i in range(1, num_rows+1):
        massive.append(i)
        for j in range(1+num_columns+1):
            massive.append(j)
            massive[i][j] = 123
            # massive[i] = 15
    return print(massive)


print_operation_table(lambda x, y: x * y, 3, 3)

x, y = 5, 3
array = [[0 for j in range(y)] for i in range(x)]
print(array)

# def print_operation_table(function, rows=9, cols=9):

#     if rows <= 2 or cols <= 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:

#         arr = [[function(j, i) for i in range(1, rows+1)]
#                for j in range(1, cols+1)]
#         for rows in arr:
#             print(" ".join([str(el) for el in rows]))

# print_operation_table(lambda x, y: x * y, 9, 9)

# def operation(x, y):
#     return lambda x, y: x * y
# a = operation(3, 3)

# def function(x, y):
#     return x * y

# def arr_el(count):
#     count = range(1, count)
#     return count

# def print_operation_table(function, num_rows, num_columns):

#     arr = [[function(num_rows, num_columns) for i in range(1, num_rows)]
#            for j in range(1, num_columns)]
#     # print(arr)
#     for row in arr:
#         print(*row)
#     print()

# print_operation_table(lambda x, y: x * y, 9, 9)

# def print_operation_table1(function, num_rows, num_columns):
#
#     # arr = [[function(j, i) for i in range(1, num_rows-1)]
#     #        for j in range(1, num_columns-1)]

#     for i in range(1, num_rows-2):
#         print()
#         for j in range(1, num_columns-2):
#  print(arr[i][j], end=" | ")

# print_operation_table(lambda x, y: x * y, 3, 3)

# def print_operation_table(function, rows=9, cols=9):

#     if rows <= 2 or cols <= 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:

#         arr = [[function(j, i) for i in range(1, rows+1)]
#                for j in range(1, cols+1)]
#         for rows in arr:
#             print(" ".join([str(el) for el in rows]))

# for row in arr:
#     print(*"".join([str(row)]).split(","))
# print(str(row).split('|'))

# for i in range(rows):
#     print()
#     for j in range(cols):
#         print(arr[j][i], end='')

# print_operation_table(lambda x, y: x * y, 3, 3)

# print_operation_table(lambda x, y: x + y, 4, 4)

# print_operation_table(lambda x, y: x - y, 5, 5)

# print_operation_table(lambda x, y: x * y, 1, 2)

# print_operation_table(lambda x, y: x / y, 4, 4)

# print_operation_table(lambda x, y: x * y)

# Задача 49 найти дальнюю орбиту, найти максимальное произведение не одинаковых чисел

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits_list):
#     max_res = []
#     for orbits in orbits_list:
#         # print(orbits)
#         max_res.append(orbits[0]*orbits[1])
#         if orbits[0] != orbits[1] and orbits[0]*orbits[1] == max(max_res):
#             index = max_res.index(max(max_res))
#     return orbits_list[index]

# print(*find_farthest_orbit(orbits))

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print(''.join(f'{e:<4}' for e in answer))

# print_operation_table(lambda x, y: x * y)

# Задача. В списке хранятся числа.
# Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = (1, 2, 3, 5, 8, 15, 23, 38)
# list = []
# for i in data:
#     if i % 2 == 0:
#         list.append((i, i**2))
# print(*list)

# numbers = list(map(int, data))
# print(numbers)

# numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbers)

# numbers = list(map(lambda x: (x, x**2), numbers))
# print(*numbers)

# numbers = list(map(lambda x: (x, x**2), (filter(lambda x: x % 2 == 0, data))))
# print(*numbers)

#

# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

# n = int(input("speed : "))
# m = int(input("distance : "))

# res = (n+m-1)//n
# print(res)

# 750//700=1
# 700//700=1
# 700-1//700=0
# 700+700//700+1=1 - отнимаем единицу,
# чтобы если расстояние равно скорости машины в день,
# при целочисленном делении мы не получали ответ 2

# distance = int(input("Enter distance : "))
# speed = int(input("Enter speed : "))

# time = (distance-1)//speed + 1
# print(time)

# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = 20
# b = 21
# c = 22

# # res = a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2

# res = (a+b+c)//2 + (a % 2+b % 2+c % 2)
# print(res)

# rooms = int(input("Enter classes count: "))

# for i in range(1, rooms+1):
#     res = 0
#     classes = int(input("Enter  class size: "))
#     for j in range(classes, classes+i):
#         sum = (j//2+(j % 2))
#         res = res+sum
#         print(sum)
#     print(res)

# a = (21//2)+(21 % 2)
# print(a)

# Задача №7. Решение в группах Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016 Output: YES

# n = 2024

# for n in range(1950, 2099):

#     if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#         print(f"the          {n} year is leap")
#     else:
#         print(f"the {n} year is standart")

#
#
#

# Урок 8. Работа с файлами
# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
# Формат сдачи: ссылка на свой репозиторий или pull request на изначальный репозиторий.
