"""Task 3. Задача Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные: Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные: Для каждого из запроса выведите название страны,
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
