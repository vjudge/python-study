# max
返回最大值。


### 定义
```python
max(iterable, *[, key, default])
```


### sample
```python
max(a)
max(a, key=lambda x: a.count(x), default=1)
# 当传入的列表为空时，则返回 default；default未赋值会异常
max((), default=111)
```














