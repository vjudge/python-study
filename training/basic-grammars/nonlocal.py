# nonlocal

def non_func():
    a = 1

    def sub_func():
        nonlocal a
        print('a: ', a)
        a += 1

    sub_func()
    print('a: ', a)


non_func()















