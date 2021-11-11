import sys
import math
import time
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ai import RandomBot
from results import Results
from settings import Settings


def black_or_white(arg: int):
    return 'white' if arg % 2 == 0 else 'black'


def d(arg: list, that_color: list, opponent_color: list, figures: list):
    result_coordinates, coordinates = dict(), []
    for i in range(arg[0] - 1, arg[0] + 2):
        for j in range(arg[1] - 1, arg[1] + 2):
            possible_step = []
            diagonal = list(
                filter(lambda x: (x[0] + x[1] == i + j or 8 - x[1] + x[0] == 8 - j + i), that_color))
            x_dim = list(filter(lambda x: x[0] == i, that_color))
            y_dim = list(filter(lambda x: x[1] == j, that_color))

            for dimension in [diagonal, x_dim, y_dim]:
                for ray in dimension:

                    step = []
                    x_coords, y_coords = i, j
                    if ray[0] > i:
                        step.append(1)
                    elif ray[0] == i:
                        step.append(0)
                    else:
                        step.append(-1)
                    if ray[1] > j:
                        step.append(1)
                    elif ray[1] == j:
                        step.append(0)
                    else:
                        step.append(-1)
                    steps = int(math.sqrt((abs(x_coords - ray[0]) ** 2 + abs(y_coords - ray[1]) ** 2)))
                    while [x_coords, y_coords] != list(ray) and (
                            [x_coords, y_coords] in opponent_color or (
                            [x_coords, y_coords] == [i, j] and len(coordinates) == 0)):
                        coordinates.append([x_coords, y_coords])
                        x_coords += step[0]
                        y_coords += step[1]
                    if [x_coords, y_coords] != list(ray) and len(coordinates) < steps or steps == 1:
                        possible_step.append(False)
                    else:
                        possible_step.append(True)
                    if possible_step[-1]:
                        if (not ([x_coords, y_coords] != list(ray) and len(coordinates) < steps or steps == 0)) and \
                                0 <= coordinates[0][0] < 8 and 0 <= coordinates[0][1] < 8:

                            if not (coordinates[0] in that_color or coordinates[0] in opponent_color or [x_coords,
                                                                                                         y_coords] != list(
                                ray) and len(coordinates) < steps or steps == 0):
                                available_step = tuple(coordinates[0])
                                if available_step in result_coordinates:
                                    result_coordinates[available_step] += coordinates[1:]
                                else:
                                    result_coordinates[available_step] = coordinates[1:]
                    coordinates = []

    return result_coordinates


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle('Реверси')
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.game_mode = GameMode()
        buttons_layout = QHBoxLayout()
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(grid_layout)
        self.results = Results()
        self.setLayout(main_layout)
        grid_layout.addLayout(buttons_layout, 0, 0)
        self.last_games = QPushButton('Результаты игр', self)
        self.new_game = QPushButton('Новая игра', self)
        self.settings = QPushButton('Настройки', self)
        self.new_game.clicked.connect(self.mode_select)
        self.last_games.clicked.connect(self.show_results)
        self.settings.clicked.connect(self.settings_method)
        self.black_white = {'white': [], 'black': []}
        self.new_game.resize(150, 50)
        self.settings.move(250, 0)
        self.settings.resize(150, 50)
        self.last_step_button = QPushButton('⮌', self)
        self.last_step_button.resize(50, 50)
        self.last_step_button.clicked.connect(self.previous_step)
        self.last_step_button.move(100, 130)
        self.counter = 0
        self.images = ['wf.png', 'bf.png']
        self.figures = []
        self.predicted = []
        self.stack_of_steps = {"predicted": [], "figures": [], "available_steps": []}
        #       print(self.stack_of_steps["available_steps"])
        self.no_steps = False
        self.with_ai = False
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Уведомдение")
        self.msg.setText("Игра окончена")
        self.styles = {"default": "QPushButton {background-color: green}",
                       "white_clicked": "QPushButton {background-color: green; image : url(wf.png)}",
                       "black_clicked": "QPushButton {background-color: green; image : url(bf.png)}",
                       "white_available": "QPushButton {background-color: yellow } "
                                          "QPushButton:hover {image : url(wf.png)}",
                       "black_available": "QPushButton {background-color: yellow } "
                                          "QPushButton:hover {image : url(bf.png)}"
                       }
        self.msg.setIcon(QMessageBox.Warning)
        buttons_layout.addWidget(self.new_game)
        buttons_layout.addWidget(self.settings)
        buttons_layout.addWidget(self.last_step_button)
        buttons_layout.addWidget(self.last_games)
        self.available_steps = dict()
        self.ai = RandomBot()

        for i in range(8):
            a = []
            for j in range(8):
                # qp.drawRect(50 * i, 50 * j, 50, 50)
                self.btn3 = QPushButton(self)
                self.btn3.setText('')
                self.btn3.setStyleSheet(self.styles["default"])
                policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

                policy.setHeightForWidth(True)
                self.btn3.setMinimumSize(80, 80)
                self.btn3.heightForWidth(self.btn3.height())
                policy.setWidthForHeight(True)
                self.btn3.setSizePolicy(policy)
                a.append(self.btn3)

                self.btn3.setEnabled(False)
                self.btn3.clicked.connect(self.step)
                self.btn3.y = i
                self.btn3.x = j
                grid_layout.addWidget(self.btn3, i, j, 1, 1)

            self.figures.append(a)

    def settings_method(self):
        self.settings_object = Settings()
        self.settings_object.show()

    def show_results(self):
        self.results = Results()
        self.results.show()

    def mode_select(self):
        self.game_mode.show()
        self.with_ai = self.game_mode.is_with_ai
        self.reset_game()

    def render_field(self):
        for i in range(8):

            for j in range(8):
                self.figures[i][j].setStyleSheet(self.styles["default"])

                self.figures[i][j].setEnabled(False)
        for color in self.black_white.keys():
            for x, y in self.black_white[color]:
                self.figures[x][y].setStyleSheet(self.styles[color + "_clicked"])
        print(self.predicted)
        for x, y in self.predicted:
            try:
                self.figures[x][y].setStyleSheet(self.styles[black_or_white(self.counter + 1 % 2) + "_available"])
                self.figures[x][y].setEnabled(True)
            except IndexError:
                print('ooops')

    def previous_step(self):
        if len(self.stack_of_steps['figures']) > 1:
            self.stack_of_steps["figures"].pop()
            self.stack_of_steps["predicted"].pop()
            self.stack_of_steps["available_steps"].pop()
            print(self.stack_of_steps["available_steps"])
            if not self.game_mode.is_with_ai:
                self.counter = (self.counter - 1) % 2

            self.predicted = self.stack_of_steps["predicted"][-1][0]
            self.black_white = self.stack_of_steps["figures"][-1][0]
            self.black_white = {'white': self.stack_of_steps["figures"][-1][0][:],
                                'black': self.stack_of_steps["figures"][-1][1][:]}
            self.available_steps = self.stack_of_steps["available_steps"][-1]
            self.render_field()
        else:
            self.reset_game()

    def reset_game(self):
        self.predicted = []
        self.stack_of_steps = {"predicted": [], "figures": [], "available_steps": []}
        self.black_white = {'white': [], 'black': []}
        self.start_game()

    def predict_step(self, enemy=None):
        self.predicted = []
        self.available_steps = dict()
        opponent_color, that_color = self.black_white[black_or_white(self.counter)], \
                                     self.black_white[black_or_white(self.counter + 1 % 2)]

        for enemy in opponent_color:
            try:
                a = d(enemy, that_color=that_color, opponent_color=opponent_color, figures=self.figures)
                for i, j in d(enemy, that_color=that_color, opponent_color=opponent_color, figures=self.figures).keys():
                    self.predicted.append(list([i, j]))
                    self.figures[i][j].setEnabled(True)
                    if (i, j) in self.available_steps:
                        #                        print(a[(i, j)])
                        for y, x in a[(i, j)]:
                            if [[y, x] not in self.available_steps[(i, j)]]:
                                self.available_steps[(i, j)] += a[(i, j)]
                    else:
                        self.available_steps[(i, j)] = a[(i, j)]

            except IndexError:
                print('oops')
        if len(self.predicted) == 0:
            if self.no_steps:
                if len(self.black_white['white']) > len(self.black_white['black']):
                    self.msg.setText('Результат: ' + '. Победили белые фишки.')
                    winner = "Белые"
                elif len(self.black_white['white']) < len(self.black_white['black']):
                    self.msg.setText('Результат: ' + '. Победили чёрные фишки.')
                    winner = "Чёрные"
                else:
                    self.msg.setText('Результат: ' + '. Ничья.')
                    winner = "Ничья"
                self.msg.setText(self.msg.text() + f"\nСчёт: Белые:{len(self.black_white['white'])}; "
                                                   f"Чёрные:{len(self.black_white['black'])}")
                conn = sqlite3.connect('result.db')

                with conn:
                    c = conn.cursor()
                    c.execute('''INSERT INTO Games(score_1, score_2, winner) VALUES(?, ?, ?)''',
                              (len(self.black_white['white']), len(self.black_white['black']), winner))
                self.msg.exec()


            else:
                self.no_steps = True
                self.counter = self.counter + 1 % 2
                self.predict_step()
        else:
            self.no_steps = False

    #        print(self.available_steps)

    def start_game(self):
        self.counter = 0
        for i in range(3, 5):
            for j in range(3, 5):
                self.black_white[black_or_white(self.counter)].append([i, j])
                self.counter = (self.counter + 1) % 2
                self.figures[i][j].setEnabled(False)

            self.counter = (self.counter + 1) % 2
        self.predict_step()
        a, b, c, d = self.black_white["white"][:], self.black_white["black"][:], self.predicted[:], dict(
            self.available_steps)
        self.stack_of_steps["figures"].append([a, b])
        self.stack_of_steps["predicted"].append([c])
        self.stack_of_steps["available_steps"].append(d)
        self.render_field()

    def step_ai(self):
        self.ai.get_values(self.predicted, self.available_steps)
        res = self.ai.calculate()
        print(res)
        if len(self.predicted) > 0:
            self.figures[res[0]][res[1]].click()

    def step(self):

        self.counter = (self.counter + 1) % 2
        ind = [self.sender().y, self.sender().x]
        if ind not in self.black_white[black_or_white(self.counter)]:
            self.black_white[black_or_white(self.counter)].append(ind)
        self.predicted = []
        self.render_field()
        self.figures[ind[0]][ind[1]].setStyleSheet(self.styles["default"])
        time.sleep(.3)
        that_color, opponent_color = self.black_white[black_or_white(self.counter)], \
                                     self.black_white[black_or_white(self.counter + 1 % 2)]
        #       print(self.available_steps[(ind[0], ind[1])])
        for y, x in self.available_steps[(ind[0], ind[1])]:

            if [y, x] not in that_color and [y, x] != ind:
                self.black_white[black_or_white(self.counter)].append([y, x])
            if [y, x] in opponent_color:
                self.black_white[black_or_white((self.counter + 1) % 2)].remove([y, x])
        if ind not in self.black_white[black_or_white(self.counter)]:
            self.black_white[black_or_white(self.counter)].append(ind)
        self.predict_step()
        self.render_field()
        if self.game_mode.is_with_ai and self.counter % 2 == 1:
            self.step_ai()
        else:
            a, b, c, d = self.black_white["white"][:], self.black_white["black"][:], self.predicted[:], dict(
                self.available_steps)
            self.stack_of_steps["figures"].append([a, b])
            self.stack_of_steps["predicted"].append([c])
            self.stack_of_steps["available_steps"].append(d)


class GameMode(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.is_with_ai = False
        self.setWindowTitle('Выбор режима')

        self.ui_layout = QVBoxLayout()
        self.setLayout(self.ui_layout)

        self.two_players = QPushButton('Два игрока', self)
        self.ai_player = QPushButton('Играть с ии', self)
        self.ai_player.clicked.connect(self.with_ai_mode)
        self.two_players.clicked.connect(self.two_players_mode)
        self.ui_layout.addWidget(self.two_players)
        self.ui_layout.addWidget(self.ai_player)

    def two_players_mode(self):
        self.is_with_ai = False
        self.close()

    def with_ai_mode(self):
        self.is_with_ai = True
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
