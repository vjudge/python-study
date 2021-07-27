# zip
将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

### 定义
```python
zip(*iterables)
# zip([iterable, ...])
```


### sample
```python
a = [1, 2, 3]
b = [4, 5, 6]
zip(a, b)
# [(1, 4), (2, 5), (3, 6)]
```


