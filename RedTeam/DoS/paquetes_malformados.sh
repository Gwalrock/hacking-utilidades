#!/bin/bash

# Configura el IP y puerto a testear
host="127.0.0.1" # IP a testear
port=4444  # Puerto a testear

# Número de llamadas que quieres enviar
num_llamadas=100  # Puedes modificar este valor

# Lista de tramas malformadas
tramas_malformadas=(
  "incomplet"  # Comando incompleto
  "ff ff ff ff"  # Datos hexadecimales erróneos
  "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"  # Simulando una trama HTTP
  "malformed_xxx_command"  # Comando ficticio
  "\xff\xff\xff\xff"  # Trama corrupta en binario
  "LONG_COMMAND_$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 1024)"  # Comando largo aleatorio
)

# Función para enviar tramas con netcat
enviar_trama() {
    echo -e "$1" | nc -n -w 1 $host $port
}

# Enviar X llamadas
for ((i=1; i<=num_llamadas; i++))
do
    # Obtener la trama malformada en secuencia (mod X para ciclar entre tramas)
    index=$(( (i - 1) % ${#tramas_malformadas[@]} ))
    trama="${tramas_malformadas[$index]}"

    # Mostrar la trama enviada y su número de llamada
    echo "Llamada $i: Enviando trama malformada: $trama"

    # Enviar la trama
    enviar_trama "$trama"

    # Opcional: añadir una pequeña pausa para no saturar demasiado rápido
    #sleep 0.5
done
