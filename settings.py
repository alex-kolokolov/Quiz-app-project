import sqlite3
from generate_pic import generate_pictures
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Settings(QWidget):
    resolution = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('Настроечки')
        self.setMinimumSize(350, 140)
        with open('settings.txt', mode='r') as f:
            self.settings = [i for i in f.readlines()]
            f.close()
        self.main_layout = QVBoxLayout()
        self.clear_db = QHBoxLayout()
        self.clear_db_label = QLabel()
        self.clear_db_label.setText("Очистить базу данных.")
        self.clear_db_button = QPushButton('Очистить', self)
        self.clear_db_button.clicked.connect(self.clear_db_method)
        self.clear_db.addWidget(self.clear_db_label)
        self.clear_db.addWidget(self.clear_db_button)
        self.main_layout.addLayout(self.clear_db)
        self.set_name_layout = QVBoxLayout()
        self.set_name_player_1 = QHBoxLayout()
        self.set_name_player_1_label = QLabel()
        self.set_name_player_1_label.setText('Имя первого игрока')
        self.set_name_player_1_line = QLineEdit()
        self.set_name_player_1_line.setMaxLength(16)
        self.set_name_player_1_button = QPushButton('✓', self)
        self.set_name_player_1_button.clicked.connect(self.change_name_method)

        self.set_name_player_2 = QHBoxLayout()
        self.set_name_player_2_label = QLabel()
        self.set_name_player_2_label.setText('Имя второго игрока')
        self.set_name_player_2_line = QLineEdit()
        self.set_name_player_2_line.setMaxLength(16)
        self.set_name_player_2_button = QPushButton('✓', self)
        self.set_name_player_2_button.clicked.connect(self.change_name_method)

        with sqlite3.connect('result.db') as db:
            a = db.cursor().execute("""SELECT players_names.name FROM players_names""").fetchall()
            if len(a) > 0:
                self.set_name_player_2_line.setText(a[1][0])
                self.set_name_player_1_line.setText(a[0][0])
        self.set_name_player_2.addWidget(self.set_name_player_2_label)
        self.set_name_player_2.addWidget(self.set_name_player_2_line)
        self.set_name_player_2.addWidget(self.set_name_player_2_button)
        self.set_name_player_1.addWidget(self.set_name_player_1_label)
        self.set_name_player_1.addWidget(self.set_name_player_1_line)
        self.set_name_player_1.addWidget(self.set_name_player_1_button)
        self.set_name_layout.addLayout(self.set_name_player_1)
        self.set_name_layout.addLayout(self.set_name_player_2)
        self.main_layout.addLayout(self.set_name_layout)
        self.set_name_player_2_line.textChanged.connect(self.change_name_method)
        self.set_color_for_figures = QVBoxLayout()
        self.set_color_for_figures_label = QLabel()
        self.set_color_for_figures_label.setText('Выбрать цвет фишек')
        self.colors_buttons = QHBoxLayout()
        self.set_color_for_first_figures_button = QPushButton('Цвет первых фигур', self)
        self.set_color_for_first_figures_button.clicked.connect(self.set_color_figures_method)
        self.colors_buttons.addWidget(self.set_color_for_first_figures_button)
        self.set_color_for_figures.addWidget(self.set_color_for_figures_label)
        self.set_color_for_figures.addLayout(self.colors_buttons)
        self.set_color_for_second_figures_button = QPushButton('Цвет вторых фигур', self)
        self.set_color_for_second_figures_button.clicked.connect(self.set_color_figures_method)
        self.colors_buttons.addWidget(self.set_color_for_second_figures_button)
        self.main_layout.addLayout(self.set_color_for_figures)
        self.change_resolution = QVBoxLayout()
        self.change_resolution_label = QLabel()
        self.change_resolution_label.setText('Разрешение главного окна')
        self.change_resolution_combo = QComboBox()
        items = [f'{i}x{i}' for i in range(400, 1100, 100)]
        self.change_resolution_combo.addItems(items)
        index = self.change_resolution_combo.findText(self.settings[2].rstrip())
        self.change_resolution_combo.setCurrentIndex(index)
        self.change_resolution_combo.findText(self.settings[2].rstrip())
        self.change_resolution.addWidget(self.change_resolution_label)
        self.change_resolution.addWidget(self.change_resolution_combo)
        self.change_resolution_combo.currentTextChanged.connect(self.change_resoluton_method)
        self.main_layout.addLayout(self.change_resolution)
        self.save_settings = QHBoxLayout()
        self.save_settings_layout = QLabel('Сохранить настройки', self)
        self.save_settings_button = QPushButton('Сохранить', self)
        self.save_settings_button.clicked.connect(self.save_settings_method)
        self.save_settings.addWidget(self.save_settings_layout)
        self.save_settings.addWidget(self.save_settings_button)
        self.main_layout.addLayout(self.save_settings)
        self.setLayout(self.main_layout)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Уведомление")
        self.msg.setFixedSize(300, 150)

    def set_color_figures_method(self):
        f = open('settings.txt', mode='r')
        color = QColorDialog.getColor()
        if color.isValid() and color not in f.readlines():
            if self.sender() == self.set_color_for_first_figures_button:
                self.settings[0] = ' '.join([str(color.red()), str(color.green()), str(color.blue())]) + '\n'
            else:
                self.settings[1] = ' '.join([str(color.red()), str(color.green()), str(color.blue())]) + '\n'

    def change_resoluton_method(self):
        self.settings[2] = f'{self.change_resolution_combo.currentText()}\n'
        self.resolution.emit(*[int(i) for i in self.change_resolution_combo.currentText().split('x')])

    def save_settings_method(self):
        f = open('settings.txt', mode='w')
        f.write(''.join(self.settings))
        f.close()
        generate_pictures()

    def change_name_method(self):
        connection = sqlite3.connect('result.db')
        if self.sender() == self.set_name_player_1_button:
            sender_line_edit = self.set_name_player_1_line
            second_line_edit = self.set_name_player_2_line
            sender_id = 1
        else:
            sender_line_edit = self.set_name_player_2_line
            second_line_edit = self.set_name_player_1_line
            sender_id = 2
        if len(sender_line_edit.text()) > 0 and sender_line_edit.text() != 'компьютер' and sender_line_edit.text().lower() != second_line_edit.text().lower():
            connection.cursor().execute(f"""UPDATE players_names
            SET name  = (?)
            WHERE id = (?)""", (sender_line_edit.text(), sender_id)).fetchall()
        else:
            if len(sender_line_edit.text()) == 0: \
                    self.msg.setText('Пустое поле')
            else:
                self.msg.setText('Такое имя уже уже используется')
            self.msg.exec()
        connection.commit()
        connection.close()

    def clear_db_method(self):
        self.connection = sqlite3.connect("result.db")
        self.connection.cursor().execute("DROP TABLE Games")
        self.connection.cursor().execute("DROP TABLE players_names")
        self.connection.cursor().execute("""CREATE TABLE Games (
    id          INTEGER     PRIMARY KEY,
    score_1     INTEGER,
    score_2     INTEGER,
    winner      VARCHAR (8),
    name_winner             REFERENCES players_names (id) 
);""")
        self.connection.cursor().execute("""CREATE TABLE players_names (
    id   INTEGER      PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (16) 
);""")
