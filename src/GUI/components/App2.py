import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import  QPixmap
from VideoThread import VideoThread
from openFile import OpenFileButton


class MediaPlayerTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.video_label = QLabel()
        self.layout.addWidget(self.video_label)

        self.open_button = QPushButton()
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

        self.thread = None

    def open_file(self):
        video_source = "path_to_your_video_file.mp4"
        if self.thread is not None:
            self.thread.stop()
        self.thread = VideoThread(video_source)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def update_image(self, cv_img):
        self.video_label.setPixmap(QPixmap.fromImage(cv_img))

    def closeEvent(self, event):
        if self.thread is not None:
            self.thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPlayerTest()
    window.show()
    sys.exit(app.exec())