# Decorator
from functools import wraps


def decorator_func(fff):
    @wraps(fff)
    def wrap_function():
        print("before executing func()")
        fff()
        print("after executing func()")
    return wrap_function


def func():
    print('doing func()')
    pass


dec_ins = decorator_func(func)
dec_ins()


# 装饰器
@decorator_func
def dec_func():
    print('doing func()')
    pass


dec_func()
print(dec_func.__name__)







