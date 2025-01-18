from threading import Thread
import time


class Knight(Thread):
    total_enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")

        while self.total_enemies > 0:
            time.sleep(1)
            days += 1

            if self.total_enemies > 0:
                enemies_defeated = min(self.power, self.total_enemies)
                self.total_enemies -= enemies_defeated
                print(f"{self.name} сражается {days} день(дня)..., осталось {self.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")
