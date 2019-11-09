import module_to_apply as m_a
""" Task 6.1 Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner1() – все фукнции вызываются по очереди
runner2(‘gen_numbers’) – вызывается только функцию gen_numbers.
runner3(‘func’, ‘func1’...) - вызывает все переданные функции
"""

all_functions = ('wierd_func', "arifm_func", 'devision_func',
                  'square_cycle', 'palindr', 'fuzz_buzz',
                  'list_compr', 'list_practice', 'dct_n',
                  'count_me', 'often_text', 'cities_countries',
                  'set_joint', 'set_differ')


def runner(*funcs):
    if len(funcs) == 0:
        funcs = all_functions
    for name in funcs:
        func = getattr(m_a, name)
        func()


runner()
