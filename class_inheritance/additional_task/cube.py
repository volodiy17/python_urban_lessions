from figure import Figure


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color: list | tuple, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        if len(__sides) != 1:
            self.set_sides(1 for i in range(self.sides_count))
        else:
            self.set_sides(__sides[0] for i in range(self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3
