from random import random
from random import uniform

# 生成10个0-1的随机浮点数
rd10 = [round(random(), 2) for _ in range(10)]
print('rd10: ', rd10)

# 生成 10 个 0 到 10 的满足均匀分布的浮点数
rdu10 = [round(uniform(0, 10), 2) for _ in range(10)]
print('rdu10: ', rdu10)





