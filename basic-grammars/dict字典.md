# 字典

一种映射表，存储 key-value（键值对）类型数据的容器。
* 同一个字典中，键必须是唯一的，不存在两个相同的键，键的值不能改变，数据类型可以是数字，字符串或者元组。
* 同一个字典中，值不必唯一，值可以是任意数据类型。
* 字典定义采用花括号 {}，键值之间用冒号隔开，键值对之间用逗号隔开。


### 创建字典
```python
# 直接赋值
dict = { 'Excellent': 100, 'Good': 80, 'Pass': 60, 'Fail': 50 }
# 构造函数
dict(Excellent=100, Good=80, Pass=60, Fail=50)
dict({'Excellent': 100, 'Good': 80}, Pass=60, Fail=50)
# 包含元组
dict([('Excellent', 100), ('Good', 80)], Pass=60, Fail=50)
# {'Excellent': 100, 'Good': 80, 'Pass': 60, 'Fail': 50}
# fromkeys()
{}.fromkeys(['Excellent', 'Good', 'Pass', 'Fail'], 0)
{'Excellent': 100, 'Good': 80}.fromkeys(['Good', 'Pass', 'Fail'], 0)
```

### 访问字典
* 通过键访问：如果不存在，就会抛异常
* 通过内建 get(key) 方法访问：如果不存在，会返回默认值
```python
dict = { 'Excellent': 100, 'Good': 80, 'Pass': 60, 'Fail': 50 }
print('dict[1]: ', dict[1])
print("dict.get('Good'): ", dict.get('Good', 0))
# 遍历
for key, val in dict.items():
    print(key, val)
```


# 是否在字典中
```python
key in dict
key not in dict
```


### 修改字典中的元素
```python
dict['Good'] = 85
```


### del：删除
```python
# 删除字典中的一个元素
del dict['Good']
# 删除字典
del dict
```


### pop(key)：内建方法删除指定元素
```python
dict.pop('Good')
```


### 批量更新
```python
dict.update({'key1': value1, 'key2': value2, ...})
dict.update([('key1', value1), ('key2', value2), ...])
dict.update([('key1', value1), ...], key=value)
```


### dict.clear()：清空字典


### dict.keys()：获取字典中所有的键
```python
set(dict)
set(dict.keys())
```

### dict.values()：获取字典中所有的值


### dict.items()：获取字典中所有的键值对


### d.setdefault(key,value)：如果字典中不存在该键值对，插入到字典中；如果存在，不修改键值
```python
d.setdefault(key,value)
```


### {**d1, **d2}：实现合并 d1 和 d2，返回一个新字典


### difference(d1, d2)：字典差
```python
def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])
```

### 按键排序
```python
def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])
```







