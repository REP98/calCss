#!/usr/bin/env python3
# License: MIT
# Author: Robert Pérez
# Title: Calculate CSS
# file: calculatecss.py
# Purpose: Calcula y convierte medidas para su uso en CSS
# Dependencies: TKinter (python3-tk), PIL, cairosvg, os, webbrowser, re
from bin.View import Application

app = Application()

if __name__ == "__main__":
	app.mainloop()

try:
   app.destroy()
except:
   pass

