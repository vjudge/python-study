# class
print('---------- class ----------')

class Monster():
    def __init__(self, hp = 100):
        self.hp = hp
    def run(self):
        print('- 移动位置 -')
    def whoami(self):
        print('I am Monster')

# 普通怪物
class Animal(Monster):
    '普通怪物'
    pass

# Boss类怪物
class Boss(Monster):
    def whoami(self):
        print('I am Boss')

monster = Monster()
animal = Animal()
boss = Boss()

print('monster type: %s', %type(monster))
print('animal type: %s', %type(animal))
print('boss type: %s', %type(boss))









