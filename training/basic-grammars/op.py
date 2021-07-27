
# -------- is --------
print('-------- is --------')
a = [1, 2, 3]
b = [1, 2, 3]
print('a is b: ', a is b)
# False

a, b = {'c': 1, 'd': 2}
a = b
print('a is b: ', a is b)
# True

a = 123
b = 123
print('a is b: ', a is b)
# True

c = 1234567
d = 1234567
print('c is d: ', c is d)
# True

# None 对象是一个单例类的实例，具有唯一的标识号
print('id(None): ', id(None))
a = None
print('a is None: ', a is None)
# True


# -------- in --------
print('-------- in --------')

print('abc-ab: ', 'ab' in 'abc')
# True
print('abc-ab: ', 'abc'.find('ab'))
# 0

print('acb-ab: ', 'ab' in 'acb')
# False
print('acb-ab: ', 'acb'.find('ab'))
# -1


# -------- == --------
print('-------- == --------')

str1 = 'abc'
str2 = 'abc'
print('str1 == str2: ', str1 == str2)

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = [1, 3, 2]
print('lst1 == lst2: ', lst1 == lst2)
# True
print('lst1 == lst3: ', lst1 == lst3)
# False






