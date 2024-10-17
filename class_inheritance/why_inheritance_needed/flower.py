from plant import Plant


class Flower(Plant):
    def __init__(self, name: str, edible = False):
        super().__init__(name, edible)
        self.edible = edible