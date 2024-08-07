import sys
from PySide6.QtWidgets import QApplication
from  App import App

if __name__ == "__main__":

    app =QApplication(sys.argv)  # Create an instance of QApplication
    window = App()  # Create an instance of your application
    window.show()  # Show the application window
    sys.exit(app.exec())  # Start the event loop

        