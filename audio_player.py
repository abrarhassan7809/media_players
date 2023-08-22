from kivy.app import App
from kivy.core.audio import SoundLoader

audio_path = 'Pardes-Katenda.mp4'


class MediaPlayer(App):
    def __init__(self, source_path):
        super().__init__()
        self.source_path = source_path

    def build(self):
        self.playe_audio = SoundLoader.load(self.source_path)
        self.playe_audio.play()


if __name__ == "__main__":
    MediaPlayer(audio_path).run()
