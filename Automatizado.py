# Databricks notebook source
import pandas as pd
from datetime import datetime, timedelta
from google.auth import load_credentials_from_file
from pandas.io import gbq

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

credentials, project_id = load_credentials_from_file(
    "/Workspace/Users/eliasemanuelalmada5757@gmail.com/basestaxis/automatizacion-taxis-nyc-d47c13651bca.json"
)

# Asignar el ID del proyecto a la variable project_id
project_id = "automatizacion-taxis-nyc"


df_automatizado.to_gbq(destination_table="basededatos_taxis.automatizado",
                       project_id=project_id,
                       if_exists="append",
                       credentials=credentials)
print("DataFrame cargado a BigQuery correctamente.")
