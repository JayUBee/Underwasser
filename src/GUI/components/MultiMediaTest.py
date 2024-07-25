import sys
import cv2
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QTimer, QThread, pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, video_source):
        super().__init__()
        self.video_source = video_source
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(self.video_source)
        while self._run_flag:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                p = convert_to_Qt_format.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class MediaPlayerTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Player Test")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.video_label = QLabel()
        self.layout.addWidget(self.video_label)

        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

        self.thread = None

    def open_file(self):
        video_source = "C:/Users/Ismail/Desktop/supplement/video.wmv"
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