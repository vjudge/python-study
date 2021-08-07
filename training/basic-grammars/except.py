# except

# try:
#     s = input('please enter two numbers separated by comma: ')
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
# except (ValueError, IndexError) as err:
#     print('Error: {}'.format(err))
# except:  # 与任意异常相匹配（包括系统异常等）
#     print('Other error')
#
# # 同上
# try:
#     s = input('please enter two numbers separated by comma: ')
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
# except ValueError as err:
#     print('ValueError: {}'.format(err))
# except IndexError as err:
#     print('IndexError: {}'.format(err))
# except Exception as err:  # Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常
#     print('OtherError: {}'.format(err))


# 自定义异常
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        return ('{} is invalid input'.format(repr(self.value)))


try:
    raise MyInputError(1)  # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))


# 关于报错
# 如果你在异常处理的 except block 中，把异常赋予了一个变量，那么这个变量会在 except block 执行结束时被删除
err = 1
try:
    1 / 0
except ZeroDivisionError as err:
    pass
# finally:
#     del e
print('err: ', err)
# NameError: name 'err' is not defined












