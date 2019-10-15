"""Task 4 Даны два списка чисел. Посчитайте, сколько чисел содержится
одновременно как в первом списке, так и во втором.
"""
a = set(input('Enter first set of numbers separated by spaces: ').split())
b = set(input('Enter second set of numbers separated by spaces: ').split())
print('Quantity of joint numbers: ', len(a & b))
