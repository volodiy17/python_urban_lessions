class Eagle:
    def __init__(self, y_distance=0, sound="I train, eat, sleep, and repeat"):
        self.y_distance = y_distance if isinstance(y_distance, int) else int(y_distance)
        self.sound = sound if isinstance(sound, str) else str(sound)

    def fly(self, dy: int):
        self.y_distance += dy
        return
