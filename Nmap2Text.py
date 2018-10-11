#Script para extraer datos del fichero resultante de Nmap
# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import os.path as path
import xml.etree.ElementTree as ET
import os
import sys

def imprime(archivo_nessus,archivo_arachni,ip,puerto):

  if imprimir == "3":	
    print ip+":"+puerto
  elif imprimir == "2":
    archivo_arachni.write("http://"+ip+":"+puerto + os.linesep)
    archivo_nessus.write(ip+":"+puerto+", ")
  elif imprimir == "1":
    archivo_arachni.write("http://"+ip+":"+puerto + os.linesep)
  elif imprimir == "0":
    archivo_nessus.write(ip+":"+puerto +", ")

def main(fichero):
  try:
    tree = ET.parse(fichero)
  except ValueError:
    print("EL fichero no es XML")

  root = tree.getroot()

  if (imprimir == "0" or imprimir =="2"):
    archivo_nessus = open("Nmap2Nessus.txt", "w")

  if (imprimir == "1" or imprimir =="2"):
    archivo_arachni = open("Nmap2Arachni.txt", "w")

  for host in root.findall('host'):
    for address in host.findall('address'):
      for ports in host.findall('ports'):
        for port in ports.findall('port'):
          if opcion == "0":
            ip = address.get('addr')
            puerto = port.get('portid')
            if (imprimir == "0"):
              imprime(archivo_nessus,"",ip,puerto)
            elif (imprimir == "1"):
              imprime("",archivo_arachni,ip,puerto)
            elif (imprimir == "2"):
              imprime(archivo_nessus,archivo_arachni,ip,puerto)
            else:
              imprime("","",ip,puerto)
              

          else:
            if (port.find('./service').attrib['name'] == "http" or port.find('./service').attrib['name'] == "https"):
              ip = address.get('addr')
              puerto = port.get('portid')	
              if (imprimir == "0"):
                imprime(archivo_nessus,"",ip,puerto)
              elif (imprimir == "1"):
                imprime("",archivo_arachni,ip,puerto)
              elif (imprimir == "2"):
                imprime(archivo_nessus,archivo_arachni,ip,puerto)
              else:
                imprime("","",ip,puerto)

  if (imprimir == "0" or imprimir =="2"):
    archivo_nessus.close()

  if (imprimir == "1" or imprimir =="2"):
    archivo_arachni.close()

if __name__ == "__main__":

	print "------------------------------------------------------"
	print "-            Extracción de datos de NMAP             -"
	print "------------------------------------------------------"
	print "------------------------------------------------------"
	print "-Tip:  Extrae la información de un fichero Nmap (XML)-"
	print "-      que puede ser volcada en dos ficheros de texto-"
	print "-      para que sean procesados por Nessus o Arachni -"
	print "------------------------------------------------------"
	print "Seleccione opcion:"
	print "0 - Todos los puertos (por defecto)"
	print "1 - Solo http y https"
	print "S - Salir"

	while True:
		try:
			opcion = raw_input("Introduzca opción: ")
			if (opcion == "S"):
				sys.exit()
			if (opcion == ""):
				opcion = "0"
			if (opcion == "0" or opcion =="1"):
				break
			else:
				print "Opción no válida"
		except ValueError:
			print("Dato no válido, solo se admiten números")

	print "Seleccione opcion:"
	print "0 - Impresión para escaneo múltiple con Nessus"
	print "1 - Impresión para escaneo múltiple con Arachni"
	print "2 - Impresión para escaneo múltiple con ambos"
	print "3 - Solo visualización (por defecto)"
	print "S - Salir"

	while True:
		try:
			imprimir = raw_input("Introduzca opción: ")
			if (imprimir == "S"):
				sys.exit()
			if (imprimir == ""):
				imprimir = "3"
			if (imprimir == "0" or imprimir == "1" or imprimir == "2" or imprimir == "3"):
				break
			else:
				print "Opción no válida"
		except ValueError:
			print("Dato no válido, solo se admiten números")

	while True:
		ruta = raw_input("Introduzca la ruta del fichero Nmap (S salir): ")
		if (ruta == "S"):
			sys.exit()
		if path.exists(ruta):
			break
		else:
			print("Fichero no existente o no valido")


	main(ruta)

