#Script para extraer datos del fichero resultante de Nmap
# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import os.path as path
import xml.etree.ElementTree as ET
import os
import sys


def crea_lista(lista,servicio,ip,puerto):

  if formato == "0":
      lista.append(servicio+"://"+ip+":"+puerto)

  elif formato == "1":
      lista.append(servicio+"://"+ip)

  elif formato == "2":
      lista.append(ip+":"+puerto)

  elif formato == "3":
      lista.append(ip)


def imprime(lista):

  lista_aux = []
  flag = True
  archivo_salida = open(nom_fichero, "w")

  if multilinea == "1":
    separador = os.linesep
  else:
    separador = sep

  lista_aux = sorted(set(lista))

  for valor in lista_aux:
    if flag:
      archivo_salida.write(valor)
      flag = False
    else:
      archivo_salida.write(separador+valor)

  archivo_salida.close()

def main(fichero):
  try:
    tree = ET.parse(fichero)
  except ValueError:
    print("EL fichero no es XML")

  root = tree.getroot()
  lista = []

  for host in root.findall('host'):
    for address in host.findall('address'):
      for ports in host.findall('ports'):
        for port in ports.findall('port'):
          if "all" in args.ports:
            ip = address.get('addr')
            puerto = port.get('portid')
            servicio = port.find('./service').attrib['name']
            crea_lista (lista,servicio,ip,puerto)            

          else:
            if (port.find('./service').attrib['name'] in args.ports):
              ip = address.get('addr')
              puerto = port.get('portid')	
              servicio = port.find('./service').attrib['name']
              crea_lista (lista,servicio,ip,puerto)


  imprime (lista)

  print("Fin del proceso")

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Formatea la salida de Nmap')
	parser.add_argument("-o", action="store", dest="output",     metavar="file", help="ruta fichero salida", required=True)
	parser.add_argument("-p", action="store", dest="ports",      metavar="service", default=['all'], nargs="+", help="servicios a exportar (default: all)")
	parser.add_argument("-f", action="store", dest="format",     metavar="0 - [servicio]://[ip]:[puerto] | 1 - [servicio]://[ip] | 2 - [ip]:[puerto] | 3 - [ip]" , default="0",choices=["0", "1", "2", "3"], help="formato de salida (default: 0)")
	parser.add_argument('-m', action='store', dest='multilinea', metavar='0/1', default='1', help='imprime un resultado por linea (default: 1)')
	parser.add_argument("-s", action="store", dest="sep",        metavar="char", default="," ,help="caracter separador entre resultados (default: ,)")
	parser.add_argument("-r", action="store", dest="ruta",       metavar="XML file", help="ruta fichero XML de Nmap", required=True)
	args = parser.parse_args()


	multilinea = args.multilinea
	sep = args.sep
	ruta = args.ruta
	nom_fichero = args.output
	formato = args.format
	opcion = args.ports

	if not path.exists(ruta):
		print "Fichero XML no existe"
		sys.exit()


	main(ruta)

