#!/usr/bin/python
#-*- coding: utf-8 -*-

#Ejercicio-JSON
#ÁLVARO SOLA OLIVERO

import json
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

with open("accidente.json") as fichero:
	datos = json.load(fichero)

#1 - Lista todos los accidentes.

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

for colision in datos["result"]:
	for vehiculo in colision["vehiculo"]:
		if pregunta in vehiculo["type"]:
			print "Tipo de accidentes en",pregunta,":",colision["type"]

print "----------------------------------------------------"

#4 - Introduzca una fecha inicial y una fecha final y muestra los accidentes producidos en ese intervalo.

#formato="%y-%m-%d"

fech_ini=raw_input("Introduzca una fecha inicial (AAAA-MM-DD), ejemplo(2013-12-20):")

if fech_ini=="":
	print "Error, introduzca valor como se pide."

fech_fin=raw_input("Introduzca una fecha final (AAAA-MM-DD), ejemplo(2013-12-25):")
		
if fech_fin=="":
	print "Error, introduzca valor como se pide."

if fech_fin>=fech_ini:
   	for accidente in datos["result"]:
   		if fech_ini and fech_fin in accidente["creationDate"]:
   			print "Accidente dentro de ese intervalo:",accidente["type"]

else:
   	print "La fecha final debe ser mayor o igual que la inicial"

print "----------------------------------------------------"

#5 - Introduce por teclado una cadena, si esta dentro de la razón del accidente, muestra la razón del accidente, sino devuelve un error.

pregunta1=raw_input("Introduce una cadena:")
print "La siguiente cadena",pregunta1,"aparece en las siguientes razones de accidentes:"

if pregunta1!="":
	for cadena in datos["result"]:
		if pregunta1.lower() in cadena["reason"].lower():
			print cadena["reason"]
else:
	print "Error."

#6- Ejercicio de Jose Domingo

fich="accidente.html"
archivo=open(fich,"w")
for elemento in datos["result"]:
	tipo=elemento["type"]
	razon=elemento["reason"]

	for lista in elemento["afectado"]:
		ano=lista["age"]
		estado=lista["status"]
			
	archivo.write("<h1>"+str(tipo)+"</h1>")
	archivo.write("<p>"+str(razon)+"</p>")
	archivo.write("<ul>")
	archivo.write("<li>"+str(ano)+"</li>")
	archivo.write("<li>"+str(estado)+"</li>")
	archivo.write("</ul>")
archivo.close()