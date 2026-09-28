from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def calculate(self):
        pass


class Add(Calculation):
    def calculate(self):
        return self.a + self.b


class Subtract(Calculation):
    def calculate(self):
        return self.a - self.b