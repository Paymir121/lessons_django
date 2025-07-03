# Task 1

class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance: float = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount: float):
        """пополнение счёта;"""
        print("1: пополнение:", self.__balance, "+", amount)
        self.__balance += amount
        print("1.2: пополнение:", self.__balance)

    def withdraw(self, amount: float):
        """снятие средств (не должно позволять уйти в минус);"""
        print("2: снятие:", self.__balance, "-", amount)
        if self.__balance >= amount:
            self.__balance -= amount
            print("2.2: снятие:", self.__balance)
        else:
            print("3: недостаточно средств")

    def get_balance(self):
        """получить текущий баланс."""
        print("4: текущий баланс",self.__balance)
        return self.__balance

# Task 2

class Employee:
    def __init__(self, name: str, salary: float, position: str):
        self.name = name
        self.salary = salary
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position} {self.salary}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, position: str, employees: list[Employee]):
        super().__init__(name, salary, position)
        self.employees = employees


    def get_info(self):
        return f"{self.name} {self.position} {self.salary} {self.employees}"

class Developer(Employee):
    def __init__(self, name: str, salary: float, position: str, programming_language: str):
        super().__init__(name, salary, position)
        self.programming_language = programming_language

    def get_info(self):
        return f"{self.name} {self.position} {self.salary} {self.programming_language}"

# Task 3


class Shape:

    def area(self) -> float:
        return 0

    def perimeter(self) -> float:
        return 0

class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    rectangle_1 = Rectangle(4, 5)
    rectangle_2 = Rectangle(3, 6)
    circle_1 = Circle(5)
    circle_2 = Circle(3)

    shapes = [rectangle_1, rectangle_2, circle_1, circle_2]

    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")


# Task 4

from abc import abstractmethod, ABC


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

    def move(self):
        print("Car is moving")

class Boat(Transport):
    def start_engine(self):
        print("Boat engine started")

    def stop_engine(self):
        print("Boat engine stopped")

    def move(self):
        print("Boat is moving")

# Task 5

class FlyAble:
    def fly(self):
        print("I can fly! And i am sexy")


class SwimAble:
    def swim(self):
        print("I'm swimming!")

class Duck(FlyAble, SwimAble):
    def make_sound(self):
        print("Quack! Fuck off!")

# Task 6

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

# Singleton

class Logger:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.logs: list[str] = []

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs

if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("First message")
    logger2.log("Second message")

    assert logger1 is logger2, "Logger is not a singleton!"
    assert logger1.get_logs() == ["First message", "Second message"]

# Solid S

class PDFReport:
    def generate(self):
        print("PDF generated")

class FileReport:
    def save(self, filename):
        print(f"Saved {filename}")

class CustomReport(PDFReport, FileReport):
    def __init__(self, title, content):
        self.title = title
        self.content = content

# Solid I

from abc import abstractmethod, ABC


class RunAble(ABC):
    @abstractmethod
    def run(self):
        pass

class FlyAble(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmAble(ABC):
    @abstractmethod
    def swim(self):
        pass

class Lion(RunAble):
    def run(self):
        print('I am running')

# Solid L


class Bird:
    def speak(self):
        print("Tweet!")

class Sparrow(Bird):
    def speak(self):
        print("Sparrow says: Chirp Chirp!")

class Pigeon(Bird):
    def speak(self):
        print("Pigeon says: Chirp Chirp!")

if __name__ == "__main__":
    bird = Bird()
    sparrow = Sparrow()
    pigeon = Pigeon()

    zoo = [bird, sparrow, pigeon]

    for animal in zoo:
        animal.speak()

# Solid O

from abc import abstractmethod, ABC


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPall(PaymentProcessor):
    def pay(self):
        print("PayPal payment processed")
class CreditCard(PaymentProcessor):
    def pay(self):
        print("Credit card payment processed")

class Crypto(PaymentProcessor):
    def pay(self):
        print("Crypto payment processed")

if __name__ == '__main__':
    paypall = PayPall()
    credit_card = CreditCard()
    crypto = Crypto()

    payment_processors = [paypall, credit_card, crypto]

    for payment_processor in payment_processors:
        payment_processor.pay()

# Static Method\ Class Method

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def fahrenheit_to_celsius(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    @classmethod
    def set_fahrenheit(cls,fahrenheit: float):
        return cls(cls.fahrenheit_to_celsius(fahrenheit))

    @property
    def kelvin(self):
        return self.celsius + 273

    def is_freezing(self):
        return self.celsius == 0