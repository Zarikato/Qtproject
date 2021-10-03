from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Img_create import StarDraw


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Тест')
        self.setGeometry(300, 200, 300, 300)
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
        self.setGeometry(0, 200, 300, 100)

    def initUI(self):
        self.line_edit = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit3 = QLineEdit(self)
        self.btn = QPushButton('go', self)
        self.labelstp = QLabel('STEP', self)
        self.labelx = QLabel('SET X', self)
        self.labely = QLabel('SET Y', self)
        self.initUi()

    def initUi(self):
        self.line_edit.move(50, 5)
        self.line_edit2.move(50, 30)
        self.line_edit3.move(50, 55)
        self.labelstp.move(0, 5)
        self.labelx.move(0, 30)
        self.labely.move(0, 55)
        self.btn.move(175, 0)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.run)

    def run(self):
        try:
            sr.set_stp(int(self.line_edit.text()))
            sr.set_x(int(self.line_edit2.text()))
            sr.set_y(int(self.line_edit3.text()))
            sr.create_dr()
            ex.load_image('image.jpg')
            ex.show()
        except ValueError as ve:
            ex.load_image('image.jpg')
            ex.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    ex = App()
    sr = StarDraw((1000, 1000), 20)
    sr.create_dr()
    ep = WindowGif()
    ex.load_image('image.jpg')
    ex.show()
    ep.show()

    sys.exit(app.exec_())
