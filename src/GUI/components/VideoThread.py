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
                p = convert_to_Qt_format.scaled(400, 200, Qt.AspectRatioMode.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()
