# Import necessary modules from PyQt6
from PyQt6 import QtWidgets, uic

# Standard Python entry point for the application
if __name__ == "__main__":
    # Import the sys module to handle system-level operations
    import sys

    # Create an application object
    app = QtWidgets.QApplication(sys.argv)

    # Create a main window object using QMainWindow
    window = QtWidgets.QMainWindow()

    # Load the user interface (UI) from a .ui file using uic.loadUi if the file is available
    # The .ui file would typically be created with Qt Designer and contains the layout of the window
    uic.loadUi('main_ui.ui', window)

    # Display the main window on the screen
    window.show()

    # Start the application's event loop to process user input and GUI events
    sys.exit(app.exec())