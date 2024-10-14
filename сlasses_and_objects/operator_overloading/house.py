class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other: 'House'):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other: 'House'):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other: 'House'):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other: 'House'):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other: 'House'):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other: 'House'):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value: int):
        self.number_of_floors += value
        return self

    def __radd__(self, value: int):
        return self.__add__(value)

    def __iadd__(self, value: int):
        return self.__add__(value)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)
        return
