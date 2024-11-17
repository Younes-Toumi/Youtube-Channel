# Import necessary modules from PyQt6
from PyQt6 import QtWidgets # QtWidgets: Provides tools for creating window elements like buttons and text boxes

# Standard Python entry point for the application
if __name__ == "__main__":
    # Import the sys module to handle system-level operations
    import sys

    # Create an application object, which is responsible for managing the GUI application's control flow
    # `sys.argv` allows the app to handle command-line arguments if provided
    app = QtWidgets.QApplication(sys.argv)

    # Create a main window object using QMainWindow
    # QMainWindow provides a standard window with a title bar, menu bar, status bar, etc.
    window = QtWidgets.QMainWindow()

    # Display the main window on the screen
    window.show()

    # Start the application's event loop to process user input and GUI events
    # The app.exec() method runs the main loop and waits until `exit()` is called or the main window is closed
    # `sys.exit()` ensures a clean exit of the application with the return status of the event loop
    sys.exit(app.exec())