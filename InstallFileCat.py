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
	ctypes.windll.user32.MessageBoxW(0, "Failed to load libraries", "Installer for FileCat", 64)

# Логика загрузки
