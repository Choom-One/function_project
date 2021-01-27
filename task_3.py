def Task(*agrs):
    summ = 0
    for i in agrs:
        summ += i
        continue
    summ *= len(agrs)
    return summ
    print(summ)
print(Task(1,3,5,7,4,3))