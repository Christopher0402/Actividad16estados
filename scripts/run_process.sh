#!/bin/bash

# 1. Entrar a la carpeta donde CodeDeploy descargó los archivos
cd /home/ec2-user/proyecto

# 2. Asegurarse de que el script de Python tenga permisos de ejecución (opcional)
chmod +x process_data.py

# 3. Ejecutar el script de Python para generar 'resultado.txt'
# Usamos python3 porque es el estándar en las AMIs de Amazon Linux
python3 process_data.py

# 4. Subir el archivo generado a S3
# REEMPLAZA 'tu-nombre-de-bucket' con el nombre real de tu bucket de S3
aws s3 cp resultado.txt s3://actividad16estados/ --acl public-read

# 5. (Opcional) Mensaje de confirmación en los logs de CodeDeploy
echo "Procesamiento completado y archivo subido a S3."