# 循环

## for循环

for 循环遍历序列中的项目，序列包括但不限于字符串、列表、元组、字典。
```
# 当 <item> in <sequence> 为 True 时，执行 <actions>
for <item> in <sequence>:
    <actions>
```

```
nums = [98,94,82,67,58,90,86]
sum = 0
#遍历列表中的元素，求和
for element in nums:
    sum += element
```


通过 range() 函数遍历数据序列，可以将 range() 生成的数列作为索引。range() 函数的参数是可变的：
```
for i in range(4):
    print('i: ', i)
# i: 0
# i: 1
# i: 2
# i: 3
```



## while循环
while 循环的依据是条件判断，即当 condition 为 True，则执行 Action，否则退出。
```
while condition:
    Action
```

```
#初始化测试数据
nums = [98,94,82,67,58,90,86]
sum = 0
index = 0
while index < len(nums):
    sum += nums[index]
    index += 1
```


## break
break 语句用于跳出 for 和 while 循环体，也就意味着循环结束


## continue
continue 不会退出循环体，而是跳过当前循环块的剩余语句，继续下一轮循环


## Pass
pass 是空语句，一般用做占位，不执行任何实际的操作，只是为了保持程序结构的完整性
```
for i in range(len(nums)):
    if nums[i] < 60:
        print('Someone failed!')
    else:
        pass
```












