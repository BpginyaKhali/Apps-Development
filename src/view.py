import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class View:
    def __init__(self):
        self.widget = QWidget()

    def start_button_clicked(self):
        if self.start_button.get
        pass

    def create_start_stop_button(self, widget):
        self.start_button = QPushButton('Start', widget)
        self.start_button.setToolTip('This is an example button')
        self.start_button.clicked.connect(self.start_button_clicked)




    def window():
        app = QApplication(sys.argv)
        widget = QWidget()

        textLabel = QLabel(widget)
        textLabel.setText("Hello World!")
        textLabel.move(1000, 1000)

        button = QPushButton('PyQt5 button', widget)
        button.setToolTip('This is an example button')
        button.move(100, 70)

        button.clicked.connect(lambda: button.setText("Hello!"))

        widget.setGeometry(100, 50, 320, 700)
        widget.setWindowTitle("PyQt5 Example")
        widget.show()
        sys.exit(app.exec_())