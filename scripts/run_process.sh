#!/bin/bash
# Ir a la carpeta del proyecto
cd /home/ec2-user/proyecto || exit

# Ejecutar el script (asegúrate de que el nombre sea exacto)
python3 process_data.py

# Esperar 2 segundos para asegurar que el archivo se escribió
sleep 2

# Subir usando la ruta relativa (más seguro)
aws s3 cp resultado.txt s3://actividad16estados/ --acl public-read