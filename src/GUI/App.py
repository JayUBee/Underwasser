from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from components.openFile import OpenFileButton
from components.videoPlayer import VideoPlayer

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.videoPlayer = VideoPlayer(self)
        self.openFileButton = OpenFileButton(self, self.videoPlayer)
        self.openFileButton.file_selected.connect(self.update_ui)

        self.fileLabel = QLabel("No file selected")
        layout.addWidget(self.openFileButton)
        layout.addWidget(self.fileLabel)
        layout.addWidget(self.videoPlayer)

        self.setLayout(layout)
        self.setWindowTitle('Video Player')
        self.resize(800, 600)

    def update_ui(self, file_path):
        self.fileLabel.setText(f"Selected file: {file_path}")