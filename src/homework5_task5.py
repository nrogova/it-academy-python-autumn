"""Task 5. Даны два списка чисел. Посчитайте, сколько чисел
входит только в один из этих списков.
"""
a = set(input('Enter first set of numbers separated by spaces: ').split())
b = set(input('Enter second set of numbers separated by spaces: ').split())
print('Quantity of different numbers: ', len(a ^ b))
