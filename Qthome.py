from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from Img_create import create_dr


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Тест')
        self.setGeometry(200, 200, 300, 300)
        self.label = QLabel(self)
        self.line_edit = QLineEdit(self)
        self.btn = QPushButton('go', self)
        self.initUi()

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())

    def initUi(self):
        self.btn.move(0, 20)
        self.btn.clicked.connect(self.run)

    def run(self):
        create_dr(1000, int(self.line_edit.text()))
        ex.load_image('image.jpg')
        ex.show()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    ex = App()
    create_dr(1000, 20)
    ex.load_image('image.jpg')
    ex.show()

    sys.exit(app.exec_())
