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