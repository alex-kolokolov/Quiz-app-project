import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Реверси')
        self.btn = QPushButton('Рисовать', self)
        self.btn2 = QPushButton('Рисовать круг', self)
        self.btn2.move(150, 150)
        self.do_paint = False
        self.do_white = False
        self.btn.clicked.connect(self.paint)
        self.btn2.clicked.connect(self.paint_ellipse)
        self.buttons = []
        self.counter = 0
        self.btn4 = QPushButton('123', self)
        self.btn4.move(250, 205)
        self.images = ['wf.png', 'bf.png']
        self.figures = []
        for i in range(8):
            a = []
            for j in range(8):
                # qp.drawRect(50 * i, 50 * j, 50, 50)
                self.btn3 = QPushButton(self)
                self.btn3.setText('')
                self.btn3.resize(50, 50)
                self.btn3.move(50 * j, 50 * i)
                self.btn3.setStyleSheet("QPushButton { background-color: green }"
                                        "QPushButton:hover { background-color: yellow; background-image : url(bf.png)}")
                print("QPushButton:hover { background-color: yellow; background-image : url(image)".replace(
                    'url(image)', f'url({self.images[0]})'))
                a.append(self.btn3)

                print(self.btn3.pos())
                self.btn3.clicked.connect(self.paint_ellipse)
            self.figures.append(a)
        for i in range(3, 5):
            for j in range(3, 5):
                self.figures[i][j].setStyleSheet("QPushButton {background-color: green; background-image : " +
                                    f"url({self.images[self.counter]})" + "}")
                self.counter = (self.counter + 1) % 2
                self.figures[i][j].setEnabled(False)
                print("QPushButton {background-color: green; background-image : " +
                f"url({self.images[self.counter]})" + "}")
            self.counter = (self.counter + 1) % 2


    def paintEvent(self, event):
        if self.do_white:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(self.btn3)
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):

        print(self.sender())
        self.do_paint = True
        self.repaint()

    def paint_ellipse(self):
        self.counter = (self.counter + 1) % 2
        print(self.sender())
        self.sender().setStyleSheet("QPushButton {background-color: green; background-image : " +
                                    f"url({self.images[self.counter]})" + "}")
        self.sender().setEnabled(False)


    def draw_flag(self, qp):
        qp.setBrush(QColor(0, 75, 0))

        for i in range(8):
            for j in range(8):
                qp.drawRect(50 * i, 50 * j, 50, 50)

    #        qp.setBrush(QColor(255, 255, 255))
    #        qp.drawEllipse(203, 203, 45, 45)

    def draw_ellipse(self, qp):
        if self.counter % 2 == 0:
            qp.setBrush(QColor(0, 0, 0))
        else:
            pass
            # self.btn3.setBrush(QColor(255, 255, 255))
        self.btn3.drawEllipse(self.position.x(), self.position.y(), 45, 45)
        print(self.counter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
