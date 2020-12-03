import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from random import randint


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.n = 0

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.resize(100, 25)
        self.btn.setText('Нарисовать')


class Ellipse(Form):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        r = randint(10, 300)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(randint(1, 500 - r), randint(1, 500 - r), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipse()
    ex.show()
    sys.exit(app.exec())