# 列表
列表用方括号 [] 定义，方括号括起的部分就是一个列表。

```
# 随意创建3个列表，同一个列表中可以存放任意基本数据类型
list1 = [] 
list2 = [1, 2, 3]
list3 = ['a', 'b', 'c'] 
# 列表中的数据项可以是不同的数据类型
list4 = [1, 2, 3.14, 3+4j, 'a']
```


### 通过索引下标访问列表中的元素，可以一次访问一个或多个元素。
```
list = [1, 2, 3.14, 3+4j, 'a']
# 访问单个元素
print('list[2]: ', list[2])
# 访问多个元素
print('list[0:2]: ', list[0:2])
```


### 更改列表中的元素
```
list = [1, 2, 3.14, 3+4j, 'a']
list[2] = 3.1415
print('after list[2]: ', list[2])
```


### 列表拼接
```
print('list1 + list2: ', list1 + list2)
```


### 列表乘法
```
print('list1 * 2: ',list1 * 2)
```


### 判断元素是否存在于列表中
```
print('3 in list1?', 3 in list1)
```


### len(list)：列表长度


### max(list)：列表中最大值


### min(list)：列表中最小值


### del：删除元素
```
del list[1]
```


### list.remove(obj)：删除元素
```
list.remove(3+4j)
```


### list.clear()：清空列表
```
list.clear()
```


### list.append(obj)：添加新元素将新元素添加到列表末尾
```
list.append('XXX')
```


### list.insert(index, obj)
添加元素：插入新元素到指定索引位置
```
list.insert(2, 'YYY')
```


### list.count(obj)：元素obj在列表中出现的次数


### list.index(obj)：从列表中找出某个值第一个匹配项的索引位置


### list.copy()：复制一个已有的表


### list.reverse()：反转一个已有的表


### list.pop()：从列表尾部取出元素











