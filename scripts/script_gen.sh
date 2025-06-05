#!/bin/bash

read -p "Digite o número de hectares da área florestal: " HECTARES

TOTAL=$(( (HECTARES + 499) / 500 ))  # Arredonda para cima
ORIGEM="./src"
ARQUIVO_ID="simulation.py"  # ou main.py, conforme seu projeto

echo "Serão criados $TOTAL setores (1 Raspberry Pi para cada 500 hectares)."

for i in $(seq 1 $TOTAL); do
    DESTINO="src_setor_${i}"
    cp -r "$ORIGEM" "$DESTINO"
    # Gera uma string aleatória de 16 caracteres (A-Za-z0-9)
    RAND_ID=$(cat /dev/urandom | tr -dc 'A-Za-z0-9' | head -c 16)
    # Insere o ID aleatório no início do arquivo principal da cópia
    sed -i "1i# DEVICE_ID: $RAND_ID" "$DESTINO/$ARQUIVO_ID"
    chmod -R 700 "$DESTINO"
done

chmod 700 "$0"