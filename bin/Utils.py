# Utilidades
import os
import re
import webbrowser

def fileName(file_path):
	""" Obtiene el nombre de la imagen sin extención"""
	basename = os.path.basename(file_path)
	file_name = os.path.splitext(basename)[0]
	return file_name

def goWeb(event):
	cls_ = event.widget.winfo_class()
	uri = None
	if cls_ == "license":
		uri = "https://github.com/REP98/calCss/blob/e880f7e4130e2d0b52ef887e96d692649c775316/LICENSE"
	elif cls_ == "profile":
		uri = "https://rep98.github.io/"
	webbrowser.open_new_tab(uri)

def number(newval):
	#[+-]?([0-9]*[.])?[0-9]+
	return re.match('^[-+]?[0-9]*\.?[0-9]*$', newval) is not None and len(newval) <= 5

def isFloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def tupleInTuple(n, s):
	if type(n) is tuple:
		k = False
		for i in n:
			if i in s:
				k = True
				break
		return k
	else:
		return n in s