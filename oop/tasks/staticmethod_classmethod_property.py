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