all: ds exe

exe:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\mainwindow.ui -o D:\Git\ToDo-list\package\ui\mainwindow_ui.py
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\add_task_dialog.ui -o D:\Git\ToDo-list\package\ui\add_task_dialog_ui.py