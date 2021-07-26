# max(iterable, *[, key, default])

list1 = [1, 2, 3, 2, 1, 2, 4, 3]

max_item = max(list1)

max_item = max(list1, key=lambda x: list1.count(x), default=1)

print('max_item: ', max_item)
# max_item:  2

print('default: ', max((), default=111))
# default:  111


lstobj = [
    {'name': 'xiaoming', 'age': 18, 'gender': 'male'},
    {'name': 'xiaohong', 'age': 20, 'gender': 'female'}
]
print('max age: ', max(lstobj, key=lambda x: x['age']))
# max age:  {'name': 'xiaohong', 'age': 20, 'gender': 'female'}


dist1 = {'a': 3, 'b': 2, 'c': 1}
print('max dist: ', max(dist1))
# max dist:  c





