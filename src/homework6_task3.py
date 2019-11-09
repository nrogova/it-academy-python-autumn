"""Task 3. Реализовать функцию get_ranges,
которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""
# I cannot do this task by myself, so ask Nastya to help me and explain.


def get_ranges(lst):
    rang = ""
    for el in range(len(lst) - 1):
        if lst[el] + 1 == lst[el + 1] and lst[el] - 1 != lst[el - 1]:
            rang += '{}-'.format(lst[el])
        elif lst[el] + 1 != lst[el + 1]:
            rang += '{},'.format(lst[el])
    rang += str(lst[-1])
    print(rang)


lst = [0, 1, 2, 3, 4, 7, 8, 10]


get_ranges(lst)
