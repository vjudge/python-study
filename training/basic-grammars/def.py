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


# 函数求和
def _sum(x, y):
    return x + y


print(_sum(3, 5))












