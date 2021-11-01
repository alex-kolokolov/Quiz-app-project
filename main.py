import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def black_or_white(arg: int):
    return 'white' if arg % 2 == 0 else 'black'


def d(arg: list, that_color: list, opponent_color: list, figures: list):
    res = []
    for i in range(arg[0] - 1, arg[0] + 2):
        for j in range(arg[1] - 1, arg[1] + 2):
            posiible_step = True
            diagonal = list(
                filter(lambda x: x[0] + x[1] == i + j or 8 - x[1] + x[0] == 8 - arg[1] + arg[0], that_color))
            x_dim = list(filter(lambda x: x[0] == i, that_color))
            y_dim = list(filter(lambda x: x[1] == j, that_color))

            for ray in diagonal:
                step = []
                x_coords, y_coords = i, j
                if ray[0] > i:
                    step.append(1)
                else:
                    step.append(-1)
                if ray[1] > j:
                    step.append(1)
                else:
                    step.append(-1)
                counter = 0
                l = int(math.sqrt((abs(x_coords - ray[0]) ** 2 + abs(y_coords - ray[1]) ** 2)))
                print(l)
                while [x_coords, y_coords] != list(ray) and ([x_coords, y_coords] in opponent_color or ([x_coords, y_coords] == [i, j] and counter == 0)):
                    counter += 1
                    x_coords += step[0]
                    y_coords += step[1]
                if counter < l or l == 1:
                    posiible_step = False
            for ray in x_dim:
                step = []
                x_coords, y_coords = i, j
                if ray[1] > j:
                    step.append(1)
                else:
                    step.append(-1)
                counter = 0
                l = int(math.sqrt((abs(x_coords - ray[0]) ** 2 + abs(y_coords - ray[1]) ** 2)))
                while [x_coords, y_coords] != list(ray) and ([x_coords, y_coords] in opponent_color or ([x_coords, y_coords] == [i, j] and counter == 0)):
                    counter += 1
                    y_coords += step[0]
                if counter < l or l == 1:
                    posiible_step = False
            for ray in y_dim:
                step = []
                x_coords, y_coords = i, j
                if ray[0] > i:
                    step.append(1)
                else:
                    step.append(-1)
                counter = 0
                x_coords += step[0]
                l = int(math.sqrt((abs(x_coords - ray[0]) ** 2 + abs(y_coords - ray[1]) ** 2)))
                print(l)
                while [x_coords, y_coords] != list(ray) and ([x_coords, y_coords] in opponent_color or ([x_coords, y_coords] == [i, j] and counter == 0)):
                    x_coords += step[0]
                    counter += 1

                if counter < l or l == 0:
                    posiible_step = False
            if len(diagonal) + len(x_dim) + len(y_dim) > 0 and posiible_step:
                res.append([i,  j])


    delimeter = lambda x: [x[0], x[1]] not in that_color and [x[0], x[1]] not in opponent_color
    return list(
        filter(delimeter, res))


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
        self.black_white = {'white': [], 'black': []}
        self.new_game.resize(150, 50)
        self.settings.move(250, 0)
        self.settings.resize(150, 50)
        self.counter = 0
        self.btn4 = QPushButton('123', self)
        self.btn4.move(250, 205)
        self.images = ['wf.png', 'bf.png']
        self.figures = []
        self.predicted = []
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

    def clear_field(self):
        self.black_white = {'white': [], 'black': []}
        for i in range(8):

            for j in range(8):
                self.figures[i][j].setStyleSheet("QPushButton { background-color: green }"
                                                 "QPushButton:hover { background-color: yellow; background-image : "
                                                 "url(bf.png)}")
                print("QPushButton:hover { background-color: yellow; background-image : url(image)".replace(
                    'url(image)', f'url({self.images[0]})'))
                self.figures[i][j].setEnabled(False)

    def predict_step(self):
        for i, j in self.predicted:
            self.figures[i][j].setStyleSheet("QPushButton { background-color: green }"
            "QPushButton:hover { background-color: yellow; background-image : "
            "url(bf.png)}")
            self.figures[i][j].setEnabled(False)
        self.predicted = []
        opponent_color, that_color = self.black_white[black_or_white(self.counter)], \
                                     self.black_white[black_or_white(self.counter + 1 % 2)]
        print('1: ', opponent_color, that_color)
        for enemy in opponent_color:
            try:
                print(d(enemy, that_color=that_color, opponent_color=opponent_color, figures=self.figures))
                for i, j in d(enemy, that_color=that_color, opponent_color=opponent_color, figures=self.figures):
                    self.figures[i][j].setStyleSheet("QPushButton { background-color: yellow }"
                                                           "QPushButton:hover {background-image : url(bf.png)}")
                    self.predicted.append([i, j])
                    self.figures[i][j].setEnabled(True)

            except IndexError:
                print('oops')

    def start_game(self):
        self.clear_field()
        for i in range(3, 5):
            for j in range(3, 5):
                self.figures[i][j].setStyleSheet("QPushButton {background-color: green; background-image : " +
                                                 f"url({self.images[self.counter]})" + "}")
                self.black_white[black_or_white(self.counter)].append([i, j])
                self.counter = (self.counter + 1) % 2
                self.figures[i][j].setEnabled(False)
                print("QPushButton {background-color: green; background-image : " +
                      f"url({self.images[self.counter]})" + "}")
            self.counter = (self.counter + 1) % 2
        self.predict_step()

    def step(self):

        self.counter = (self.counter + 1) % 2
        print(self.sender())
        ind = \
            [[i, _list.index(self.sender())] for i, _list in enumerate(self.figures) if
             self.sender() in self.figures[i]][0]
        self.predicted.remove(ind)
        for i, j in self.predicted:
            if self.figures[i][j].styleSheet() == "QPushButton { background-color: yellow }" + \
                                                           "QPushButton:hover {background-image : url(bf.png)}":
                self.figures[i][j].setStyleSheet("QPushButton { background-color: green }"
                                                       "QPushButton:hover { background-color: yellow;" +
                                                       " background-image : url(bf.png)}")
                self.figures[i][j].setEnabled(False)
        print(self.sender())
        print(self.black_white[black_or_white(self.counter)])
        ind = \
            [[i, _list.index(self.sender())] for i, _list in enumerate(self.figures) if
             self.sender() in self.figures[i]][0]
        color = self.black_white[black_or_white(self.counter)]
        #        print(color[0][1])
        diagonal = list(
            filter(lambda x: x[0] + x[1] == ind[0] + ind[1] or 8 - x[1] + x[0] == 8 - ind[1] + ind[0], color))
        x_dim = list(filter(lambda x: x[0] == ind[0], color))
        y_dim = list(filter(lambda x: x[1] == ind[1], color))
        if len(diagonal) != 0:
            diagonal = set(
                map(lambda x: tuple(x), [min(diagonal, key=lambda x: x[0]), min(diagonal, key=lambda x: x[1]),
                                         max(diagonal, key=lambda x: x[0]), max(diagonal, key=lambda x: x[1])]))
        if len(x_dim) != 0:
            x_dim = set(map(lambda x: tuple(x), [max(x_dim, key=lambda x: x[0]), min(x_dim, key=lambda x: x[0])]))
        if len(y_dim) != 0:
            y_dim = set(map(lambda x: tuple(x), [max(y_dim, key=lambda x: x[0]), min(y_dim, key=lambda x: x[0])]))
        print(x_dim, y_dim)
        print(diagonal)
        for ray in diagonal:
            step = []
            x_coords, y_coords = ind
            if ray[0] > ind[0]:
                step.append(1)
            else:
                step.append(-1)
            if ray[1] > ind[1]:
                step.append(1)
            else:
                step.append(-1)

            while [x_coords, y_coords] != list(ray):
                self.figures[x_coords][y_coords].setStyleSheet \
                    ("QPushButton {background-color: green; background-image : " +
                     f"url({self.images[self.counter]})" + "}")
                if [x_coords, y_coords] not in color:
                    self.black_white[black_or_white(self.counter)].append([x_coords, y_coords])
                    if [x_coords, y_coords] in self.black_white[black_or_white((self.counter + 1) % 2)]:
                        self.black_white[black_or_white((self.counter + 1) % 2)].remove([x_coords, y_coords])
                x_coords += step[0]
                y_coords += step[1]
        for ray in x_dim:
            step = []
            x_coords, y_coords = ind
            if ray[1] > ind[1]:
                step.append(1)
            else:
                step.append(-1)

            while [x_coords, y_coords] != list(ray):
                self.figures[x_coords][y_coords].setStyleSheet \
                    ("QPushButton {background-color: green; background-image : " +
                     f"url({self.images[self.counter]})" + "}")
                if [x_coords, y_coords] not in color and [x_coords, y_coords] != ind:
                    self.black_white[black_or_white(self.counter)].append([x_coords, y_coords])
                    if [x_coords, y_coords] in self.black_white[black_or_white((self.counter + 1) % 2)]:
                        self.black_white[black_or_white((self.counter + 1) % 2)].remove([x_coords, y_coords])
                y_coords += step[0]
        for ray in y_dim:
            step = []
            x_coords, y_coords = ind
            if ray[0] > ind[0]:
                step.append(1)
            else:
                step.append(-1)

            while [x_coords, y_coords] != list(ray):
                self.figures[x_coords][y_coords].setStyleSheet \
                    ("QPushButton {background-color: green; background-image : " +
                     f"url({self.images[self.counter]})" + "}")
                if [x_coords, y_coords] not in color:
                    self.black_white[black_or_white(self.counter)].append([x_coords, y_coords])
                    if [x_coords, y_coords] in self.black_white[black_or_white((self.counter + 1) % 2)]:
                        self.black_white[black_or_white((self.counter + 1) % 2)].remove([x_coords, y_coords])
                x_coords += step[0]

        if ind not in self.black_white[black_or_white(self.counter)]:
            self.black_white[black_or_white(self.counter)].append(ind)
        # i = n - 4,

        self.sender().setStyleSheet("QPushButton {background-color: green; background-image : " +
                                    f"url({self.images[self.counter]})" + "}")
        self.sender().setEnabled(False)
        self.predict_step()
        print(self.black_white)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
