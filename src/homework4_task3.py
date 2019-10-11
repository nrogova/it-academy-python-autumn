"""3.1 Create the list ['a', 'b', 'c'],
then create a tuple from that list.
"""
lst = ['a', 'b', 'c']
tpl = tuple(lst)
print(tpl, type(tpl))

"""3.2 Create the tuple ('a', 'b', 'c'),
then create a list from that tuple.
"""
tpl1 = ('a', 'b', 'c')
lst1 = list(tpl1)
print(lst1, type(lst1))

"""3.3 Make the following instantiations simultaneously:
a = 'a', b=2, c='gamma'. (That is, in one line of code).
"""
a, b, c = 'a', 2, 'gamma'
print(a, b, c)

"""3.4 Create tuple containing just single element
which in turn contains three elements 'a', 'b', and 'c'.
Verify that length is actually 1 by using len() function.
"""
tpl2 = ('a', 'b', 'c')
tpl3 = (tpl2, )
print(tpl3, len(tpl3))
