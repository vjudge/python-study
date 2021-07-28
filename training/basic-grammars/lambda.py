# lambda
from functools import reduce

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







