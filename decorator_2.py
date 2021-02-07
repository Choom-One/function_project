import random


def decoder(func):
    def rev(*args):
        m_list = args[::-1]
        return func(m_list)
    return rev

@ decoder
def func(*args):
    return args

print(func(2, 4, 6, 3))