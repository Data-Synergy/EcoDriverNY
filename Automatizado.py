import os
import pandas as pd
from datetime import datetime, timedelta
from google.auth import load_credentials_from_file
from pandas.io import gbq
import gcsfs
import json  # Agregar esta línea

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

# Definir el nombre del bucket
bucket_name = "bucketpgrupal"

# Cargar las credenciales desde el archivo JSON
with open('secret.json') as json_file:
    credentials_json = json.load(json_file)

# Crear un cliente de Google Cloud Storage con las credenciales proporcionadas
fs = gcsfs.GCSFileSystem(token=credentials_json["GCP_BUCKET"])

# Guardar el DataFrame como un archivo Parquet en el bucket
with fs.open(f"{bucket_name}/{nombre_archivo}", "wb") as f:
    df_automatizado.to_parquet(f)

print(f"DataFrame guardado correctamente en gs://{bucket_name}/{nombre_archivo}")
