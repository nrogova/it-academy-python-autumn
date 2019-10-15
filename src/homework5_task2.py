"""Task 2. Дан текст (строк может быть много, разделенных \n).
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.
"""
text = input('Please enter text: ')
lst = text.split()

dct = {}
for i in lst:
    dct[i] = dct.get(i, 0) + 1

max_value = max(dct.values())
most_often = [k for k, v in dct.items() if v == max_value]

print(min(most_often))
