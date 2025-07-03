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