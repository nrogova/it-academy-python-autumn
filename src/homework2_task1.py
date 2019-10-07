'''Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество L товара.
Посчитайте общую цену в рублях и копейках за L товаров.
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек.
'''

userM = int(input('Сколько рублей стоит товар? '))
userN = int(input('Сколько копеек стоит товар? '))
userL = int(input('Какое количество товара? '))

countM = userM * userL
countN = userN * userL
moreN = countN % 100
moreM = countN // 100
countMN = countM + moreM

if countN >= 100:
    print(int(userL), ' единиц(ы) товара стоят ', int(countMN), ' рублей ', int(moreN), ' копеек.')
else:
    print(int(userL), ' единиц(ы) товара стоят ', int(countM), ' рублей ', int(countN), ' копеек.')