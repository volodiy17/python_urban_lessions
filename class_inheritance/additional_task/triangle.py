from figure import Figure
import math


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color: list | tuple, *__sides, filled=False):
        super().__init__(__color,*__sides, filled=filled)
        if len(__sides) != self.sides_count:
            self.set_sides(1 for i in range(self.sides_count))
        else:
            self.set_sides(*__sides)

    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
