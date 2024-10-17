from animal import Animal


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
            return
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")
            return
