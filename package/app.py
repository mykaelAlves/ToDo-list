from package import connection_db
from package.mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

def run():
    connection, cursor = connection_db.get_connection()

    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()