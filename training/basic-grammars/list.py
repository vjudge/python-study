# list

list = [1, 3.14, 'test', ['ls1-1', 'ls2-2', 'ls3-3']]
sku = list[3]
# sku = list[3].copy()
print('sku = ', sku)
# sku = ['ls1-1', 'ls2-2', 'ls3-3']
# 正数第2个元素
print('list1: ', list[1])
# 倒数第2个元素
print('list[-2]: ', list[-2])

sku.append('ls4-4')
print('append sku = ', sku)
# append sku =  ['ls1-1', 'ls2-2', 'ls3-3', 'ls4-4']

sku.insert(1, 'ls-insert')
print('insert sku = ', sku)
# insert sku =  ['ls1-1', 'ls-insert', 'ls2-2', 'ls3-3', 'ls4-4']

sku.pop()
print('pop sku = ', sku)
# pop sku =  ['ls1-1', 'ls-insert', 'ls2-2', 'ls3-3']

sku.remove('ls2-2')
print('remove sku = ', sku)
# remove sku =  ['ls1-1', 'ls-insert', 'ls3-3']

print('list = ', list)
# list =  [1, 3.14, 'test', ['ls1-1', 'ls-insert', 'ls3-3']]


print('------------ 浅,深拷贝 ----------------')
from copy import deepcopy

lst = [1, 2, [3, 4, 6]]
cplst = lst.copy()
# cplst = deepcopy(lst)
cplst[0] = 10
cplst[2][1] = 40
print('cplst = ', cplst)
# cplst =  [10, 2, [3, 40, 6]]
print('lst = ', lst)
# lst =  [1, 2, [3, 40, 6]]


print('------------ 列表生成式 ----------------')

# 求 [1-10] 的平方
lst = [x*x for x in range(1, 11)]
print('lst: ', lst)
# lst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 求 [1-10] 中偶数的平方
lst = [x*x for x in range(1, 11) if x % 2 == 0]
print('lst: ', lst)
# lst:  [4, 16, 36, 64, 100]

# 多个值
lst = [x+y for x in range(1, 5) if x % 2 == 0 for y in range(1, 5) if y % 2 == 1]
print('lst: ', lst)
# lst:  [3, 5, 5, 7]

# y = 2*|x| + 5
x = [1, 2, 5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print('y: ', y)



