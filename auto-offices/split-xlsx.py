import pylightxl as xl

TOTAL_FILE = './files/merge-total.xlsx'
MERGE_FILES_PREFIX = './files/merge-file'

db = xl.readxl(fn=TOTAL_FILE)
titleFlag = True
title = []
file_cnt = 1
for rowdt in db.ws(ws='Sheet1').rows:
    if titleFlag:
        title = rowdt.copy()
        titleFlag = False
        continue
    file_name = MERGE_FILES_PREFIX + str(file_cnt) + '.xlsx'
    print('file_name: ', file_name)
    splitdb = xl.Database()
    splitdb.add_ws(ws='Sheet1')
    rowIndex = 1
    for data in rowdt:
        splitdb.ws(ws='Sheet1').update_index(row=rowIndex, col=1, val=title[rowIndex-1])
        splitdb.ws(ws='Sheet1').update_index(row=rowIndex, col=2, val=data)
        rowIndex += 1
    xl.writexl(db=splitdb, fn=file_name)
    file_cnt += 1





