#!/bin/bash
# -*- ENCODING: UTF-8 -*-
echo "Calculadora Css"
echo "Generando Ejeutable"

VERSION="1.0"
DIST_DIRECTORY="./dist"

NAMEROOT="Calulate_CSS"
DIROUT="./dist/$NAMEROOT"

STPL="./stpl"

ROOTPATH=$PWD

pyinstaller -w -F -y \
	--clean \
	--icon=./image/png/calculator1.ico \
	 --add-data="./image:./image" \
	--add-data="README.md:." \
	--add-data="LICENSE:." \
	--hidden-import='PIL._tkinter_finder' \
	calculatecss.py


if [ -d $DIST_DIRECTORY ]
then
	echo "Entrando en la carpeta dist"
	cd dist
	if [ ! -d $NAMEROOT ]
	then
		echo "Creado Directorio $NAMEROOT"
		mkdir -m 0775 $NAMEROOT
	fi
	echo "Creando Instaladores"	
	mv -v calculatecss $NAMEROOT
	echo "Regresando a la Raiz"
	cd $ROOTPATH 
	echo "Copiando Templates"
	cp -a -v "image/svg/calculator1.svg" $DIROUT
	cp -a -v "image/screen.png" $DIROUT
	cp -a -v "$STPL/calculate.desktop" $DIROUT
	cp -a -v "$STPL/Intructions.md" $DIROUT
	cp -a -v "$STPL/Setup.sh" $DIROUT
	cp -a -v "$STPL/Uninstall.sh" $DIROUT
	cp -a -R -v image $DIROUT
	echo "Entrando en la carpeta dist"
	cd dist
	tar -cvzf "calculatecss-v$VERSION.tar.gz" $NAMEROOT
	mv -v "calculatecss-v$VERSION.tar.gz" $ROOTPATH
	echo "Regresando a la Raiz"
	cd $ROOTPATH 
	echo "Limpiando Basura"
	rm -v -R dist
	rm -v -R build
fi

echo "Proceso Finalizado"

exit 0