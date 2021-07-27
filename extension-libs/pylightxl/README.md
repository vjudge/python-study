# pylightxl

### [GitHub传送门](https://github.com/PydPiper/pylightxl)

### 安装
```buildoutcfg
pip3 install pylightxl
```

### 导入
```python
import pylightxl as xl
```

### 读文件
```python
# 返回所有的sheets
db = xl.readxl(fn='excelfile.xlsx')
# 返回指定sheets
db = xl.readxl(fn='excelfile.xlsx', ws=('Sheet1','Sheet2'))
# 读取sheets
db.ws_names // ['Sheet1', 'Sheet2']
```
```python
with open('excelfile.xlsx', 'rb') as f:
    db = xl.readxl(f)
```


### 读取工作簿数据
```python
# 读取Sheet1第A列第1行的数据
db.ws(ws='Sheet1').address(address='A1')
# 读取Sheet1第1行第2列内容
db.ws(ws='Sheet1').index(row=1, col=2)
# 读取Sheet1第A列第1行的数据
db.ws(ws='Sheet1').range(address='A1')
# 读取Sheet1第A列到Cl列中，第1行到第2行的数据
db.ws(ws='Sheet1').range(address='A1:C2')
# 获取Sheet1整行数据
db.ws(ws='Sheet1').row(row=1)
# 获取Sheet1整列数据
db.ws(ws='Sheet1').col(col=1)
# 按行读取
for row in db.ws(ws='Sheet1').rows:
    print(row)
# 按列读取
for col in db.ws(ws='Sheet1').cols:
    print(col)
```


### 修改工作簿数据
```python
# 工作簿内容设置为空
db.ws(ws='Sheet1').set_emptycell(val=0)
# 更新A1的值为100
db.ws(ws='Sheet1').update_address(address='A1', val=100)
db.ws(ws='Sheet1').update_address(address='A1', val='=B1+100')
# 更新A1的值为10
db.ws(ws='Sheet1').update_index(row=1, col=1, val=10)
db.ws(ws='Sheet1').update_index(row=1, col=1, val='=B1+100')
xl.writexl(db=db, fn='updated.xlsx')
```


### Named Ranges
```python
db.add_nr(name='Table1', ws='Sheet1', address='A1:B2')
db.nr_names
db.nr(name='Table1')
db.remove_nr(name='Table1')
```


###
```python
# 返回第1行中，值为20的那列值
db.ws(ws='Sheet1').keycol(key=20, keyindex=1)
# 返回第1列中，值为张三的那行值
db.ws(ws='Sheet1').keyrow(key='张三', keyindex=1)
```


### 写新文件
```python
wtdb = xl.Database()
wtdb.add_ws(ws='Sheet1')
data = [10, 20, 30, 40]
for row_id, data in enumerate(data, start=1):
    wtdb.ws(ws='Sheet1').update_index(row=row_id, col=1, val=data)
xl.writexl(db=wtdb, fn='output.xlsx')
```




