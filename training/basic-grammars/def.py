# def func

# 变量作用域
a = 10


def parent():
    b = 20

    def son():
        c = 30  # c: local
        print(b + c)  # b: enclosing
        print(a + b + c)  # a: global
        print(min(a, b, c))  # min : built-in

    son()


parent()














