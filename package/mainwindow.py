from PyQt6.QtWidgets import QMainWindow, QDialog
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import add_task_dialog_ui
from package.ui import remove_task_dialog_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.add_button.clicked.connect(self.add_it)
        ui.remove_button.clicked.connect(self.remove_it)
        self.show()


    def add_it(self):
        dialog = QDialog()
        ui = add_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        #ui.buttonBox.accepted.connect() #to implement
        #ui.buttonBox.rejected.connect() #to implement

        dialog.exec()


    def remove_it(self):
        dialog = QDialog()
        ui = remove_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        dialog.exec()


    def see_it():
        pass


    def edit_it():
        pass