# 错误和异常
异常，通常是指程序运行的过程中遇到了错误，终止并退出。我们通常使用 try except 语句去处理异常，这样程序就不会被终止，仍能继续执行。

### 语法错误
语法错误，指的是程序不符合编程语言的语法规范，进而导致不能被解释器解释或者编译器无法编译。这些错误违背了语法规则，必须在程序执行前纠正，属于比较低级的错误，在编写程序时，可借助 IDE 进行语法检测，避免错误流到下游。


### 逻辑错误
在编程时没有充分考虑应用场景，导致程序逻辑不完整，或者输入不合法等。这类错误通常会导致程序无法达成期望的结果，在编程前应该通过周密的设计进行避免。


## 异常
异常是在程序运行中产生的，大多数的异常都不会被程序处理，并以错误信息的形式抛出，Python 中常见的异常有：

对于非致命异常，可以不终止程序，取代以“和谐”的处理方式来解决：捕获程序运行中出现的异常，并针对这种异常进行特定的处理，使程序得以继续执行而不至于终止。


### try-except
当程序中存在多个 except block 时，最多只有一个 except block 会被执行。换句话说，如果多个 except 声明的异常类型都与实际相匹配，那么只有最前面的 except block 会被执行，其他则被忽略。
```python
# 指定捕获异常，并处理
try:
    <statement>
except ErrorType:
    <statement>

# 同时捕获多种指定异常，并处理
try:
    <statement>
except (ErrorType1, ErrorType2, …, ErrorTypeN) as err:
    <statement>

# 默认捕获所有异常
try:
    <statement>
except:  # 与任意异常相匹配（包括系统异常等）
    <statement>
```

### finally
无论发生什么情况，finally block 中的语句都会被执行，哪怕前面的 try 和 excep block 中使用了 return 语句。
```python
try:
    <statement>
except Exception:  # Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常
    <statement>
finally:
    <statement>
```








