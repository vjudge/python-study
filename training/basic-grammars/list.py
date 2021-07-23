# list

# list = [1, 3.14, 'test', ['ls1-1', 'ls2-2', 'ls3-3']]
# sku = list[3]
# # sku = list[3].copy()
# print('sku = ', sku)
# # sku = ['ls1-1', 'ls2-2', 'ls3-3']
#
# sku.append('ls4-4')
# print('append sku = ', sku)
# # append sku =  ['ls1-1', 'ls2-2', 'ls3-3', 'ls4-4']
#
# sku.insert(1, 'ls-insert')
# print('insert sku = ', sku)
# # insert sku =  ['ls1-1', 'ls-insert', 'ls2-2', 'ls3-3', 'ls4-4']
#
# sku.pop()
# print('pop sku = ', sku)
# # pop sku =  ['ls1-1', 'ls-insert', 'ls2-2', 'ls3-3']
#
# sku.remove('ls2-2')
# print('remove sku = ', sku)
# # remove sku =  ['ls1-1', 'ls-insert', 'ls3-3']
#
# print('list = ', list)
# # list =  [1, 3.14, 'test', ['ls1-1', 'ls-insert', 'ls3-3']]


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





