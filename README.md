	Nmap2Text.py
	
	Script en python que extrae información de un fichero Nmap en formato XML
	para que pueda ser tratado automáticamente por Nessus o Arachni.

	Este script nos retorna el contenido de un escaneo de Nmap (xml) en un 
	fichero de texto que puede ser tratado por Nessus o Arachni; con el formato
	
	ip, ip,[...] 
	para Nessus
	
	O
	
	http://ip:puerto
	http://ip:puerto
	[...]
	
	para Arachni
