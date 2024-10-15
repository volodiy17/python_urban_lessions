class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now if isinstance(time_now, int) and time_now >= 0 else 0
        if isinstance(adult_mode, bool):
            self.adult_mode = adult_mode
        else:
            raise ValueError("Unexpected adult_mode type, expected bool")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title