"""
"""

# import abc


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# town = input("Enter your town: ")
# print(name,age,town)
# print(name.find('a'))
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
# print(import datetime)


# import datetime


# def time(self: datetime.
#          datetime(year=2023, month=03, day=22,
#                   hour=07, minute=27, second=10)):

#     print(datetime.date(),
#           datetime.time())


# time

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
number = int(input("enter number :"))

if number % 2 == 0:

    print(number, (' четное число'))
else:
    print(number, (' нечетное число'))

    # else:

#     print(number, ('четное число'))


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

# to reverse array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_new = []
index = 0
size = len(numbers)
new_symbol = 0
while index < size:
    print('new_symbol before action', new_symbol)
    new_symbol = numbers[(len(numbers)-1)-index]
    print('new_symbol after action', new_symbol)
    array_new.append(new_symbol)
    index = index+1
    # print(new_symbol)
print(numbers)
print(array_new)
"""

"""

# to find indexes of max and min values
# input(int(numbers=[]))
numbers = [1, 20, 3, 45, 55, 2, 10]
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

# to find summ of values excluding of max and min values

numbers = [3, 5, 7, 1, 4, 5, 6, 7, 8, 9, 1, 5, 6, 7, 8, 11]
size = len(numbers)
index = 0
i_min = 0
i_max = 0
min = numbers[0]
max = numbers[0]
old_max = 0
tempsum = 0
sum = 0
arrayoldmax = []
arrayoldmin = []
array3 = []
old_min = 0
secmin = 0
secmax = 0
arraysecmin = []
arraysecmax = []


for index in range(size):
    #     print('min', min)
    #     print('max', max)
    # print('the value of the index', index, 'equals ', numbers[index])
    if numbers[index] == min:
        secmin = numbers[index]
        arraysecmin.append(secmin)
    if numbers[index] == max:
        secmax = numbers[index]
        arraysecmax.append(numbers[index])

    if numbers[index] < min:
        old_min = min
        arrayoldmin.append(old_min)
        min = numbers[index]
        i_min = index
        print('min is', min)
    if numbers[index] > max:
        old_max = max
        print('old_max is', old_max)
        arrayoldmax.append(old_max)
        max = numbers[index]
        i_max = index
        print('max is', max)
    if old_max > min and old_max < max:
        # print('tempsum index equals', index)
        # tempsum = tempsum+numbers[index]
        array3.append(numbers[index])
    print('min', min)
    print('max', max)
    # print('tempsum', tempsum)
index = index+1
sum = tempsum-max
print('sum', sum)
print(arrayoldmax)
print(arrayoldmin)
print(array3)
print(arraysecmin)
print(arraysecmax)
# print(array_new2)
# print('min index=', n_min, 'min value=', min)
# print('max index=', n_max, 'max value=', max)




# n = [0, -1, 5, -2, 3]
n = [0, -1, 5, 3]
print(n)

left = 0  # index equals 0   - from where we will start
right = len(n) - 1  # size of array minus 1 - where we will finish
print('size-1 is', right)

while left <= right:  # while 0 < or  equals  size of the array minus 1
    for i in range(left, right, 1):  # for i variable in range  ->
        #                               ->        from starting "left" - index - to "right" - end of the size
        print('"i" in 1st for is', i)
        if n[i] > n[i + 1]:  # if element with index - i - is more than element with index i+1
            # do this line - reverse places of n[i],n[i+1], to n[i+1],n[i]
            n[i], n[i + 1] = n[i + 1], n[i]
    right -= 1   # count minus -1 from the end of the array - right -1
    print('right', right)

    # for i variable in range  from  end of the array "right" -size
    # #             to  starting "left" - index, with step minus one element  " -1"
    for i in range(right, left, -1):
        print(' "i" in 2nd for is', i)
        if n[i - 1] > n[i]:  # if element with index -1 - n[i-1] - is more than element with index n[i]
            n[i], n[i - 1] = n[i - 1], n[i]  # do this line-
            #   reverse elements n[i],and one element back  - n[i-1] to n[i-1], n[i]
    left += 1  # count plus one element -(one index )from right end to the left
    print('left', left)

print(n)


# def print_name(name):
#     print('eldar')


# print_name('name')
# print_name = 10

# print(print_name)




# Here’s an echo server with the asyncio API:

#!/usr/bin/env python




from websockets.sync.client import connect
import asyncio
from websockets.server import serve
async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

# Here’s how a client sends and receives messages with the threading API:

#!/usr/bin/env python


# def hello():
#     with connect("ws://localhost:8765") as websocket:
#         websocket.send("Hello world!")
#         message = websocket.recv()
#         print(f"Received: {message}")


# hello()





# Задача 1  За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2

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




Задача №3. Общее обсуждение
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32

a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2





Вагоны в электричке пронумерованы натуральными числами, 
начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
 это зависит от того, в какую сторону едет электричка). 
 В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
 что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
   Напишите программу, которая будет это делать или сообщать, 
   что без дополнительной информации это сделать невозможно. 

   j+i-1

   if j=i  это сделать невозможно. 





   Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES


if (n%4&&n%400 ==0) 
else n%100 !=0


year = int(input("Введите год: "))
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


"""
"""
"""

# n = int (input("Enter a number"))
# print(        n%4==0 and n%400 ==0  or n%100 !=0        )


# n = int (input("Enter a number"))
# print(        n%4==0 and n%400 ==0  or n%100 !=0        )








