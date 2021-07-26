# all
判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False

### 定义
```python
all(iterable)
```


### sample
```python
all(1, 2, 3)
# True
all(1, 2, 0)
# False
all('a', '', 'c')
# False
all([])
# True
all(())
# True
```


