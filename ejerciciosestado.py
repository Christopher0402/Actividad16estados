import boto3
import sys

# 1. Conexión a servicios
# Si sabes en qué región está tu tabla, puedes ponerla aquí, ej: region_name='us-east-1'
dynamo = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# 2. Configuración de la Tabla
nombre_tabla = 'ejercioestado'
tabla = dynamo.Table(nombre_tabla)

# 3. Entradas del usuario
print(f"--- Buscador en Tabla: {nombre_tabla} ---")
formato = input("Formato (ej: Imagen): ")
nombre_archivo = input("Nombre del archivo (ej: data.txt): ")

# 4. Buscar en DynamoDB
try:
    resp = tabla.get_item(
        Key={
            'Mexico': formato,   # Clave de Partición
            'Estados': nombre_archivo # Clave de Clasificación
        }
    )
except Exception as e:
    print(f"\n❌ Error de conexión: {e}")
    sys.exit()

# 5. Validar si el registro existe
if 'Item' not in resp:
    print(f"\n❌ No se encontró el registro con Mexico='{formato}' y Estados='{nombre_archivo}'")
    sys.exit()

item = resp['Item']
print("\n✅ Registro encontrado en DynamoDB.")

# 6. Obtener datos del Bucket y descargar
bucket_name = item.get('Bucket')
# Usamos el valor de la clave 'Estados' como nombre del archivo para S3
archivo_remoto = item.get('Estados') 

if not bucket_name:
    print("❌ El registro no contiene el campo 'Bucket'.")
    sys.exit()

try:
    print(f"Descargando '{archivo_remoto}' desde el bucket '{bucket_name}'...")
    s3.download_file(bucket_name, archivo_remoto, archivo_remoto)
    print(f"\n✨ ¡Éxito! El archivo se ha descargado correctamente en CloudShell.")
except Exception as e:
    print(f"\n❌ Error al descargar desde S3: {e}")
