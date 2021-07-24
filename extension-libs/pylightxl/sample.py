import pylightxl as xl

# db = xl.readxl(fn='./sample1.xlsx')
db = xl.readxl(fn='./sample1.xlsx', ws=('Sheet1', 'Sheet2', 'Sheet3'))

# 读取所有Sheets名
print('db.ws_names: ', db.ws_names)
# db.ws_names:  ['Sheet1', 'Sheet2', 'Sheet3']


# 读取Sheet1第A列第1行的数据
print('rc11 = ', db.ws(ws='Sheet1').address(address='A1'))
# rc11 =  姓名


# 输出该单元格对应的公式
print('G2: ', db.ws(ws='Sheet1').address(address='G2', output='f'))
# G2:  =SUM(B2:F2)


# 输出该单元格对应的评论
print('G2: ', db.ws(ws='Sheet1').address(address='G2', output='c'))
# G2:  vjudge: 语文总分


# 读取Sheet1第1行第2列内容
print('rc12 = ', db.ws(ws='Sheet1').index(row=1, col=2))
# rc12 =  第1题


# 读取Sheet1第A列第1行的数据
print('rc11 = ', db.ws(ws='Sheet1').range(address='A1'))
# rc11 =  [['姓名']]


# 读取Sheet1第A列到Cl列中，第1行到第2行的数据
print('A1:C2 = ', db.ws(ws='Sheet1').range(address='A1:C2'))
# A1:C2 =  [['姓名', '第1题', '第2题'], ['张三', 2, 6]]


# 获取Sheet1整行数据
print('row1 = ', db.ws(ws='Sheet1').row(row=1))
# row1 =  ['姓名', '第1题', '第2题', '第3题', '第4题', '第5题', '总分']


# 获取Sheet1整列数据
print('col1 = ', db.ws(ws='Sheet1').col(col=1))
# col1 =  ['姓名', '张三', '李四', '王五', '平均分']

# 按行读取
for row in db.ws(ws='Sheet1').rows:
    print(row)
# ['姓名', '第1题', '第2题', '第3题', '第4题', '第5题', '总分']
# ['张三', 2, 6, 2, 4, 7, 21]
# ['李四', 5, 4, 3, 8, 4, 24]
# ['王五', 3, 7, 5, 2, 8, 25]
# ['平均分', 1.11, 1.11, 1.11, 2.22, 1.56, 1.56]


# 按列读取
for col in db.ws(ws='Sheet1').cols:
    print(col)
# ['姓名', '张三', '李四', '王五', '平均分']
# ['第1题', 2, 5, 3, 1.11]
# ['第2题', 6, 4, 7, 1.11]
# ['第3题', 2, 3, 5, 1.11]
# ['第4题', 4, 8, 2, 2.22]
# ['第5题', 7, 4, 8, 1.56]
# ['总分', 21, 24, 25, 1.56]


# 更新B1的值为6
print('rc21 = ', db.ws(ws='Sheet1').address(address='B2'))
db.ws(ws='Sheet1').update_address(address='B2', val=6)
print('rc21 = ', db.ws(ws='Sheet1').address(address='B2'))
xl.writexl(db=db, fn='updated.xlsx')

# ---------- range name --------------
db.add_nr(name='Table1', ws='Sheet1', address='A1:B2')
print('nr_names: ', db.nr_names)
# nr_names:  {'Table1': 'Sheet1!A1:B2'}

print('nr: ', db.nr(name='Table1'))
# nr:  [['姓名', '第1题'], ['张三', 6]]

db.remove_nr(name='Table1')
print('nr_names: ', db.nr_names)
# nr_names:  {}


# ---------- row/col based on key-value --------------
# 返回第4行中，值为key的那列值
print('col4,key=9: ', db.ws(ws='Sheet1').keycol(key=1, keyindex=4))
# col4,key=9:  ['第4题', 4, 8, 1, 2.44]

print('row1,key=1: ', db.ws(ws='Sheet1').keyrow(key='李四', keyindex=1))
# row1,key=1:  ['李四', 5, 4, 3, 8, 4, 24]


# 获取为空
ssd = db.ws(ws='Sheet1').ssd(keycols="KEYCOLS", keyrows="KEYROWS")
print('ssd: ', ssd)


# --------------- 写新文件 -------------------
wtdb = xl.Database()
wtdb.add_ws(ws='Sheet1')
data = [10, 20, 30, 40]
for row_id, data in enumerate(data, start=1):
    wtdb.ws(ws='Sheet1').update_index(row=row_id, col=1, val=data)
xl.writexl(db=wtdb, fn='output.xlsx')

