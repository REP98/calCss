#!/bin/bash
# -*- ENCODING: UTF-8 -*-
echo "Calculadora Css"
mkdir -m 0775 /opt/Calculate_CSS
cp -a -v calculatecss /opt/Calculate_CSS
cp -a -v calculator1.svg /opt/Calculate_CSS
cp -a -v screen.png /opt/Calculate_CSS
cp -a -v Intructions.md /opt/Calculate_CSS
cp -a -v Uninstall.sh /opt/Calculate_CSS
cp -a -R -v image /opt/Calculate_CSS
echo "Creado Archivo Desktop"
cp -a -v calculate.desktop /usr/share/applications
echo "Listo"
echo "Gracias por instalar Calculadora CSS"