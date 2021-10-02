from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
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
        
    def run(self):
        create_dr(1000, int(self.line_edit.text()))
        ex.load_image('image.jpg')



class secondW(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Тест')
        self.setGeometry(200, 200, 300, 300)
        self.initUi()

    def initUi():
        self.line_edit = QLineEdit(self)
        self.btn = QPushButton('go', self)
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
    ep = secondW()
    create_dr(1000, 20)
    ex.load_image('image.jpg')
    ex.show()
    ep.show

    sys.exit(app.exec_())
