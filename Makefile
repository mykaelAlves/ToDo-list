exe:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic D:\Git\ToDo-list\designer\mainwindow.ui -o D:\Git\ToDo-list\package\ui\mainwindow_ui.py
	python package/ui/test_ui.py