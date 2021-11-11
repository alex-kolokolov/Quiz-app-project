import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ai import RandomBot
from results import Results


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('Настроечки')
        self.setMinimumSize(350, 50)
        self.main_layout = QVBoxLayout()
        self.clear_db = QHBoxLayout()
        self.clear_db_label = QLabel()
        self.clear_db_label.setText("Очистить базу данных.")
        self.clear_db_button = QPushButton('Очистить', self)
        self.clear_db_button.clicked.connect(self.clear_db_method)
        self.clear_db.addWidget(self.clear_db_label)
        self.clear_db.addWidget(self.clear_db_button)
        self.main_layout.addLayout(self.clear_db)
        self.setLayout(self.main_layout)

    def clear_db_method(self):
        self.connection = sqlite3.connect("result.db")
        self.connection.cursor().execute("DROP TABLE Games")
        self.connection.cursor().execute("""CREATE TABLE Games (
    id      INTEGER     PRIMARY KEY,
    score_1 INTEGER,
    score_2 INTEGER,
    winner  VARCHAR (6) 
);""")
