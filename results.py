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
        self.setWindowTitle("Работа с QTableWidget")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["Номер", "Счёт чёрных", "Счёт белых", "Победитель"])

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)
        self.connection = sqlite3.connect("result.db")
        c = self.connection.cursor()


        res = self.connection.cursor().execute("SELECT * FROM Games").fetchall()
        print(res)
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