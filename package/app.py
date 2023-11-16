from package import connection_db
from package.mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

def run():
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()

    window.connection.commit()
    window.connection.close()