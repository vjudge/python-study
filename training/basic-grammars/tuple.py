# 元组
print('------ 元组 ------')
tuple1 = ()
# 如果元组只有一个元素，那么这个元素后面要加逗号。否则将被认为是基础类型
tuple2 = (12,)
tuple3 = (1, 2, 3)
tuple4 = (3.14, 5.96, 1897, 2020, 'a', 3 + 4j)
# 创建元组，可以没有括号，元素之间用逗号分隔开即可
tuple5 = 4, 5, 6
# 正数第2个元素
print('tuple4[1]: ', tuple4[1])
# 倒数第2个元素
print('tuple4[-2]: ', tuple4[-2])

# 列表反转
# [::-1] 生成逆向索引（负号表示逆向），步长为 1 的切片
def reverse(lst):
    return lst[::-1]
print(reverse((1, 2, 3, 4, 5)))


# 列表元组长度大小
# 由于列表是动态的，所以它需要存储指针，来指向对应的元素
# 由于列表可变，所以需要额外存储已经分配的长度大小
lst = [1, 2, 3]
print('lst.sizeof: ', lst.__sizeof__())
# lst.sizeof:  104
tuple5 = (1, 2, 3)
print('tuple5.sizeof: ', tuple5.__sizeof__())
# tuple5.sizeof:  48








