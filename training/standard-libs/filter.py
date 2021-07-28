# filter

def filter_per(p):
    return p.get('age') <= 18


persons = [
    {'name': 'Jack', 'age': 18},
    {'name': 'Rose', 'age': 16},
    {'name': 'Tom', 'age': 23}
]

rst = filter(filter_per, persons)
print('rst: ', rst)
for item in rst:
    print('item: ', item)







