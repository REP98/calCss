from tkinter import *
from tkinter import font
from tkinter import ttk
from bin.Load import get_scaled_icon
from bin.Utils import number, goWeb, isFloat, tupleInTuple
from bin.Converter import To
from bin.Style import Theme


class Tab1(ttk.Frame):
	"""docstring for Frame"""
	def __init__(self, root):
		super().__init__(root, relief="ridge")
		self.TxtBase = StringVar(value="Base en PX:")
		self.MSVar = StringVar(value="px")
		self.MSVar1 = StringVar(value="rem")
		self.baseFont = StringVar(value="16")
		self.baseDec = StringVar(value="3")
		self.numberOne = StringVar(value="16")
		self.numberTwo = StringVar(value="1")
		self.PhotoArrowLR= get_scaled_icon('image/svg/arrow-left-right.svg', 18)
		pads = {"padx":10, "pady":5}
		check_num = (root.register(number), '%P')

		self.grid()

		# GRID ROW 1
		ttk.Label(self, textvariable=self.TxtBase).grid(column= 0, row=0, **pads, sticky="NSWE")		
		self.baseRoot = ttk.Entry(self, textvariable=self.baseFont, validate="key", validatecommand=check_num, width=7)
		self.baseRoot.grid(column=1, row=0, **pads, sticky="NSWE")
		ttk.Label(self, text = "Decimales:").grid(column=2, row=0, **pads, sticky="NSWE")
		self.baseDecimal = ttk.Entry(self, textvariable=self.baseDec, validate="key", validatecommand=check_num, width=7)
		self.baseDecimal.grid(column=3, row=0, **pads, sticky="NSWE")

		# GRID ROW 2
		ttk.Label(self, text = "Número").grid(column= 0, row=1, pady=5, padx=10, sticky="W")
		ttk.Label(self, text = "de").grid(column= 1, row=1, **pads, columnspan=2, sticky="W")
		ttk.Label(self, text = "a").grid(column= 3, row=1, **pads, columnspan=2, sticky="W")

		#GRID ROW 3
		self.entryNumber = ttk.Entry(self, textvariable=self.numberOne, validate="key", validatecommand=check_num, width=7)
		self.entryNumber.grid(column=0, row=2, **pads, sticky="NSWE")		
		self.MeasureStart = ttk.Combobox(self, textvariable=self.MSVar,  width=5)
		self.MeasureStart.set("px")
		self.MeasureStart.grid(column=1, row=2, **pads, sticky="NSWE")
		self.MeasureStart['values'] = self.getMeaseure()
		self.MeasureStart['state'] = 'readonly'		
		self.btnChange = ttk.Button(self, text="", width=10, image=self.PhotoArrowLR, compound="center", command=self.onChageValue)
		self.btnChange.grid(column=2, row=2, **pads, sticky="NSWE")
		self.entryNumber1 = ttk.Entry(self, textvariable=self.numberTwo, validate="key", validatecommand=check_num, width=7)
		self.entryNumber1["state"] = 'readonly'
		self.entryNumber1.grid(column=3, row=2, **pads, sticky="NSWE")
		self.MeasureEnd = ttk.Combobox(self, textvariable=self.MSVar1, width=5)
		self.MeasureEnd['values'] = self.getMeaseure()
		self.MeasureEnd['state'] = 'readonly'
		self.MeasureEnd.set("rem")
		self.MeasureEnd.grid(column=4, row=2, **pads, sticky="NSWE")

		#GRID ROW 4
		self.msm = StringVar()
		ttk.Label(self, textvariable=self.msm, foreground="red").grid(column=1, row=3, columnspan=4, **pads)
		self.onBind()

	def getMeaseure(self):
		return (
			"px", "em", "rem", "cm", "in", "mm",
			"pc", "pt", "n%", "lh",
			"vw", "vh"
			)

	def onBind(self):
		self.MeasureStart.bind('<<ComboboxSelected>>', self.onChageNumber)
		self.MeasureEnd.bind('<<ComboboxSelected>>', self.onChageNumber)

		for field in (self.entryNumber, self.baseRoot,self.baseDecimal, self.entryNumber1):
			for event in ('<KeyRelease>', '<<Paste>>', '<<Clear>>'):
				field.bind(event, self.onKeyPress)

	def inMetrix(self, measure):
		return tupleInTuple(measure, (self.MSVar.get(), self.MSVar1.get()))

	def onKeyPress(self, *args):
		self.convert()

	def onChageNumber(self, event= False):
		if self.inMetrix("vw"):
			self.TxtBase.set("Ancho:")
			self.baseFont.set(self.winfo_screenwidth())
		elif self.inMetrix("vh"):
			self.TxtBase.set("Altura:")
			self.baseFont.set(self.winfo_screenheight())
		elif self.inMetrix(("cm", "mm", "in", "pt", "pc")):
			self.TxtBase.set("PPI/DPI:")
			self.baseFont.set(96)
		else:
			self.TxtBase.set("Base en PX:")
			self.baseFont.set(16)

		if self.MSVar in ("cm", "mm") and self.MSVar1 in ("vw", "vh"):
			x = self.winfo_screenwidth()
			self.TxtBase.set("Ancho:")
			if self.MSVar1.get() == "vh":
				x = self.winfo_screenheight()
				self.TxtBase.set("Alto:")
			self.baseFont.set(x)

		self.convert()

	def onChageValue(self, *args):
		v = (
			self.numberOne.get(),
			self.MSVar.get(),
			self.numberTwo.get(),			
			self.MSVar1.get()
		)
		self.numberOne.set(v[2])
		self.numberTwo.set(v[0])
		self.MSVar.set(v[3])
		self.MSVar1.set(v[1])
		self.onChageNumber(False)

	def convert(self):
		self.msm.set("")
		if self.baseFont.get() is None or self.baseFont.get() == "":
			self.msm.set("Debe establecer una Base de Calculo")
			self.baseRoot.focus()
			pass

		if self.baseDec.get() is None or self.baseDec.get() == "":
			self.baseDec.set(3)

		to = To(self.baseFont.get(), self.baseDec.get())
		if len(self.numberOne.get()) > 0:
			nVal = to.get(
				number=self.numberOne.get(), 
				measuerof=self.MSVar.get(), 
				to=self.MSVar1.get())
			if nVal == None:
				nVal = "No Calculado"

			if isFloat(nVal):
				self.numberTwo.set(nVal)
			else:
				self.msm.set(nVal)	
				self.numberTwo.set(0)
		
