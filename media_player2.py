
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

video_path = "Pardes-Katenda.mp4"


class MediaPlayer(App):
    def __init__(self, v_path):
        super().__init__()
        self.v_path = v_path

    def build(self):
        player = VideoPlayer(source=self.v_path, state='play')

        return player


if __name__ == "__main__":
    MediaPlayer(video_path).run()
