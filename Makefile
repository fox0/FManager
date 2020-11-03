all: ui_main.py

ui_%.py: ui_%.ui
	pyuic5 $< -o $@ -x
