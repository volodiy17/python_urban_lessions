class Plant:
    def __init__(self, name: str, edible = False):
        self.name = name
        self.edible = edible if isinstance(edible, bool) else False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name