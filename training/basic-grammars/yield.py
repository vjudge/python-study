# yield

def yield_func():
    print('init yield function')
    yield
    print('return ok')


# gen = yield_func()
# print('gen: ', gen)
# print('gen first: ')
# next(gen)
# print('gen second: ')
# next(gen)


# send
def yield_send():
    print('init send')
    result = yield 111
    if result:
        print('send value is: ', result)
    else:
        print('no send value')


gen = yield_send()
print('yield first: ', next(gen))
print('start send: ')
# print('yield second: ', next(gen))
print('yield send: ', gen.send(222))



















