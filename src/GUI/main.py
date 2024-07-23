import sys
from PySide6 import QtWidgets
from  App import App

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QApplication
    window = App()  # Create an instance of your application
    window.show()  # Show the application window
    sys.exit(app.exec())  # Start the event loop

        