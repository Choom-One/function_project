# generator_list
# list_a = [i for i in range(5)]
# print(list_a)
#
# list_b = [i ** 2 for i in [1, 2, 3]]
# print(list_b)

# list_a = ['privet', 'poka', 'spasibo']
# list_b = [ i for i in reversed(list_a) ]
#
# print([list_b])

# names = ['Max', 'Helen', 'Alex', 'Misha']
# list_a = [name for name in names if 'a' in name]
# print(list_a)

# cars = [{'q':1234354, 'w':1996}, {'q': 1242535, 'w': 1995}, {'q':13343453, 'w':1997}, {'q':124513452, 'w':1995}]
# n = 1995
# list_b = [i for i in cars for q, w in i.items() if w > n]
# print(list_b)

# list_dicts = [{'n': 1, 'y': 1993}, {'n': 2, 'y': 1995}, {'n': 3, 'y': 1998}, {'n': 4, 'y': 1959}, {'n': 5, 'y': 1994}]
# n = 1995
# list_b = [i for i in list_dicts for k, v in i.items() if v > n]
# print(list_b)


from random import randint

# n = 4
# b = 3
# matrix = [[randint(1, 9) for j in range(n)] for i in range(b)]
# print(matrix)

# old_dict = {'aa': 1, 'b': 2, 'ccc': 3}
# new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dict)
#
# old_dict = {'aa': 1, 'b': 2, 'ccc': 3, 'sffr': 4}
# new_dict = {value : key for key, value in old_dict.items()}
# print(new_dict) #разобрать


# n = 4
# list_1 = [randint(1, 8) for i in range(n)]
# list_2 = set(list_1)#превращаем список во множество
# tuple_n = {}
# for i in list_2:
#     tuple_n[i] = list_1.count(i)
# print(tuple_n)


# def main():
#     pass
#
# if __name__ == '__main__':
#     main()


# hello = lambda name: print(f'Hello {name}')#lambda-это анонимная функция, name-это аргумент функции который мы передаём, после двоеточия идет скрипт функции
#
# hello(name='Artiom')

name2 = ['qwer', 'lea', 'amir']#список наших имен

hello_name = lambda name: [f'Hello {i}' for i in name]#передаём фенкции аргемент name, потом проходимся циклом по списку записывая все в сторку где i- это имя,
#а сам цик мы оборацуиваем в список

print(hello_name(name2))