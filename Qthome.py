from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Img_create import create_dr


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Тест')
        self.setGeometry(200, 200, 300, 300)
        self.label = QLabel(self)

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())


class WindowGif(QDialog):
    def __init__(self, parent = None):
        super().__init__()                       
        self.parent = parent
        self.initUI()
        self.setWindowTitle('Settings')
        self.setGeometry(0, 200, 200, 100)

    def initUI(self):
        self.line_edit = QLineEdit(self)
        self.line_edit.move(0, 5)
        self.btn = QPushButton('go', self)
        self.initUi()

    def initUi(self):
        self.btn.move(125, 0)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.run)

    def run(self):
        try:
            create_dr(1000, int(self.line_edit.text()))
            ex.load_image('image.jpg')
            ex.show()
        except ValueError as ve:
            create_dr(1000, 20)
            ex.load_image('image.jpg')
            ex.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    ex = App()
    ep = WindowGif()
    create_dr(1000, 20)
    ex.load_image('image.jpg')
    ex.show()
    ep.show()

    sys.exit(app.exec_())
