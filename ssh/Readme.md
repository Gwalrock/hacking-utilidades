# Utilidades para SSH

## add_ssh_ciphers_config.sh

Crea el fichero config de ssh añadiendo los cifrados obtenidos de:
ssh -Q mac
ssh -Q kex
ssh -Q key
ssh -Q cipher

## user_enum_ssh.py

Muestra los posibles usuarios existentes a través del protocolo SSH mediante un ataque por diccionario

Se ha modificado el script de Justin Gardner para que nos muestre la información de conexión y no nos muestre los usuarios inválidos
