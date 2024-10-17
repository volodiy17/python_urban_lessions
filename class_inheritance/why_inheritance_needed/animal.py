class Animal:
    def __init__(self, name: str, alive = True, fed = False):
        self.name = name
        self.alive = alive if isinstance(alive, bool) else True
        self.fed = fed if isinstance(fed, bool) else False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name