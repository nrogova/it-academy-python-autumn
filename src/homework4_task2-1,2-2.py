"""2.1 Use a list comprehension to construct
list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""
lst1 = [x+y for x in ['a', 'b'] for y in ['b', 'c', 'd']]
print(lst1)

"""2.2 Use a slice on the above list to construct
the list ['ab', 'ad', 'bc'].
"""
lst2 = lst1[::2]
print(lst2)
