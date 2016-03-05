#!/usr/bin/python
#-*- coding: utf-8 -*-

#Ejercicio-JSON
#ÁLVARO SOLA OLIVERO

#1 - Lista todos los accidentes.

import json

with open("accidente.json") as fichero:
	datos = json.load(fichero)

print "Lista de accidentes:"
print "--------------------------------"

for x in datos["result"]:
	print x["type"]

print "--------------------------------"

#2 - Muestra el número de accidentes.

contador=0
for total in datos["result"]:
	contador=contador+1
print "Total de accidentes:",contador
print "--------------------------------"

#3 - Pide por teclado un vehiculo y muestra cual es el tipo de accidente.

pregunta=raw_input("Introduzca un vehiculo:")

#4 - Introduzca una fecha inicial y una fecha final y muestra los accidentes producidos en ese intervalo.

#5 - Introduce por teclado una cadena, si esta dentro de algún comentario, muestra el comentario del accidente, sino devuelve un error. 