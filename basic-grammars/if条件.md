# if条件

* 每个条件后面要使用冒号 :，冒号后的内容表示满足条件后要执行的语句块。
* 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块（IDE 会自动缩进）。
* 在 Python 中没有 switch–case 语句。

```
if boolean_expression1:
    suite1 
elif boolean_expression2:
    suite2
...
elif boolean_expressionN:
    suiteN
else:
    else_suite
```

```
if A > B:
    print('The larger number is:',A) 
elif A == B:
    print('A and B are equal to ',A)  
else:
    print('The larger number is:',B) 
```






