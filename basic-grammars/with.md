# with

使用with语句都可以抽象出大部分资源处理逻辑。不必每次都显式地写一个try...finally语句，with语句会自行处理。


with语句一般用来管理系统资源的安全获取和释放。资源首先由with语句获取，并在执行离开with上下文时自动释放。


打开文件时一般建议使用with语句，因为这样能确保打开的文件描述符在程序执行离开with语句的上下文后自动关闭。
```
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
```
以上代码同以下代码：
```
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
```














