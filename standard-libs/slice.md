# slice
返回一个由 range(start, stop, step) 所指定索引集的 slice 对象。

### 定义
```python
slice(stop)
slice(start, stop[, step])
```


### sample
```python
a = [1, 2, 3, 4, 5]
a[slice(0, 5, 2)]
# [1, 3, 5]
```


