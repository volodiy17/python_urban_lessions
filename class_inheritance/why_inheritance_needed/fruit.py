from plant import Plant


class Fruit(Plant):
    def __init__(self, name: str, edible = True):
        super().__init__(name, edible)
        self.edible = edible