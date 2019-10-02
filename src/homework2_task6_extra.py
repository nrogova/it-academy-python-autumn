'''
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).  Число положительное целое, произвольной длинны.
'''
#variables
num = int(input('Enter number '))
#logic
if str(num) == str(num)[::-1]:
    print('Palindrom')

else:
    print('Not palindrom')