# Clase encargada de convertir Unidades
class To():
	bFont = 16
	bDec = 3
	"""docstring for to"""
	def __init__(self, baseFont, baseDec):
		self.bFont = int(baseFont)
		self.bDec = int(baseDec)
		self.listMetrix = (
			"px", "em", "rem", "n%", "cm", "in", "mm",
			"pc", "pt", "lh",
			"vw", "vh"
			)

	def get(self, number, measuerof, to):
		if measuerof not in self.listMetrix or to not in self.listMetrix:
			return "Medida no permitida"

		n = float(number)
		if measuerof == "px":
			return self.px(n, to)
		elif measuerof in ("em", "rem"):
			return self.e(n, to)
		elif measuerof == "n%":
			return self.percentage_to(n)
		elif measuerof in ("vw", "vh"):
			return self.viewport(n, to)
		elif measuerof == "in":
			return self.inches(n, to)
		elif measuerof == "mm":
			return self.mm(n, to)
		elif measuerof == "cm":
			return self.cm(n, to)
		elif measuerof == "pt":
			return self.point(n, to)
		elif measuerof == "pc":
			return self.picas(n, to)
		elif measuerof == "lh":
			return self.lh(n, to)
		else:
			return "Medida no encontrada"
		

	def r(self, n):
		return round(n, self.bDec)

	def px(self, n, to):
		num = None
		txt = ""
		if to in ("rem", "em", "lh"):
			num = (n / self.bFont)
		elif to == "n%":
			return self.to_percent(n)
		elif to == "cm":
			num = ((n / self.bFont) * 2.54)
		elif to == "mm":
			num = ((n / self.bFont) * 25.4)
		elif to == "in":
			num = (n / self.bFont)
		elif to == "pt":
			num = (n * (72 / self.bFont))
		elif to == "pc":
			num = (n * (6 / self.bFont))
		elif to in ("vw", "vh"):
			num = ((100 * n) / self.bFont)
		else:
			txt = "Medida ["+to+"] no soportada para PX"

		if num is None :
			return txt
		else:
			return self.r(num)
			
	def e(self, n, to):
		if to == "px":
			return self.r((n * self.bFont))
		else:
			px = self.e(n, "px")
			if to == "n%":
				return self.to_percent(n)
			else:
				return self.px(px, to)

	def viewport(self, n,to):
		num = None
		if to == "px":
			num = ((self.bFont * n) / 100)
		elif to == "n%":
			return self.to_percent(n)
		else:
			px = self.viewport(n, "px")
			return self.px(px, to)

		return self.r(num)


	def to_percent(self, n):
		""" Convierte un numero a porcentaje """
		return self.r((n * 100) / self.bFont)

	def percentage_to(self, n):
		""" Convierte Porcentaje a medidas en base a la base px """
		return self.r((n * self.bFont) / 100)

	def cm(self, n, to):
		num = None
		txt = ""
		if to == "px":
			num = (self.bFont * n) / 2.54
		elif to == "n%":
			return self.to_percent(n)
		elif to in ("rem", "em", "lh", "vw", "vh"):
			px = self.cm(n, "px")
			self.bFont = 16
			return self.px(px, to)
		elif to == "in":
			num = (n / 2.54)
		elif to == "mm":
			num = (n * 10)
		elif to == "pc":
			num = (n * (6/2.54))
		elif to == "pt":
			num = (n * (72/2.54))
		else:
			txt = "Medida ["+to+"] no soportada para CM"

		if num is None :
			return txt
		else:
			return self.r(num)

	def mm(self, n, to):
		num = None
		txt = ""
		if to == "px":
			num = (self.bFont * n) / 25.4
		elif to in ("rem", "em", "lh", "vw", "vh"):
			px = self.mm(n, "px")
			self.bFont = 16
			return self.px(px, to)
		elif to == "n%":
			return self.to_percent(n)
		elif to == "in":
			num = (n / 25.4)
		elif to == "cm":
			num = (n / 10)
		elif to == "pc":
			num = (n * (6/25.4))
		elif to == "pt":
			num = (n * (72/2.54))
		else:
			txt = "Medida ["+to+"] no soportada para MM"

		if num is None :
			return txt
		else:
			return self.r(num)

	def inches(self, n, to):
		num = None
		txt = ""
		if to == "px":
			num = self.bFont * n
		elif to in ("rem", "em", "lh", "vw", "vh"):
			px = self.inches(n, "px")
			self.bFont = 16
			return self.px(px, to)
		elif to == "n%":
			return self.to_percent(n)
		elif to == "cm":
			num = (2.54 * n)
		elif to == "mm":
			num = (25.4 * n)
		elif to == "pc":
			num = (n * 6)
		elif to == "pt":
			num = (n * 72)
		else:
			txt = "Medida ["+to+"] no soportada para IN"

		if num is None :
			return txt
		else:
			return self.r(num)

	def point(self, n, to):
		num = None
		txt = ""
		if to == "px":
			num = (n * (self.bFont / 72))
		elif to == "n%":
			return self.to_percent(n)
		elif to in ("rem", "em", "lh", "vw", "vh"):
			px = self.inches(n, "px")
			self.bFont = 16
			return self.px(px, to)
		elif to == "cm":
			num = ((n / 72) * 2.54)
		elif to == "mm":
			num = ((n / 72) * 25.4)
		elif to == "in":
			num = (n / 72)
		elif to == "pc":
			num = (n * (6 / 72))
		else:
			txt = "Medida ["+to+"] no soportada para PT"

		if num is None :
			return txt
		else:
			return self.r(num)

	def picas(self, n, to):
		num = None
		txt = ""
		if to == "px":
			num = (n * (self.bFont / 6))
		elif to == "n%":
			return self.to_percent(n)
		elif to in ("rem", "em", "lh", "vw", "vh"):
			px = self.inches(n, "px")
			self.bFont = 16
			return self.px(px, to)
		elif to == "cm":
			num = ((n / 6) * 2.54)
		elif to == "mm":
			num = ((n / 6) * 25.4)
		elif to == "in":
			num = (n / 6)
		elif to == "pt":
			num == (n * 12)
		else:
			txt = "Medida ["+to+"] no soportada para PC"

		if num is None :
			return txt
		else:
			return self.r(num)

	def lh(self, n, to):
		if to == "px":
			return self.r((n * self.bFont))
		else:
			px = self.lh(n, "px")
			return self.px(px, to)

			