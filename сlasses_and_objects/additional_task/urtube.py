from time import sleep
from user import User
from video import Video


class Urtube:
    def __init__(self, users=None, videos=None, current_user=None):
        if videos is None:
            videos = []
        if users is None:
            users = []
        self.current_user = current_user if isinstance(current_user, User) else None
        if isinstance(users, list) and all(isinstance(user, User) for user in users):
            self.users = users
        else:
            raise ValueError("Unexpected type")
        if isinstance(videos, list) and all(isinstance(video, Video) for video in videos):
            self.videos = videos
        else:
            raise ValueError("Unexpected type")

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
        return f"Пользователь {nickname} не найден или вы ввели не верный пароль."

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user
        return

    def log_out(self):
        self.current_user = None
        return

    def add(self, *args: Video):
        for new_video in args:
            if self.videos:
                for old_video in self.videos:
                    if old_video.title != new_video.title:
                        self.videos.append(new_video)
            else:
                self.videos.append(new_video)
        return

    def get_videos(self, search_word: str):
        videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                videos.append(video)
        return videos

    def watch_video(self, title: str):
        if self.current_user is not None:
            search_video = None
            for video in self.videos:
                if video.title == title:
                    search_video = video
            if search_video is not None:
                if self.current_user.age >= 18:
                    for i in range(search_video.time_now, search_video.duration + 1):
                        search_video.time_now += 1
                        print(i)
                        sleep(1)
                    search_video.time_now = 0
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                return
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
        return
