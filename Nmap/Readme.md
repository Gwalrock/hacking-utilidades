Nmap2Text.py

Formatea la salida de los Xml de Nmap
Se le debe indicar un fichero de salida y el fichero Xml de Nmap a tratar

Los servicios a formatear se indican con la opción -p, por defecto muestra todos.

El formato de salida se indica con la opción -f, puede ser
0 - [servicio]://[ip]:[puerto] (opción por defecto)
1 - [servicio]://[ip] 
2 - [ip]:[puerto] 
3 - [ip]

Para mostrar los resultados en una sola linea indicarlo con la opción -m 0, por defecto la opción -m tiene valor 1


Ejemplos:

Para salida con formato aceptado por Nessus (todo en una misma linea y separado por comas)
#python Nmap2Text.py  -o xml_tratado.txt -r tcp_scan.xml -m 0 -s , -f 3

ip,ip,ip,...

Para salida con formato aceptado por Arachni (resultados en distintas lineas)
#python Nmap2Text.py  -o xml_tratado.txt -r tcp_scan.xml -p http,https -f 1

http://ip
https://ip
[...]


#python Nmap2Text.py -h

usage: v3Nmap2Text.py [-h] -o file [-p service [service ...]]
                      [-f 0 - [servicio]://[ip]:[puerto] | 1 -
                      [servicio]://[ip] | 2 - [ip]:[puerto] | 3 - [ip]]
                      [-m 0/1] [-s char] -r XML file

Formatea la salida de Nmap

optional arguments:
  -h, --help                  show this help message and exit
  -o file                     ruta fichero salida
  -p service [service ...]    servicios a exportar (default: all)
  -f 0 - [servicio]://[ip]:[puerto] | 1 - [servicio]://[ip] | 2 - [ip]:[puerto] | 3 - [ip]
                              formato de salida (default: 0)
  -m 0/1                      imprime un resultado por linea (default: 1)
  -s char                     caracter separador entre resultados (default: ,)
  -r XML file                 ruta fichero XML de Nmap
