# 整数，浮点数，复数
print('------ 整数，浮点数，复数 ------')
a = 123
b = 3.14
print('a = ', int(b))
print('b = ', float(a))
print('complex(a) = ', complex(a))
print('complex(a, b) = ', complex(a, b))

# 字符串
print('------ 字符串 ------')
str1 = 'hello world!'
print('str1: ', str1)
print('str1[0]: ', str1[0])
print('str1[6:11]: ', str1[6:11])
print('str1[6:11]: ', str1[6:11])

print('字符替换：', str1.replace('world', 'python'))
print('首字符大写：', str1.title())
print('连接字符串：', '-'.join(['111', '222', '333']))


# 赋值
a, b = {'c': 1, 'd': 2}
print('a: ', a)
# a:  c
print('b: ', b)
# b:  d

a, b = 1, 2
print('a: ', a)
# a:  1
print('b: ', b)
# b:  2

# ------ 格式化字符串 ------
print("I'm %s. I'm %d year old" % ('Rose', 19))

print("I'm %(name)s. I'm %(age)d year old" % {'name': 'Rose', 'age': 19})

# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world", "test"))
# 设置指定位置
print("{0} {1}".format("hello", "world"))
# 设置指定位置
print("{1} {0} {1}".format("hello", "world"))

print("我是：{name}, 大家可以叫我 {nickname}".format(name="vjudge", nickname="VVV"))

# 通过字典设置参数
names = {"name": "vjudge", "nickname": "VVV"}
print("我是：{name}, 大家可以叫我 {nickname}".format(**names))

# 通过列表索引设置参数
lst1 = ['vjudge', 'VVV']
print("我是：{0[0]}, 大家可以叫我 {0[1]}".format(lst1))  # "0" 是必须的


# ------ ------
print("%.2f" % 3.1415926)
print("%.0f" % 3.1415926)
print("%+.2f" % 3.1415926)
print("%+.2f" % -3.1415926)
print("逗号分隔数字: ", '{:,}'.format(1000000))
print("数字补零 (填充左边, 宽度为4)：0>4d", '{:0>4d}'.format(5))
print("数字补x (填充右边, 宽度为4)：x<4d", '{:x<4d}'.format(5))

print("百分比格式: ", '{:.2%}'.format(0.25))
print("指数计法: ", '{:.2e}'.format(1234000000))
print("右对齐，宽度是10，默认: ", '{:>10d}'.format(100))
print("左对齐，宽度是10: ", '{:<10d}'.format(100))
print("中间对齐: ", '{:^10d}'.format(100))




