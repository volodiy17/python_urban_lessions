from figure import Figure
import math


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: list | tuple, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        if len(__sides) != self.sides_count:
            self.set_sides(1)
        else:
            self.set_sides(*__sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2
