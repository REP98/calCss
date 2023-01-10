from tkinter import ttk
from bin.Theme import Paleta

class Theme():
	"""Asigna el Tema de la calculadora"""
	def __init__(self, root):
		self.css = ttk.Style()
		self.filetTheme = Paleta()
		self.css.theme_settings("default", self.config())
		self.css.theme_use("default")
		
	def config(self):
		return {
			"Tk": {
				"configure": {
					"background": self.filetTheme.colors["Bg"],
					"borderwidth": 0,
					"highlightthickness": 0
				}
			},
			"TNotebook": {
				"configure": {
					"background": self.filetTheme.colors["Bg"],
					"borderwidth": 0,
					"highlightthickness": 0
				}
			},
			"TNotebook.Tab": {
				"configure": {
					"relief":"flat",
					"background": self.filetTheme.colors["DarkPrimary"],
					"font": ("Ubuntu", "12"),
					"foreground": self.filetTheme.colors["Text"],
					"borderwidth": 0,
					"highlightthickness": 0,
					"padding": [3, 1],
					"justify": "center",
					"width": 30
				},
				"map": {
					"background": [("selected", "focus", self.filetTheme.colors["Primary"])],
					"foreground": [("selected", "focus", self.filetTheme.colors["Text"])]
				}
			},
			"TFrame": {
				"configure": {
					"background": self.filetTheme.colors["Bg"],
					"foreground": self.filetTheme.colors["Text"],
					"borderwidth": 0,
					"highlightthickness": 0,
					"padding": 1
				}
			},
			"TLabel": {
				"configure": {
					"font": ("Ubuntu", "12"),
					"background": self.filetTheme.colors["Bg"],
					"foreground": self.filetTheme.colors["Text"],
					"justify": "left"
				}
			},
			"TCombobox": {
				"configure": {
					"relief":"flat",
					"padding": [6, 3],
					"fieldbackground": self.filetTheme.colors["SecondaryText"],
					"foreground": self.filetTheme.colors["Text"],
					"borderwidth": 1,
					"bordercolor": self.filetTheme.colors["DarkPrimary"],
					"highlightthickness": 0,
					"font": ("Ubuntu", 12)
				},
				"map": {
					"fieldbackground": [("readonly", self.filetTheme.colors["SecondaryText"])]
				}
			},
			"TButton": {
				"configure": {
					"relief":"flat",
					"padding": [6, 3],
					"background": self.filetTheme.colors["Accent"],
					"foreground": self.filetTheme.colors["Text"],
					"justify": "center"
				},
				"map": {
					"background":[
							('pressed', "!disabled", "active", self.filetTheme.colors["Primary"]),
							("focus", self.filetTheme.colors["DarkPrimary"])
						],
					"foreground": [("pressed", "active", self.filetTheme.colors["Text"])],
				}
			},
			"TEntry": {
				"configure": {
					"relief": "flat",
					"padding": [6,3],
					"bordercolor": self.filetTheme.colors["DarkPrimary"],
					"fieldbackground": self.filetTheme.colors["SecondaryText"],
					"foreground": self.filetTheme.colors["Text"],
					"borderwidth": 1,
					"highlightthickness": 0,
					"highlightbackground": "red",
					"highlightcolor": "red",
					"sticky": "NSWE"
				},
				"map": {
					"fieldbackground": [
						("readonly", self.filetTheme.colors["SecondaryText"]),
						("pressed", "active", self.filetTheme.colors["LightPrimary"])
					]
				}
			},
			"TSeparator": {
				"configure": {
					"bordercolor": self.filetTheme.colors['Accent']
				}
			},
			"unde.TLabel": {
				"configure": {
					"underline": True
				}
			}
		}
