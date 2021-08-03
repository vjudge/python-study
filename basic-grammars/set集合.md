# 集合
用大括号 {} 创建集合。如果要创建一个空集合，必须用 set() 而不是 {}，{}创建一个空的字典。
集合是一种不允许元素出现重复的容器。
集合内的元素必须是可哈希类型（hashable）。

集合不支持索引操作。

集合具有三个特点：
* 确定性，集合中的元素必须是确定的
* 互异性，集合中的元素互不相同
* 无序性，集合中的元素没有先后之分


### 创建集合
```
set1 = set()
set1 = set('a')
set1 = {'a', 'b', 'c'}
set1 = set(['a', 'b', 'c'])
```


### set1.add(obj)：添加元素
```
set1.add('a')
```


### set1.remove(obj)：移除元素
```
setA.remove('A')
```


### setA&setB：交集
```python
setA.intersection(setB)
```


### setA|setB：并集
```python
setA.union(setB)
```


### setA-setB：差集
```python
setA.difference(setB)
```


### setA是否是setB的子集
```python
setA.issubset(setB)
```
