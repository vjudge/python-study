import pylightxl as xl

db = xl.readxl(fn='./sample1.xlsx')

print('db.ws_names: ', db.ws_names)

rc11 = db.ws(ws='语文').address(address='A1')
print('rc11 = ', rc11)

rc12 = db.ws(ws='语文').index(row=1, col=2)
print('rc12 = ', rc12)

index = 0
for row in db.ws(ws='语文').rows:
    index += 1
    print(index, row)





