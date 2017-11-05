class Mario():
    gender = "male"
    age = 12
    def move(self):
        print("i am moving")

class Mashroom():
    gender = 'female'
    def eat(self):
        print("i am eating mashroom")

class bigMario(Mashroom, Mario):
    gender_1 = Mario.gender
    gender_2 = Mashroom.gender
    pass

big = bigMario()
big.eat()
big.move()
