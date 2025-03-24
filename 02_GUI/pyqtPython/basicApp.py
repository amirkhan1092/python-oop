import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("PyQt6 Basic App")
        self.setGeometry(100, 100, 300, 200)


        # Create a button
        self.button = QPushButton("Click Me!", self)
        self.button.clicked.connect(self.on_button_click)

        # Layout to organize widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        self.button.setText("Clicked!")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
