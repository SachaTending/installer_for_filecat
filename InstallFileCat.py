# Импортирование простого показателя прогресса
import PySimpleGUI as sg

# Загрузка основных библеотек
count_libs = 5
try:
	sg.one_line_progress_meter('Loading is lib "ctypes"', 0, count_libs, 'LoadLib')
	import ctypes
	sg.one_line_progress_meter('Loading is lib "wget"', 1, count_libs, 'LoadLib')
	import wget
	sg.one_line_progress_meter('Loading is lib "json"', 2, count_libs, 'LoadLib')
	import json
	sg.one_line_progress_meter('Loading is lib "zipfile"', 3, count_libs, 'LoadLib')
	import zipfile
	sg.one_line_progress_meter('Loading is lib "os"', 4, count_libs, 'LoadLib')
	import os
	sg.one_line_progress_meter('Loading is lib "sys"', 5, count_libs, 'LoadLib')
	import sys
except:
	raise ImportError("Failed to load modules to work with")

# Создание переменой
if sys.platform == "win32":
	Directory = str(os.getcwd())
	UI = True
else:
	raise OSError("Your operating system is not supported")

# Логика загрузки
if sys.platform == "win32":
	if len(sys.argv) > 1:
		if "-D" in sys.argv:
			try:
				Directory = str(sys.argv[int(sys.argv.index("-D")) + 1])
			except:
				ctypes.windll.user32.MessageBoxW(0, "SyntaxError: The folder path is not specified correctly", "Install FileCat", 16)
				raise SyntaxError("The folder path is not specified correctly")
			if not(os.path.isabs(Directory)):
				ctypes.windll.user32.MessageBoxW(0, "NotADirectoryError: The specified folder does not exist", "Install FileCat", 16)
				raise NotADirectoryError("The specified folder does not exist")
		if "-UI" in sys.argv:
			try:
				UI = bool(sys.argv[int(sys.argv.index("-UI")) + 1])
			except:
				ctypes.windll.user32.MessageBoxW(0, "ValueError: The parameter value is not specified correctly", "Install FileCat", 16)
				raise ValueError("The parameter value is not specified correctly")
	if UI:
		pass
	else:
		pass
else:
	raise OSError("Your operating system is not supported")