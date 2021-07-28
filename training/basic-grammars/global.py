# global

i = 1


def f():
    global i  # 声明为全局作用域
    i = 222
    print(i)


f()
# 222


def t():
    print(i)


t()
# 222


def g():
    i = 333  # 局部作用于
    print(i)
    pass


g()
# 333