class Tab3(ttk.Frame):
	"""docstring for Tab3"""
	def __init__(self, root):
		super().__init__(root)

		self.grid()
		self.columnconfigure(0, weight=2)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)

		self.photo = get_scaled_icon('image/svg/calculator1.svg', 200)
		self.c = Canvas(self, width=200, height=200, background="#212121", bd=0, relief='ridge', highlightthickness=0)
		self.c.grid(column=0, row=0, sticky="N", pady=0, padx=0, rowspan=6)
		self.c.create_image(0,0, image=self.photo, anchor="nw")
		
		
		ttk.Label(self, text="Calculadora CSS").grid(column=1, row=0, sticky="N", pady=5, padx=5, columnspan=2)
		ttk.Label(self, text="Version").grid(column=1, row=1, sticky="NW", pady=5, padx=5)
		ttk.Label(self, text="1.0").grid(column=2, row=1, sticky="NW", pady=5, padx=5)
		ttk.Label(self, text="Convierta Facilmente sus unidades CSS con esta aplicación", wraplength=300).grid(column=1, row=2, sticky="NW", pady=5, padx=5, columnspan=2)
		ttk.Separator(self, orient='horizontal').grid(column=1, row=3, padx=5, pady=5, sticky="NSWE", columnspan=2)
		ttk.Label(self, text="Autor:").grid(column=1, row=4, sticky="NW", pady=5, padx=5)
		link = ttk.Label(self, text="Robert Pérez", cursor="hand2", class_="profile")
		link.grid(column=2, row=4, sticky="NSWE", pady=5, padx=5)
		self.f = font.Font(link, link.cget('font'))
		self.f.configure(underline=True)
		link.configure(font=self.f)
		ttk.Label(self, text="License:").grid(column=1, row=5, sticky="NW", pady=5, padx=5)
		link1 = ttk.Label(self, text="MIT", cursor="hand2", class_="license")
		self.f1 = font.Font(link1, link1.cget('font'))
		self.f1.configure(underline=True)
		link1.configure(font=self.f1)
		link1.grid(column=2, row=5, sticky="NSWE", pady=5, padx=5)

		link.bind('<Button-1>', goWeb)
		link1.bind('<Button-1>', goWeb)
								

class Application(Tk):
	"""docstring for Application"""
	def __init__(self):
		super().__init__()
		self.title("Calculadora CSS")
		self.maxsize(500, 250)
		self.geometry("500x250")
		self.resizable(0,0)	
		self.iconphoto(False,
			get_scaled_icon('image/svg/calculator1.svg', 24)
		)
		Theme(self)
		self.ParentTabs = ttk.Notebook(self)
		self.Tab1 = Tab1(self.ParentTabs)
		self.Tab2 = Tab3(self.ParentTabs)
		self.ParentTabs.add(self.Tab1, text="Medidas")
		self.ParentTabs.add(self.Tab2, text="Acerca de")
		self.ParentTabs.pack(expand=True, fill="both")

		