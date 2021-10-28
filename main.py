import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle('Реверси')
        self.new_game = QPushButton('Новая игра', self)
        self.settings = QPushButton('Настройки', self)
        self.new_game.clicked.connect(self.start_game)
        self.new_game.resize(150, 50)
        self.settings.move(250, 0)
        self.settings.resize(150, 50)
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
                self.btn3.move(50 * j, 200 + 50 * i)
                self.btn3.setStyleSheet("QPushButton { background-color: green }"
                                        "QPushButton:hover { background-color: yellow; background-image : url(bf.png)}")
                print("QPushButton:hover { background-color: yellow; background-image : url(image)".replace(
                    'url(image)', f'url({self.images[0]})'))
                a.append(self.btn3)
                self.btn3.setEnabled(False)
                self.btn3.clicked.connect(self.step)
                print(self.btn3.pos())

            self.figures.append(a)


    def start_game(self):
        for i in range(8):
            for j in range(8):
                self.figures[i][j].setEnabled(True)
        for i in range(3, 5):
            for j in range(3, 5):
                self.figures[i][j].setStyleSheet("QPushButton {background-color: green; background-image : " +
                                    f"url({self.images[self.counter]})" + "}")
                self.counter = (self.counter + 1) % 2
                self.figures[i][j].setEnabled(False)
                print("QPushButton {background-color: green; background-image : " +
                f"url({self.images[self.counter]})" + "}")
            self.counter = (self.counter + 1) % 2

    def step(self):
        self.counter = (self.counter + 1) % 2
        print(self.sender())
        self.sender().setStyleSheet("QPushButton {background-color: green; background-image : " +
                                    f"url({self.images[self.counter]})" + "}")
        self.sender().setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
