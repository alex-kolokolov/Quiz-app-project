import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import QSize, Qt


class Results(QMainWindow):
    def __init__(self):

        super().__init__()

        self.InitUI()

    def InitUI(self):
        self.setMinimumSize(QSize(750, 250))
        self.move(500, 200)
        self.setWindowTitle("Результаты")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(1)
        """Колонки"""
        table.setHorizontalHeaderLabels(["Номер", "Счёт игрока 1", "Счёт игрока 2", "Исход игры", 'Имя Победителя'])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)
        """Запрос получения данных"""
        with sqlite3.connect("result.db") as self.connection:
            res = self.connection.cursor().execute("""SELECT games.id, games.score_1, games.score_2, result as conclusion, 
            name AS name_winner 
            FROM 
            games 
            LEFT JOIN game_results ON games.conclusion = game_results.id
            LEFT JOIN players_names ON games.name_winner = players_names.id""").fetchall()


        for i, row in enumerate(res):
            table.setRowCount(
                table.rowCount() + 1)
            for j, elem in enumerate(row):
                table.setItem(
                    i, j, QTableWidgetItem(str(elem)))
