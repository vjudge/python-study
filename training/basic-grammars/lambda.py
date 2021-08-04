# lambda
from functools import reduce

# Python 主要提供了这么几个函数：map()、filter() 和 reduce()，通常结合匿名函数 lambda 一起使用。

# 求 [1, 10] 的所有偶数
lst = filter(lambda x: x % 2 == 0, range(1, 11))
print('lst: ', list(lst))
# lst:  [2, 4, 6, 8, 10]

lst = map(lambda x: x + 10, range(1, 11))
print('lst: ', list(lst))
# lst:  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

sum_nums = reduce(lambda x, y: x + y, range(1, 11))
print('lst: ', sum_nums)
# lst:  55

# 列表每项平方
print([(lambda x: x*x)(x) for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


tuple1 = [(1, 15), (2, 0), (10, 10), (5, -1)]
tuple1.sort(key=lambda x: x[1])  # 按列表中元组的第二个元素排序
print('tuple1: ', tuple1)
# tuple1:  [(5, -1), (2, 0), (10, 10), (1, 15)]










