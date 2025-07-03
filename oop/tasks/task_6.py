from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

    def move(self):
        print("Dog is moving")

class Bird(Animal):
    def speak(self):
        print("Tweet!")

    def move(self):
        print("Bird is flying")


class Fish(Animal):
    def speak(self):
        print("Я молчу вообще то")

    def move(self):
        print("Fish is swimming")


if __name__ == "__main__":
    dog = Dog()
    bird = Bird()
    fish = Fish()

    zoo = [dog, bird, fish]

    for animal in zoo:
        animal.speak()
        animal.move()