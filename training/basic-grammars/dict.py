# dict字典

# 直接赋值
# dict1 = {}
# dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1 = {'Excellent': 100, 'Good': 80, 'Pass': 60, 'Fail': 50}

# dict构造函数
# dict1 = dict(Excellent=100, Good=80, Pass=60, Fail=50)
# dict1 = dict({'Excellent': 100, 'Good': 80}, Pass=60, Fail=50)
# dict1 = dict([('Excellent', 100), ('Good', 80)], Pass=60, Fail=50)

# fromkeys()
# dict1 = {}.fromkeys(['Excellent', 'Good', 'Pass', 'Fail'], 0)
# output: dict1:  {'Excellent': 0, 'Good': 0, 'Pass': 0, 'Fail': 0}
# dict1 = {'Excellent': 100, 'Good': 80}.fromkeys(['Good', 'Pass', 'Fail'], 0)
# output: dict1:  {'Good': 0, 'Pass': 0, 'Fail': 0}

print('dict1: ', dict1)

# 批量更新
dict1.update({'ccc': 1, 'ddd': 2})
dict1.update([('ccc', 222), ('ddd', 222)])
dict1.update([('ccc', 222)], eee=444)
print('dict1: ', dict1)

# 获取值
print('dict1.Good: ', dict1['Good'])
print('dict1.Good: ', dict1.get('Good'))

# 遍历dict
for key, val in dict1.items():
    print(key, val)

# 获取所有key值
print('values: ', set(dict1))
print('keys: ', dict1.keys())

# 获取所有values值
print('values: ', dict1.values())

# 判断是否在
if 'Excellent' in dict1:
    print('Excelent in dict')
if 'test' not in dict1:
    print('test not in dict')

# 删除
del dict1['ccc']
print('dict1: ', dict1)
dict1.pop('ddd')
print('dict1: ', dict1)


print('dict1: ', dict1.items())
# dict1:  dict_items([('Excellent', 100), ('Good', 80), ('Pass', 60), ('Fail', 50)])

dict1.setdefault('eee', 111)
dict1.setdefault('fff', 111)
print('', dict1)


# 合并
dict3 = {**{'eee': 1, 'fff': 2, 'c': [1, 2]}, **{'eee': 22, 'e': 33}}
print('dict3: ', dict3)


# 求差集
def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])


print('difference: ', difference(dict1, dict3))


# 按键排序
def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])


print(dict1)


