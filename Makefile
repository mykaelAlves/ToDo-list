all: ds build run

allt: ds test

build:
	pyinstaller --onefile -w main.py

run:
	dist/main.exe

test:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic designer\mainwindow.ui -o package\ui\mainwindow_ui.py
	python.exe -m PyQt6.uic.pyuic designer\add_task_dialog.ui -o package\ui\add_task_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic designer\remove_task_dialog.ui -o package\ui\remove_task_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic designer\edit_task_dialog.ui -o package\ui\edit_task_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic designer\see_all_tasks_dialog.ui -o package\ui\see_all_tasks_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic designer\error_dialog.ui -o package\ui\error_dialog_ui.py