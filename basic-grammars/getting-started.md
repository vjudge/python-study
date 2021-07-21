# python入门

Python 是一门动态的、强类型语言。
* 动态语言：动态指代码运行时才被编译器一行一行翻译执行
* 强类型：强类型指被绑定一个类型后便不能修改，不能与其他类型混用

Python默认使用UTF-8字符编码。

通常，Python，使用 .py 作为Python控制台程序与Python模块的扩展名，使用 .pyw 作为GUI程序的扩展名。


### 命名规则
* 允许包括英文、数字以及下划线（_），不能以数字开头
    - 类变量若以单下划线（_）开头，代表不能直接被访问，不能通过 import module_name 而导入
    - 类变量若以双下划（__）开头，表示为类的私有成员，不能被导入和其他类变量访问
    - 以双下划开头和双下划线结尾的变量是 Python 里的专用标识，有特殊的身份
* 名称区分大小写
* Python 变量命名习惯遵守蛇形命名法（snake case）


### 缩进原则
Python 的缩进方法，一般为 4 个字符。通过这种层级结构，展现代码的逻辑层次。


### 关键字
Python有35个关键字
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
* True 和 False 用于表示值的真假
* 逻辑反操作 Python 使用 not
* None 表示空值
* Python 两个条件同时满足使用 and
* 两者满足其一，Python 使用 or
* Python 使用 elif



### “#”表示注解
