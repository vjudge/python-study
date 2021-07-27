# set

# set1 = set()
# set1 = set('a')
# set1 = {'a', 'b', 'c'}
set1 = set(['a', 'b', 'c'])

print('set1: ', set1)

set2 = set(['a', 'd', 'e'])
set3 = set(['a', 'b', 'd', 'f'])

print('union: ', set1.union(set2, set3))
print('difference: ', set1.difference(set2, set3))
print('intersection: ', set1.intersection(set2, set3))

set4 = set(['a', 'b', 'c', 'd'])
print('issubset: ', set1.issubset(set4))
print('issubset: ', set1.issubset(set3))