from PyQt6 import QtWidgets, uic

# Define a MainWindow class that inherits from QMainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        uic.loadUi('main_ui.ui', self)

        # Connect the button click event to a method
        self.pushButton.clicked.connect(self.on_button_click)

    # Define a method to be called when the button is clicked
    def on_button_click(self):
        print("Button from the UI was clicked!")


if __name__ == "__main__":
    import sys

    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create an instance of the MainWindow class
    window = MainWindow()

    # Show the main window
    window.show()

    # Run the application's event loop
    sys.exit(app.exec())
