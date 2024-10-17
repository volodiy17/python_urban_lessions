class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance if isinstance(x_distance, int) else int(x_distance)
        self.sound = sound if isinstance(sound, str) else str(sound)

    def run(self, dx: int):
        self.x_distance += dx
        return
