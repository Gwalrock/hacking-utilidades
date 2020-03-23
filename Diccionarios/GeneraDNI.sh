#!/usr/bin/env bash

function genera {

	nl="\n"
	LETRAS="TRWAGMYFPDXBNJZSQVHLCKEO"
	ndni=$1

	modulo ()
	{
	    return $(( $ndni  % 23 ))
	}

	modulo ndni
	mod=$?
	echo $ndni${LETRAS:$mod:1} >> dni.txt
}

for i in {1..1000000..1}
  do 
     genera $i
 done