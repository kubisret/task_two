import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Рисование окружностей')

        self.flag = False
        self.push_generate.clicked.connect(self.flagEvent)

    def flagEvent(self):
        self.flag = True
        self.update()

    def random_size_and_coor(self):
        range_size = range(500)
        random_size = random.choice(range_size)
        range_x = range(250)
        random_x = random.choice(range_x)
        range_y = range(250)
        random_y = random.choice(range_y)

        return random_size, random_x, random_y

    def random_color(self):
        rgb = random.choice(range(255)), random.choice(range(255)), random.choice(range(255))
        return rgb

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.flag = False

    def draw_flag(self, qp):
        random_size, random_x, random_y = self.random_size_and_coor()
        print(random_x)
        rgb = self.random_color()
        qp.setBrush(QColor(*rgb))
        rect = QRectF(random_x, random_y, random_size, random_size)
        qp.drawEllipse(random_x, random_y, random_size, random_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())