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
class History:
    def __init__(self):
        self._calculations = []

    def add(self, calculation):
        self._calculations.append(calculation)

    def get_all(self):
        return list(self._calculations)

    def remove(self, index):
        return self._calculations.pop(index)

    def clear(self):
        self._calculations.clear()