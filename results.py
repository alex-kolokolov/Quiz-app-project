import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt

class Results(QMainWindow):
    def __init__(self):

        super().__init__()

        self.InitUI()

    def InitUI(self):
        self.setMinimumSize(QSize(480, 80))
        self.setWindowTitle("Результаты")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["Номер", "Счёт игрока 1", "Счёт игрока 2", "Победитель", 'Имя Победителя'])

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)
        self.connection = sqlite3.connect("result.db")

        res = self.connection.cursor().execute("""SELECT Games.id, Games.score_1, Games.score_2, Games.winner, name AS name_winner
                                               FROM
                                                Games
                                               INNER JOIN players_names ON Games.name_winner = players_names.id""").fetchall()
        for i, row in enumerate(res):
            table.setRowCount(
                table.rowCount() + 1)
            for j, elem in enumerate(row):
                table.setItem(
                    i, j, QTableWidgetItem(str(elem)))



    def closeEvent(self, event):
        self.connection.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = Results()
    mw.show()
    sys.exit(app.exec())