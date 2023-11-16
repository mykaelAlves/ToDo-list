from PyQt6.QtWidgets import QMainWindow, QDialog
from package import connection_db
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import add_task_dialog_ui
from package.ui import remove_task_dialog_ui
from package.ui import see_all_tasks_dialog_ui
from package.ui import edit_task_dialog_ui
from package.task import Task


class MainWindow(QMainWindow):
    connection, con_cursor = connection_db.get_connection()
    tasks = []
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.con_cursor.execute("SELECT * FROM sqlite_master")

        if not bool(self.con_cursor.fetchall()): #check if db exists
            self.con_cursor.execute('''CREATE TABLE Items (
                                    title TEXT NOT NULL UNIQUE,
                                    description text,
                                    deadline datetime
                                    );''')
            
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_button.clicked.connect(self.add_it)
        self.ui.remove_button.clicked.connect(self.remove_it)
        self.ui.edit_button.clicked.connect(self.edit_it)
        self.ui.see_all_button.clicked.connect(self.see_it)
        self.ui.done_button.clicked.connect(self.task_done)
        self.show()


    def was_clicked(self):
        self.go = True


    def add_it(self):
        self.go = False
        
        dialog = QDialog()
        ui = add_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        ui.buttonBox.accepted.connect(self.was_clicked)

        dialog.exec()

        if self.go:
            title = ui.task_title.toPlainText()
            deadline = ui.task_date.toPlainText()
            description = ui.task_details.toPlainText()

            self.tasks.append(Task(deadline, title, description))

            title = self.tasks[len(self.tasks) - 1].title
            deadline = self.tasks[len(self.tasks) - 1].deadline
            description = self.tasks[len(self.tasks) - 1].description

            self.ui.listWidget.addItem(self.tasks[len(self.tasks) - 1].title)

            self.con_cursor.execute("INSERT INTO Items VALUES (?, ?, ?)", (title, description, deadline))


    def remove_it(self):
        dialog = QDialog()
        ui = remove_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        dialog.exec()


    def see_it(self):
        dialog = QDialog()
        ui = see_all_tasks_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        #ui.buttonBox.accepted.connect() ;;to implement
        #ui.buttonBox.rejected.connect() ;;to implement

        dialog.exec()


    def edit_it(self):
        dialog = QDialog()
        ui = edit_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        dialog.exec()

    
    def task_done(self):
        pass