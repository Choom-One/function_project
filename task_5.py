def task_5(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key,value)
task_5(ads=1, sd=2, asdf=3, sdgfr=4, rdfetg=8)