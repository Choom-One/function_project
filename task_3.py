# def Task(*agrs):
#     summ = 0
#     for i in agrs:
#         summ += i
#         continue
#     summ *= len(agrs)
#     return summ
#     print(summ)
# print(Task(1,3,5,7,4,3))

def my_func(a, b):
    summ = a + b
    diff = a - b
    return summ, diff
summ, diff = my_func(a, b)

print(my_func(4, 6))