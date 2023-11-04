from package import connection_db
from package.mainwindow import MainWindow
import sys
from PyQt6.QtWidgets import QApplication

def run():
    connection, cursor = connection_db.get_connection()

    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()