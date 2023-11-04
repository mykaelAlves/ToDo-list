all: ds build run

allt: ds test

build:
	pyinstaller --onefile -w main.py

run:
	dist/main.exe

test:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\mainwindow.ui -o D:\Git\ToDo-list\package\ui\mainwindow_ui.py
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\add_task_dialog.ui -o D:\Git\ToDo-list\package\ui\add_task_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\remove_task_dialog.ui -o D:\Git\ToDo-list\package\ui\remove_task_dialog_ui.py