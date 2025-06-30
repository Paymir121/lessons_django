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