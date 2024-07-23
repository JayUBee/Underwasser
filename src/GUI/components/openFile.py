from PySide6.QtWidgets import QPushButton, QFileDialog
from PySide6.QtGui import QFont

class OpenFileButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Open File", parent)
        self.clicked.connect(self.open_file)
        self.set_style()

    def set_style(self):
        self.setFixedSize(150, 50)
        self.setFont(QFont("Arial", 14))
        self.setStyleSheet("background-color: lightblue; color: black; border-radius: 10px;")

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            print(f"Selected file: {file_path}")