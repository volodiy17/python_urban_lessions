from eagle import Eagle
from horse import Horse


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)
        return

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)
        return
