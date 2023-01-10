import os
from distutils.core import setup

CURRENT_PATH = os.path.abspath(os.getcwd())+'/image/png/calculator1.png'

desc="""\
# calCss
Calculadora de unidades CSS


![ScreenShot](data:image/png;base64,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)

Hecha en Python, pensada en los desarrolladores frontEnd
Licensia MIT
"""

setup(
	name="Calculadora CSS",
	version="1.1",
	packages=["bin"],
	url="https://github.com/REP98/calCss",
	download_url="https://github.com/REP98/calCss/release",
	license="MIT",
	author="Robert Pérez",
	author_email="delfinmundo@gmail.com",
	description=desc,
	package_data={'.': "*.py"},
	requires=["tkinter","os","PIL","re", "webbrowser"],
	scripts=["calculatecss.py"],
	data_files=[("image", ("image/**/.svg", "image/**/.png"))],
	classifiers=[
		"License :: MIT",
		'Programming Language :: Python',
		'Operating System :: Unix :: Linux'
	]
)