from PyQt6 import QtWidgets, uic


# Define a function that will be called when the button is clicked
def on_button_click():
    print("Button was clicked!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()

    uic.loadUi('main_ui.ui', window)
    window.show()

    # Connect the button's click event to the function
    window.pushButton.clicked.connect(on_button_click)

    sys.exit(app.exec())