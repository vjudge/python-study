import pylightxl as xl

TOTAL_FILE = './files/merge-total.xlsx'
MERGE_FILES = ['./files/merge-file1.xlsx', './files/merge-file2.xlsx', './files/merge-file3.xlsx']

tdata = []

titleFlag = True
for file in MERGE_FILES:
    db = xl.readxl(fn=file)
    if titleFlag:
        tdt = db.ws(ws='Sheet1').col(col=1)
        tdata.append(tdt)
        titleFlag = False
    coldt = db.ws(ws='Sheet1').col(col=2)
    tdata.append(coldt)

print('tdata: ', tdata)

# 写入文件
wtdb = xl.Database()
wtdb.add_ws(ws='Sheet1')
rowIndex = 0
for rowdt in tdata:
    rowIndex += 1
    colIndex = 1
    for data in rowdt:
        wtdb.ws(ws='Sheet1').update_index(row=rowIndex, col=colIndex, val=data)
        colIndex += 1
xl.writexl(db=wtdb, fn=TOTAL_FILE)







