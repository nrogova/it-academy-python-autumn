"""Task 2. Создайте декоратор, который хранит в файле результаты вызовы функций
(за все время, не только текущий запуск программы)
"""


def results_dec(fun):
    def wrapper():
        results = fun()
        f = open('results.txt', 'a')
        f.write(results + " ")
        f.close()
    return wrapper


@results_dec
def palindr():
    num = input('Enter number ')

    lst1 = list(num)
    lst2 = lst1[::-1]

    if lst1 == lst2:
        print(num, 'is palindrom')
    else:
        print(num, 'is not palindrom')
    return(num)


palindr()
