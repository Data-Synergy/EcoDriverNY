import pandas as pd
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular el mes y año tres meses atrás
mes_tres_meses_atras = fecha_actual.month - 3
año_tres_meses_atras = fecha_actual.year
if mes_tres_meses_atras <= 0:
    mes_tres_meses_atras += 12
    año_tres_meses_atras -= 1

# Construir el nombre del archivo Parquet
nombre_archivo = f"yellow_tripdata_{año_tres_meses_atras}-{mes_tres_meses_atras:02}.parquet"

# Construir la ruta del archivo Parquet
ruta_archivo = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{nombre_archivo}"

# Intentar cargar el archivo Parquet en un DataFrame
try:
    df_automatizado = pd.read_parquet(ruta_archivo)
    print(f"DataFrame cargado correctamente desde {ruta_archivo}")
except Exception as e:
    print(f"No se pudo cargar el archivo {nombre_archivo}: {e}")


# Configuración de las credenciales de Azure Blob Storage
account_name = 'dbstorageceyfyf6fyuxbw'
account_key = 'rH40G/3urTHoJ2R58YOKlQQ0TAQyIavk19Si1ZgLXNiAyiiLx6N31L/Iu47wiF4vbavSgROh+RXF+AStoik10A=='
container_name = 'taxisbucket'

# Crear el cliente del servicio de blob de Azure
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net/", credential=account_key)

# Obtener el cliente del contenedor
container_client = blob_service_client.get_container_client(container_name)

# Construir la ruta completa con la carpeta taxis_yellow
ruta_archivo_con_carpeta = f"taxis_yellow/{nombre_archivo}"

# Guardar el DataFrame como un archivo Parquet en el contenedor de Azure Blob Storage
blob_client = container_client.get_blob_client(ruta_archivo_con_carpeta)
with open(nombre_archivo, "wb") as data:
    df_automatizado.to_parquet(data)
blob_client.upload_blob(open(nombre_archivo, "rb"))

print(f"DataFrame guardado correctamente en el contenedor '{container_name}' de Azure Blob Storage como '{ruta_archivo_con_carpeta}'")
