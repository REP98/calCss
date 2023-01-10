# License: MIT
# Author: Robert Pérez
# Title: Load Resources
# file: Load.py
# Purpose: Carga images para el app
# Dependencies: TKinter (python3-tk), PIL(python3-pil.imagetk), cairosvg(python3-cairosvg)
# See: https://bgstack15.wordpress.com/2019/07/13/display-svg-in-tkinter-python3/
from tkinter import *
from PIL import Image, ImageTk, PngImagePlugin
from bin.Utils import fileName

LM_USE_SVG = 0
try:
   from cairosvg import svg2png
   LM_USE_SVG = 1
except:
   print("WARNING: Unable to import cairosvg. No svg images will be displayed.")
   LM_USE_SVG = 0

def photoimage_from_svg(filename = "",size = "48"):
   # this one works, but does not allow me to set the size.
   # this is kept as an example of how to open a svg without saving to a file.
   # open svg
   item = svg2png(url=filename, parent_width = size, parent_height = size)
   return ImageTk.PhotoImage(data=item)

def empty_photoimage(size=24):
   photo = Image.new("RGBA",[size,size])
   return ImageTk.PhotoImage(image=photo)

def image_from_svg(filename = "",size = 0):
	path_out = "image/png/"+fileName(filename)+".png"
	# open svg
	if LM_USE_SVG == 1:
		if size == 0:
			# unscaled
			svg2png(url=filename, write_to=path_out)
		else:
			svg2png(url=filename, write_to=path_out, parent_width = size, parent_height = size)
		photo = Image.open(path_out)
	else:
		photo = Image.new("RGBA",[size,size])
	return photo
		
def get_scaled_icon(iconfilename, size = 0):
	try:
		# try an svg
		if re.compile(".*\.svg").match(iconfilename):
			photo = image_from_svg(filename=iconfilename, size=size)
		else:
			photo = Image.open(iconfilename)
	except Exception as f:
		print("Error with icon file:", f)
		return empty_photoimage()

	if size != 0 and (type(photo) is Image or type(photo) is PngImagePlugin.PngImageFile):
		photo.thumbnail(size=[size, size])

	if not type(photo) is ImageTk.PhotoImage:
		try:
			photo = ImageTk.PhotoImage(photo)
		except Exception as e:
			print("Error was ",e)
	return photo

	
