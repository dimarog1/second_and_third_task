import math
import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui')
        self.resize(1343, 977)
        self.setWindowTitle('Супрематизм')
        self.initUi()
        self.setMouseTracking(True)

    def initUi(self):
        self.paint = False
        self.x = 0
        self.y = 0
        self.side = 0
        self.figure = ''

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.RightButton:
            self.figure = 'square'
        elif event.button() == Qt.LeftButton:
            self.figure = 'ellipse'
        self.draw()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figure = 'triangle'
            self.draw()

    def draw(self):
        width = self.width()
        random_w_h = random.randint(5, int(width * 0.2))
        self.side = random_w_h
        self.paint = True
        self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setPen(QColor(r, g, b))
        qp.setBrush(QBrush(QColor(r, g, b)))
        if self.paint and self.figure == 'square':
            qp.drawRect(self.x - self.side // 2, self.y - self.side // 2, self.side, self.side)
        elif self.paint and self.figure == 'ellipse':
            qp.drawEllipse(self.x - self.side // 2, self.y - self.side // 2, self.side, self.side)
        elif self.paint and self.figure == 'triangle':
            d = self.side * math.tan(math.radians(30))

            pos_top = QPointF(self.x, self.y)
            pos_left = QPointF(self.x - d, self.y + self.side)
            pos_right = QPointF(self.x + d, self.y + self.side)
            qp.drawPolygon(pos_top,
                           pos_left,
                           pos_right)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
