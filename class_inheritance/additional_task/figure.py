class Figure:
    sides_count = 0

    def __init__(self, __color: list | tuple, *__sides, filled=False):
        if all(isinstance(side, int) for side in __sides):
            self.__sides = list(__sides)
        else:
            raise ValueError('All sides must be integers')
        if isinstance(__color, (list, tuple)) and len(__color) == 3 and self.__is_valid_color(*__color):
            self.__color = list(__color)
        else:
            raise ValueError('All colors must be RGB')
        if isinstance(filled, bool):
            self.__filled = filled
        else:
            raise ValueError('All filled must be boolean')

    def get_color(self):
        return self.__color

    def is_filled(self):
        return self.__filled

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
                return True
        return False

    def set_color(self, r, g, b):
        self.__color = [r, g, b] if self.__is_valid_color(r, g, b) else self.__color

    def __is_valid_sides(self, *args):
        return True if all(isinstance(arg, int) for arg in args) and len(args) == len(self.__sides) else False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.__sides = list(new_sides) if len(new_sides) == self.sides_count else self.__sides
