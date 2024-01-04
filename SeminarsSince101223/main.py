

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

# Задача 1

# n = int(input("Сколько за день проезжает машина? - "))
# m = int(input("Общее расстояние: "))
# # 750 : 700 = 1(ост. 50) + 1
# # 2100 : 700 = 3 (ост. 0) + 0
# print((m + n - 1) //  n)
# (m + n - 1) // n
# (1401 + 700 - 1) // 700 = 3
# print(-12 % 5) # 15 - 12 = 3
# print(-14 % 6) # 18 - 14
# print(-7 % 3) # 9 - 7







*/








# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2





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

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

# data = [str(i) for i in input("Введите числа: ").split()]
# print(data)


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


# n = int(input("Введите кол-во элементов списка: "))
# data = []
# for i in range(n):
#     data.append(str(input("Введите число: ")))
#     # insert(position, element)
# print(data)


# print(" !! ".join(data))

# A, E, I, O, U, L, N, S, T, R – 1

# data = [{"A, E, I, O, U, L, N, S, T, R": "1"}, {"V": "S002"}, {"VI": "S001"},
#         {"VI": "S005"}, {"VII": "S005"}, {"V ": "S009"}, {"VIII": "S007 "}]

# print(data[0]["A, E, I, O, U, L, N, S, T, R"])

wordsCost = 0
wordsdict = {}
# print(type(wordsdict))

k = [str(i.capitalize()) for i in input("Введите числа: ").split()]
print(k)

wordsdict = {"A": "1", "E": "1", "O": "1", "U": "1", "L": "1", "N": "1",
             "S": "1", "T": "1", "R": "1", "D": "2", "G": "2", "B": "3",
             "C": "3", "M": "3", "P": "3", "F": "4", "H": "4", "V": "4",
             "W": "4", "Y": "4", "K": "5", "J": "8", "X": "8", "Q": "10", "Z": "10",

             "А": "1", "В": "1", "Е": "1", "И": "1", "Н": "1", "О": "1",
             "Р": "1", "С": "1", "Т": "1",
             "Д": "2", "К": "2", "Л": "2", "М": "2", "П": "2", "У": "2",
             "Б": "3", "Г": "3", "Ё": "3", "Ь": "3", "Я": "3",

             "Й": "4", "Ы": "4",

             "Ж": "5", "З": "5", "Х": "5", "Ц": "5", "Ч": "5",
             "Ш": "8", "Э": "8", "Ю": "8",
                            "Ф": "10", "Щ": "10", "Ъ": "10"

             }
# print(type(wordsdict))
for el in k:
    if el in wordsdict:

        # print(wordsdict.get(el))

        temp = int(wordsdict.get(el))
        # print(temp)

        wordsCost = wordsCost + temp


print(wordsCost)


# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.


# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
