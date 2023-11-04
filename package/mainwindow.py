from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QDialog
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui.add_task_dialog_ui import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.pushButton_2.clicked.connect(self.add_it)
        self.show()

    def add_it(self):
        dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        dialog.show()

    def remove_it():
        pass

    def see_it():
        pass

    def edit_it():
        pass