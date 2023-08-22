from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import sys

__version__ = 'v1.1'
__author__ = 'Abrar'


class YoutubeMediaPlayer(QWidget):
    def __init__(self, video_id, parent=None):
        super().__init__()
        self.parent = parent
        self.video_id = video_id

        default_setting = QWebEngineSettings.globalSettings()
        default_setting.setFontSize(QWebEngineSettings.MinimumFontSize, 25)

        self.layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        label = QLabel("Enter Video Id: ")
        self.input = QLineEdit()
        self.installEventFilter(self)
        self.input.setText(self.video_id)
        top_layout.addWidget(label, 1)
        top_layout.addWidget(self.input, 9)
        self.layout.addLayout(top_layout)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        button_layout = QHBoxLayout()
        self.layout.addLayout(button_layout)
        button_update = QPushButton('Update', clicked=self.update_video)
        button_remove = QPushButton('Delete', clicked=self.remove_player)
        button_layout.addWidget(button_update)
        button_layout.addWidget(button_remove)

        self.update_video()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.update_video()
        return super().eventFilter(source, event)

    def update_video(self):
        video_id = self.input.text()
        self.web_view.setUrl(QUrl(f'https://www.youtube.com/embed/{video_id}?rel=0'))

    def remove_player(self):
        self.setParent(None)
        self.deleteLater()
        self.parent.organize_layout()


class PlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Media Player")
        self.setMinimumSize(500, 250)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        button_add_player = QPushButton('Add Player', clicked=self.add_player)
        self.layout.addWidget(button_add_player)

        self.video_grid = QGridLayout()
        self.layout.addLayout(self.video_grid)

        self.player = YoutubeMediaPlayer('raTMa8MneTY', parent=self)
        self.video_grid.addWidget(self.player, 0, 0)

        self.layout.addWidget(QLabel(f"{__version__} by {__author__}"), alignment=Qt.AlignBottom | Qt.AlignRight)

        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                height: 22;
                width: 22px;
                background-color: gray;
                color: white;
            }
            * {
                background-color: lightgray;
            }
            QLineEdit {
                background-color: white;
            }
        """)

    def add_player(self):
        player_count = self.video_grid.count()
        row = player_count % 3
        col = player_count // 3

        self.player = YoutubeMediaPlayer('', parent=self)
        self.video_grid.addWidget(self.player, row, col)

    def organize_layout(self):
        player_count = self.video_grid.count()
        players = []

        for i in reversed(range(player_count)):
            player = self.video_grid.itemAt(i).widget()
            players.append(player)

        for index, player in enumerate(players):
            self.video_grid.addWidget(player, index % 3, index // 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlayerWindow()
    window.show()
    sys.exit(app.exec_())
