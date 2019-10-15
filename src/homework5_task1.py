""" Task1. Define a dict comprehension which returns a dictionary
where the keys are numbers between 1 and n (both included)
and the values are square of keys. n – function argument. Default is 20.
"""
n = 20


def dct_n(n):
    dct = {a: a**2 for a in range(1, n + 1)}
    return dct


print(dct_n(n))

"""Define a code which count and return numbers
of each character in count_me_string argument.
Example:
If the following string is given as argument to the function:
abcdefgabc
Then, the return result of the function should be:
{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
"""
count_me_string = input('Please, enter string: ')
dct = {}
for i in count_me_string:
    dct[i] = dct.get(i, 0) + 1
print(dct)
