from PyQt6.QtWidgets import QMainWindow, QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView, QTableWidget, QLabel
from PyQt6.QtGui import QMovie, QFont, QAction
from package import connection_db
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import add_task_dialog_ui
from package.ui import remove_task_dialog_ui
from package.ui import see_all_tasks_dialog_ui
from package.ui import edit_task_dialog_ui
from package.ui import error_dialog_ui
from package.ui import edit_task_connect_dialog_ui
from package.task import Task
from package import check
import webbrowser
import sqlite3


class MainWindow(QMainWindow):
    connection, con_cursor = connection_db.get_connection()
    tasks = []
    

    def __init__(self):
        super(MainWindow, self).__init__()

        self.con_cursor.execute("SELECT * FROM sqlite_master")

        if not bool(self.con_cursor.fetchall()): #check if db exists
            self.con_cursor.execute('''CREATE TABLE Items (
                                    title TEXT NOT NULL UNIQUE,
                                    deadline datetime,
                                    description text
                                    );''')
            
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_list(self.ui.listWidget)
        action_transparent = self.findChild(QAction, "actionTransparent_window")
        action_dark = self.findChild(QAction, "actionDark_mode")
        action_light = self.findChild(QAction, "actionLight_mode")
        
        movie = QMovie("icons/cat_.gif") 
        self.ui.cat.setMovie(movie)
        movie.start()
        
        self.ui.listWidget.itemClicked.connect(self.task_done)
        self.ui.listWidget.setFont(QFont('Helvetica [Cronyx]', 14))
        self.ui.add_button.clicked.connect(self.add_it)
        self.ui.remove_button.clicked.connect(self.remove_it)
        self.ui.edit_button.clicked.connect(self.edit_it)
        self.ui.see_all_button.clicked.connect(self.see_it)
        self.ui.done_button.clicked.connect(self.task_done)
        action_transparent.triggered.connect(self.transparent_mode)
        action_dark.triggered.connect(self.dark_mode)
        action_light.triggered.connect(self.light_mode)
        self.ui.menuHelp.aboutToShow.connect(self.help_open)
        self.show()


    def load_list(self, listWidget):
        self.con_cursor.execute("SELECT * from Items")

        records = self.con_cursor.fetchall()
        print(f"records: {records}")
        self.tasks.clear()
        if listWidget == self.ui.listWidget:
            self.ui.listWidget_2.clear()
        listWidget.clear()

        for row in records:
            task = Task(row[0], row[1], row[2])

            self.tasks.append(task)

            if listWidget == self.ui.listWidget:
                self.today_list_widget()
                self.due_list_widget()

                continue

            listWidget.addItem(task.title)


    def today_list_widget(self):
        try:
            if self.tasks[len(self.tasks) - 1].is_today():
                self.ui.listWidget.addItem(self.tasks[len(self.tasks) - 1].title)
                
        except Exception as e:
            print(e)


    def due_list_widget(self):
        try:
            if self.tasks[len(self.tasks) - 1].is_due():
                self.ui.listWidget_2.addItem(self.tasks[len(self.tasks) - 1].title)

        except Exception as e:
            print(e)


    def add_task(self, ui):
        title = ui.task_title.toPlainText()
        deadline = ui.task_date.toPlainText()
        description = ui.task_details.toPlainText()

        self.tasks.append(Task(title, deadline, description))
        task = self.tasks[len(self.tasks) - 1]

        title = task.title
        deadline = task.deadline
        description = task.description

        try:
            check.check_task(task)
        except RuntimeWarning as e:
            self.tasks.remove(self.tasks[len(self.tasks) - 1])
            self.error(e.__str__())
            
            return
            
        try:
            self.con_cursor.execute("INSERT INTO Items VALUES (?, ?, ?)", (title, deadline, description,))
        except sqlite3.IntegrityError as e:
            self.error(text="ERROR: TITLE MUST BE UNIQUE")
            
        self.load_list(self.ui.listWidget)


    def add_it(self):        
        dialog = QDialog()
        ui = add_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        ui.buttonBox.accepted.connect(lambda: self.add_task(ui))

        dialog.exec()


    def remove_it(self):        
        dialog = QDialog()
        ui = remove_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)
        
        self.con_cursor.execute("SELECT * from Items")

        records = self.con_cursor.fetchall()

        for row in records:
            task = Task(row[0], row[1], row[2])

            ui.task_list.addItem(task.title)


        ui.remove_confirm_button.clicked.connect(lambda: self.remove_task(ui.task_list))
        ui.reject_button.clicked.connect(dialog.close)

        dialog.exec()

        self.load_list(self.ui.listWidget)


    def error(self, text):
        error = QDialog()
        error_ui = error_dialog_ui.Ui_Dialog()
        error_ui.setupUi(error)
        error_ui.label.setText(text)

        error.exec()


    def see_it(self):
        dialog = QDialog()
        ui = see_all_tasks_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        self.con_cursor.execute("SELECT * from Items")

        records = self.con_cursor.fetchall()

        ui.tableWidget.setRowCount(len(self.tasks))
        ui.tableWidget.setColumnWidth(0, 200)
        ui.tableWidget.setColumnWidth(2, 441)

        r = 0

        for row in records:
            ui.tableWidget.setItem(r, 0, QTableWidgetItem(row[0]))
            ui.tableWidget.setItem(r, 1, QTableWidgetItem(row[1]))
            ui.tableWidget.setItem(r, 2, QTableWidgetItem(row[2]))
            
            r+=1

        ui.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        dialog.exec()


    def edit_it(self):
        dialog = QDialog()
        ui = edit_task_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)
        
        for i in self.tasks:
            ui.task_list.addItem(i.title)

        ui.remove_confirm_button.clicked.connect(lambda: self.edit_task(ui.task_list))
        ui.reject_button.clicked.connect(dialog.close)

        dialog.exec()

        self.load_list(self.ui.listWidget)

    
    def edit_task(self, listWidget):
        dialog = QDialog()
        ui = edit_task_connect_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)
        
        task = None
        
        if not bool(listWidget.currentItem()):
            self.error("ERROR: NOTHING WAS SELECTED")
            return
        
        for i in self.tasks:
            if i.title == listWidget.currentItem().text():
                task = i
        
        title = task.title
        temp_deadline = task.deadline
        temp_description = task.description
        
        dialog.exec()
        
        deadline = ui.task_date.toPlainText()
        description = ui.task_details.toPlainText()

        try:
            self.remove_task(listWidget)
            check.check_task(task)
        except RuntimeWarning as e:
            self.error(e.__str__())
            
            return
        finally:
            try:
                check.check_task(Task(title, deadline, description))
            except RuntimeWarning as e:
                self.error(e.__str__())
                deadline = temp_deadline
                description = temp_description
            self.tasks.append(Task(title, deadline, description))
            for i in self.tasks:
                listWidget.addItem(i.title)
             
        try:
            self.con_cursor.execute("INSERT INTO Items VALUES (?, ?, ?)", (title, deadline, description,))
        except sqlite3.IntegrityError as e:
            self.error(text="ERROR: TITLE MUST BE UNIQUE")

        self.load_list(self.ui.listWidget)
    
    
    def remove_task(self, listWidget):
        try:
            title = listWidget.currentItem().text()
            self.con_cursor.execute("DELETE FROM Items WHERE title=?", (title,))
        
            for i in self.tasks:
                if i.title.__eq__(title):
                    self.tasks.remove(i)
                    break

        except AttributeError:
            self.error("ERROR: NOTHING WAS SELECTED")

        self.load_list(listWidget)


    def task_done(self):       
        self.ui.done_button.clicked.connect(lambda: self.remove_task(self.ui.listWidget))
        
    
    def transparent_mode(self):
        self.setWindowOpacity(0.8)
        
        
    def dark_mode(self):
        with open("designer/darkmode.txt") as f:
            dark_style = f.read()
        
        self.setStyleSheet(dark_style)
        self.setWindowOpacity(1)
        
        
    def light_mode(self):
        self.setStyleSheet(" ")
        self.setWindowOpacity(1)
        
    
    def help_open(self):
        webbrowser.open('https://github.com/Macai13/ToDo-list/blob/main/README.md', new=2)