# enumerate

lst = ['jack', 'rose', 'tom']
for i, v in enumerate(lst):
    print(i, v)
# 0 jack
# 1 rose
# 2 tom

enum = enumerate(lst)
print(next(enum))
# (0, 'jack')
print(next(enum))
# (1, 'rose')
print(next(enum))
# (2, 'tom')












