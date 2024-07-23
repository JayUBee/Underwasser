from PySide6 import QtCore, QtWidgets
from components.openFile import OpenFileButton





class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #add components here
        self.openFile= OpenFileButton()
        
        
        
        
        layout = QtWidgets.QVBoxLayout()
        
        #show components here
        layout.addWidget(self.openFile)
        
        
        
        self.setLayout(layout)
        self.setWindowTitle("File Opener")
        self.setGeometry(100, 100, 300, 200)


