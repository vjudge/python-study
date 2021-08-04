# global
声明局部变量为全局变量

```python
param = 1
def func():
    global param
    pass
```
global 关键字，并不表示重新创建了一个全局变量 param，而是告诉 Python 解释器，函数内部的变量 param，就是之前定义的全局变量，并不是新的全局变量，也不是局部变量。这样，程序就可以在函数内部访问全局变量，并修改它的值了。















