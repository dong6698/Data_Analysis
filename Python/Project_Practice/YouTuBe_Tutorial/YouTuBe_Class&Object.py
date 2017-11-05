class Enemy:
    __gender = 'male'

    def __init__(self, new_life):
        self.life = new_life
        print("init enemy")

    def attack(self):
        print("ooh attacked!")
        self.life -= 1
        self.checkLife()

    def checkLife(self):
        print(str(self.life) + " life left")

    def get_gener(self):
        return self.__gender

def cal():
    a = b = c = 1
    if a == b == c:
        print("yes")

e_1 = Enemy(10)
print(e_1.get_gener())
e_1.checkLife()
e_1.attack()
cal()

