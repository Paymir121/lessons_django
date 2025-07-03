class FlyAble:
    def fly(self):
        print("I can fly! And i am sexy")


class SwimAble:
    def swim(self):
        print("I'm swimming!")

class Duck(FlyAble, SwimAble):
    def make_sound(self):
        print("Quack! Fuck off!")

