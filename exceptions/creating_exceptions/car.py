from IncorrectVinNumberException import IncorrectVinNumber
from IncorrectCarNumbersException import IncorrectCarNumbers


class Car:
    model = str
    __vin = int
    __numbers = str

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin if Car.__is_valid_vin(vin) else None
        self.__numbers = numbers if Car.__is_valid_numbers(numbers) else None

    @staticmethod
    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int):
            if vin_number in range(1000000, 9999999):
                return True
            else:
                raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            raise IncorrectVinNumber("Некорректный тип vin номер")

    @staticmethod
    def __is_valid_numbers(numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers("Неверная длина номера")
        else:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
