# for

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d'%(j, i, j*i), end='\t')
    print()

attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]

rst = []
for objs in values:
    mid_rst = {}
    for i in range(0, len(objs)):
            mid_rst[attributes[i]] = objs[i]
    rst.append(mid_rst)
print('rst: ', rst)

print('rst: ', [dict(zip(attributes, value)) for value in values])











