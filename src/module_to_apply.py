"""task 2.1 Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество L товара
Посчитайте общую цену в рублях и копейках за L товаров.
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


def price_counter():
    userM = int(input('Сколько рублей стоит товар? '))
    userN = int(input('Сколько копеек стоит товар? '))
    userL = int(input('Какое количество товара? '))

    countM = userM * userL
    countN = userN * userL
    moreN = countN % 100
    moreM = countN // 100
    countMN = countM + moreM

    if countN >= 100:
        print('Общая цена: ', int(countMN), ' рублей ', int(moreN), ' копеек.')
    else:
        print('Общая цена: ', int(countM), ' рублей ', int(countN), ' копеек.')


""" Task 2.2 Given an integer, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""


def wierd_func():
    n = int(input('Enter number '))
    if n % 2 != 0:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')


"""Task 2.3 Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers.
The third line contains the product of the two numbers.
"""


def arifm_func():
    a = int(input('Enter a '))
    b = int(input('Enter b '))

    print(a + b)
    print(a - b)
    print(a * b)


""" Task 2.4 Read two integers and print two lines.
The first line should contain integer division.
The second line should contain float division.
You don't need to perform any rounding or formatting operations.
"""


def devision_func():
    a = int(input('Enter a '))
    b = int(input('Enter b '))

    print(a // b)
    print(a / b)


"""Task 2.5 Read an integer N.
For all non-negative integers print i**2.
"""


def square_cycle():
    N = int(input('Enter N '))

    for i in range(N):
        print(i ** 2)


"""Task 2.6 Определите, является ли число палиндромом.
Число положительное целое, произвольной длинны.
"""


def palindr():
    num = input('Enter number ')

    lst1 = list(num)
    lst2 = lst1[::-1]

    if lst1 == lst2:
        print(num, 'is palindrom')
    else:
        print(num, 'is not palindrom')


""" Task 4.1.FizzBuzz: Write program that prints numbers from 1 to 100,
but for multiples of three print “Fizz” instead of number
and for multiples of five print “Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”.
"""


def fuzz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


"""Task 4.2 Use a list comprehension to construct
list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Use a slice on the above list to construct
the list ['ab', 'ad', 'bc'].
Use a list comprehension
to construct list ['1a', '2a', '3a', '4a'].
"2.4 Simultaneously remove element '2a'
from the above list and print it.
2.5 Copy the above list and add '2a' back into the list
such that the original is still missing it.
"""


def list_compr():
    lst1 = [x+y for x in ['a', 'b'] for y in ['b', 'c', 'd']]
    print(lst1)

    lst2 = lst1[::2]
    print(lst2)

    lst3 = [str(el) + 'a' for el in range(1, 5)]
    lst3.pop(1)
    print(lst3)
    lst4 = lst3[:]
    lst4.insert(1, '2a')
    print(lst4)


"""Task 4.3 Create the list ['a', 'b', 'c'],
then create a tuple from that list.
Create the tuple ('a', 'b', 'c'),
then create a list from that tuple.
Make the following instantiations simultaneously:
a = 'a', b=2, c='gamma'. (That is, in one line of code).
reate tuple containing just single element
which in turn contains three elements 'a', 'b', and 'c'.
Verify that length is actually 1 by using len() function.
"""


def list_practice():
    lst = ['a', 'b', 'c']
    tpl = tuple(lst)
    print(tpl, type(tpl))

    tpl1 = ('a', 'b', 'c')
    lst1 = list(tpl1)
    print(lst1, type(lst1))

    a, b, c = 'a', 2, 'gamma'
    print(a, b, c)

    tpl2 = ('a', 'b', 'c')
    tpl3 = (tpl2, )
    print(tpl3, len(tpl3))


""" Task 5.1.1 Define a dict comprehension which returns a dictionary
where the keys are numbers between 1 and n (both included)
and the values are square of keys. n – function argument. Default is 20.
"""


def dct_n(n=20):
    dct = {a: a**2 for a in range(1, n + 1)}
    print(dct)


"""Task 5.1.2 Define a code which count and return numbers
of each character in count_me_string argument.
Example:
If the following string is given as argument to the function:
abcdefgabc
Then, the return result of the function should be:
{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
"""


def count_me():
    count_me_string = input('Please, enter string: ')
    dct = {}
    for i in count_me_string:
        dct[i] = dct.get(i, 0) + 1
    print(dct)


"""Task 5.2. Дан текст (строк может быть много, разделенных \n).
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.
"""


def often_text():
    text = input('Please enter text: ')
    lst = text.split()

    dct = {}
    for i in lst:
        dct[i] = dct.get(i, 0) + 1

    max_value = max(dct.values())
    most_often = [k for k, v in dct.items() if v == max_value]

    print(min(most_often))


"""Task 5.3. Задача Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные: Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов —
названия каких-то M городов,
перечисленных выше. Выходные данные: Для каждого из запроса
в котором находится данный город.
Примеры:
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""


def cities_countries():
    num_co = int(input('Enter number of countries: '))
    dct = {}
    for i in range(num_co):
        country, *city = input('Enter country and cities: ').split()
        for el in city:
            dct[el] = country

    lst_ci = []
    num_ci = int(input('Enter number of cities: '))
    for i in range(num_ci):
        cities = input('Enter cities: ')
        lst_ci.append(cities)
    for el in lst_ci:
        print(dct.setdefault(el))


"""Task 5.4 Даны два списка чисел. Посчитайте, сколько чисел содержится
одновременно как в первом списке, так и во втором.
"""


def set_joint():
    a = set(input('Enter first set of numbers separated by spaces: ').split())
    b = set(input('Enter second set of numbers separated by spaces: ').split())
    print('Quantity of joint numbers: ', len(a & b))


"""Task 5.5 Даны два списка чисел. Посчитайте, сколько чисел
входит только в один из этих списков.
"""


def set_differ():
    a = set(input('Enter first set of numbers separated by spaces: ').split())
    b = set(input('Enter second set of numbers separated by spaces: ').split())
    print('Quantity of different numbers: ', len(a ^ b))
