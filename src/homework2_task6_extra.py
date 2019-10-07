'''Определите, является ли число палиндромом.
Число положительное целое, произвольной длинны.
'''
num = input('Enter number ')
lst1 = list(num)
lst2 = lst1[::-1]
if lst1 == lst2:
    print(num, 'is palindrom')
else:
    print(num, 'isnt palindrom')