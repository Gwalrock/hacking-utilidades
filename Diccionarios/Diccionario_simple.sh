#! /bin/bash
#script que genera un diccionario concatenando las lineas una a una de dos ficheros en ambos sentidos y los añade al inicio
#la salida se vuelca en el tercer parametro
#si no hay tercer parametro se vuelca en el fichero dic.txt
#Autor: Gwalrock


if [ -n "$3" ]; then
        fsalida=$3
else
        fsalida=dic.txt
fi

if [ -f $fsalida ]; then
  rm -f $fsalida
fi

cat $1 $2 >> $fsalida

while read lineaf1
do

   while read lineaf2
   do

     echo "${lineaf1}${lineaf2}" >> $fsalida
     echo "${lineaf2}${lineaf1}" >> $fsalida

   done < $2

done < $1