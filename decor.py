# декоратор

# тестируем  замыкание
# def outer(counter):
#     print(counter)
#     def ineer(*args):
#         nonlocal counter
#         counter += args[0]
#         return counter
#     return ineer
# b = outer(4)
# print(b(6))

# def test(*args, **kwargs):
#     print(args, kwargs)
#     print(*args, *kwargs, *kwargs.values())
#
#
# # принимаем во внешнюю функцию другую - some_function
#
# # Тест аналога arguments в JS
# test(5,6,7,8, bar = 5, f = 'asdfs')

# Протестируем парсер на декораторах

# def inner_html(*args, **kwargs):
#     print(*args)
#
# def h1(some_func):
#     def h1_parser(*args, **kwargs):
#         print('<h1>')
#         some_func(*args, **kwargs)
#         print( '</h1>')
#     return h1_parser
#
# f = h1(inner_html)
# f('some html text')
#
# inner_html = h1(inner_html)
# inner_html('some html text2')


# тест декоратора - символа

# def h1(some_func):
#     def h1_parser(*args, **kwargs):
#         print('<h1>')
#         some_func(*args, **kwargs)
#         print( '</h1>')
#     return h1_parser
#
# @h1
# def inner_html(*args, **kwargs):
#     print(*args)
#
# inner_html('some html text')


#несколько декораторов
# def div(some_func):
#     def div_parser(*args, **kwargs):
#         print('<div>', end = ' ')
#         some_func(*args, **kwargs)
#         print('</div>', end = ' ')
#     return div_parser
#
#
#
# def h1(some_func):
#     def h1_parser(*args, **kwargs):
#         print('<h1>' ,end = ' ')
#         some_func(*args, **kwargs)
#         print( '</h1>',end = ' ')
#     return h1_parser
#
#
# @h1
# @div
# def inner_html(*args, **kwargs):
#     print(*args,end = ' ')
#
# inner_html('h1')
# print()
# inner_html('another html')




# inner_html = h1(div(inner_html))
# inner_html('h1 in div' )

# inner_html = div(h1(inner_html))
# inner_html('div in h1')



#повторяем
def outer(func):
    def parser(*args,**kwargs):
        print('<styles>')
        func(*args,**kwargs)
        print('</styles>')
    return parser

@outer
def coords(*args,**kwargs):
    print(*args)

coords(12,13,14,15)

# было жутко