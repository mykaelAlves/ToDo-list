from PyQt6.QtWidgets import QMainWindow, QDialog
from package import connection_db
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import add_task_dialog_ui
from package.ui import remove_task_dialog_ui
from package.ui import see_all_tasks_dialog_ui
from package.ui import edit_task_dialog_ui
from package.task import Task
import pickle


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
        self.load_list()
        self.ui.add_button.clicked.connect(self.add_it)
        self.ui.remove_button.clicked.connect(self.remove_it)
        self.ui.edit_button.clicked.connect(self.edit_it)
        self.ui.see_all_button.clicked.connect(self.see_it)
        self.ui.done_button.clicked.connect(self.task_done)
        self.show()


    def load_list(self):
        self.con_cursor.execute("SELECT * from Items")

        records = self.con_cursor.fetchall()

        for row in records:
            task = Task(row[0], row[2], row[1])
            if not self.is_already_on_list(task):
                self.tasks.append(task)
            self.today_list_widget()


    def is_already_on_list(self, task):
        for i in self.tasks:
            if i.title == task.title:
                return True
        return False


    def today_list_widget(self):
        try:
            if self.tasks[len(self.tasks) - 1].is_today():
                self.ui.listWidget.addItem(self.tasks[len(self.tasks) - 1].title)
        except:
            print("there's a column with no deadline")


    def not_due_list_widget(self):
        try:
            if not self.tasks[len(self.tasks) - 1].is_due():
                pass
                #to implement
        except:
            print("there's a column with no deadline")


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

            self.con_cursor.execute("INSERT INTO Items VALUES (?, ?, ?)", (deadline, description, title))

            self.load_list()


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