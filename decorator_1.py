def my_decorator(func):
    def delete(arg):
        del_dec = [i for i in arg if i % 2 != 0]
        return func(del_dec)

    return delete


@my_decorator
def func(x):
    print(x)


func([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10])