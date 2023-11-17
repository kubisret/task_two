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
        self.spis_elips = []

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

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)

            for circle in self.spis_elips:
                qp.drawEllipse(circle)
            qp.end()
        self.flag = False

    def draw_flag(self, qp):
        random_size, random_x, random_y = self.random_size_and_coor()

        qp.setBrush(QColor(210, 240, 17))
        elips = QRectF(random_x, random_y, random_size, random_size)
        self.spis_elips.append(elips)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())