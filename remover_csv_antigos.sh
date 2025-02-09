#!/bin/bash

# Diret  rio onde os arquivos CSV est  o localizados (ajuste conforme necess  rio)
diretorio="/home/samba/publica"

# Data de 7 dias atras
data_limite=$(date -d "-7 days" +%Y-%m-%d)
echo "Removendo arquivos anteriores a: $data_limite"

# Percorre todos os arquivos CSV no diret  rio
for arquivo in "$diretorio"/*.csv; do
  # Obtem uma data de modificao do arquivo
  data_modificacao=$(stat -c %W "$arquivo")
  data_formatada=$(date -d "@$data_modificacao" +"%Y-%m-%d")
  # Compara as datas
  if [[ "$data_formatada" < "$data_limite" ]]; then
    echo "Removendo arquivo: $arquivo"
    #rm "$arquivo"
  fi
done