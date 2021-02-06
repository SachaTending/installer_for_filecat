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
	UI = False
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
		count_stages = 9
		# Загрузка update_data.json
		try:
			sg.one_line_progress_meter('Download is "update_api.json"', 0, count_stages, 'Install')
			namefile_update_data = wget.download("https://raw.githubusercontent.com/romanin-rf/FileCat/master/update_api.json")
		except:
			sg.one_line_progress_meter('Download is "update_api.json"', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "ConnectionError: An error occurred while uploading the file", "Install FileCat", 16)
			raise ConnectionError("An error occurred while uploading the file")

		# Открытие update_data.json
		try:
			sg.one_line_progress_meter('Loading is "update_api.json"', 1, count_stages, 'Install')
			with open(str(namefile_update_data)) as UpdateDataFile:
				UpdateData = json.load(UpdateDataFile)
		except:
			sg.one_line_progress_meter('Loading is "update_api.json"', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "BlockingIOError: Couldn't get information from file", "Install FileCat", 16)
			raise BlockingIOError("Couldn't get information from file")

		# Удаление update_data.json
		try:
			sg.one_line_progress_meter('Delected is "update_api.json"', 2, count_stages, 'Install')
			os.remove(str(os.getcwd()) + "\\" + str(namefile_update_data))
		except:
			ctypes.windll.user32.MessageBoxW(0, "Warning: Couldn't delete file", "Install FileCat", 16)

		# Переход в директорию для установки
		try:
			sg.one_line_progress_meter('Changing the directory', 3, count_stages, 'Install')
			os.chdir(Directory)
		except:
			sg.one_line_progress_meter('Changing the directory', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "IsADirectoryError: Couldn't navigate to the installation directory", "Install FileCat", 16)
			raise IsADirectoryError("Couldn't navigate to the installation directory")

		# Создание папки для распаковки
		try:
			sg.one_line_progress_meter('Create directory for install', 4, count_stages, 'Install')
			namedir_for_install = "FileCat-v{0}".format(UpdateData["version"])
			os.mkdir(namedir_for_install)
		except:
			sg.one_line_progress_meter('Create directory for install', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "PermissionError: Failed to create folder", "Install FileCat", 16)
			raise PermissionError("Failed to create folder")

		# Переход в папку для загрузки и установки
		try:
			sg.one_line_progress_meter('Changing the directory', 5, count_stages, 'Install')
			os.chdir(namedir_for_install)
		except:
			sg.one_line_progress_meter('Changing the directory', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "IsADirectoryError: Couldn't navigate to the installation directory", "Install FileCat", 16)
			raise IsADirectoryError("Couldn't navigate to the installation directory")

		# Загрузка пакета .zip для распаковки
		try:
			sg.one_line_progress_meter('Download is FileCat.zip', 6, count_stages, 'Install')
			namefile_release_zip = str(wget.download(str(UpdateData["url"])))
		except:
			sg.one_line_progress_meter('Download is FileCat.zip', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "ConnectionError: An error occurred while uploading the file", "Install FileCat", 16)
			raise ConnectionError("An error occurred while uploading the file")

		# Проверка .zip
		try:
			if zipfile.is_zipfile(namefile_release_zip) == False:
				sg.one_line_progress_meter('Checking the file', count_stages, count_stages, 'Install')
				ctypes.windll.user32.MessageBoxW(0, "FileNotFoundError: The file failed validation", "Install FileCat", 16)
				raise FileNotFoundError("The file failed validation")
			sg.one_line_progress_meter('Checking the file', 7, count_stages, 'Install')
		except:
			sg.one_line_progress_meter('Checking the file', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "FileNotFoundError: The file failed validation", "Install FileCat", 16)
			raise FileNotFoundError("The file failed validation")

		# Распаковка .zip
		try:
			sg.one_line_progress_meter('Unpacking', 8, count_stages, 'Install')
			with zipfile.ZipFile(namefile_release_zip, 'r') as ReleaseFileForUpacking:
				ReleaseFileForUpacking.extractall()
			sg.one_line_progress_meter('Unpacking', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "Installation is complete", "Install FileCat", 64)
		except:
			sg.one_line_progress_meter('Unpacking', count_stages, count_stages, 'Install')
			ctypes.windll.user32.MessageBoxW(0, "OSError: Failed to complete the installation", "Install FileCat", 16)
			raise OSError("Failed to complete the installation")
else:
	raise OSError("Your operating system is not supported")