import sys
import os
import tempfile
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget
from pytube import YouTube


class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video Player")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

        self.url_input = QLineEdit("https://www.youtube.com/watch?v=lcODEpLgrJg")
        layout.addWidget(self.url_input)

        self.load_button = QPushButton("Play Video")
        layout.addWidget(self.load_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_button.clicked.connect(self.load_video)

    def load_video(self):
        video_url = self.url_input.text()
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()

        temp_dir = tempfile.mkdtemp()
        video_path = os.path.join(temp_dir, f"{yt.title}.mp4")
        video_stream.download(temp_dir)

        media_url = QUrl.fromLocalFile(video_path)
        media_content = QMediaContent(media_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()


def main():
    app = QApplication(sys.argv)
    window = VideoPlayerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
