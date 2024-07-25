from PySide6.QtWidgets import  QWidget, QVBoxLayout, QPushButton
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QUrl, Signal, Slot
from PySide6.QtMultimedia import QMediaDevices


audio_inputs = QMediaDevices.audioInputs()
audio_outputs = QMediaDevices.audioOutputs()

print("Audio Inputs:", audio_inputs)
print("Audio Outputs:", audio_outputs)

class VideoPlayer(QWidget):
    file_path_updated = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_path = None
        self.player = QMediaPlayer()
        self.video_widget = QVideoWidget()

        self.player.setVideoOutput(self.video_widget)

        self.initUI()
        self.file_path_updated.connect(self.update_file_path)

    def initUI(self):
        layout = QVBoxLayout()

        self.play_button = QPushButton('Play')
        self.play_button.clicked.connect(self.play_video)
        layout.addWidget(self.play_button)
        layout.addWidget(self.video_widget)

        self.setLayout(layout)
        self.setWindowTitle('Video Player')
        self.resize(800, 600)

        
        
    @Slot(str)
    def update_file_path(self, new_file_path):
        self.file_path = new_file_path
        self.player.setSource(QUrl.fromLocalFile(new_file_path))

    def play_video(self):
        if self.file_path:
            print(f"Playing video: {self.file_path}")   
            self.player.play()

