"""2.3 Use a list comprehension
to construct list ['1a', '2a', '3a', '4a'].
"""
lst3 = [str(el) + 'a' for el in range(1, 5)]

"""2.4 Simultaneously remove element '2a'
from the above list and print it.
"""
lst3.pop(1)
print(lst3)

"""2.5 Copy the above list and add '2a' back into the list
such that the original is still missing it.
"""
import copy
lst4 = copy.copy(lst3)
lst4.insert(1, '2a')
print(lst4)
