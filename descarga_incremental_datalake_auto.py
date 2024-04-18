import os
import snowflake.connector
import pandas as pd
import requests
from io import BytesIO
from pyspark.sql import SparkSession
import tempfile
from datetime import datetime, timedelta
from pyspark.sql import functions as F
from pyspark.sql.functions import when
from pyspark.sql.window import Window
from pyspark.sql.functions import min, max, hour, to_timestamp, round


import snowflake.connector
import requests
import tempfile
import os
from datetime import datetime, timedelta
import calendar

# Configuración de conexión a Snowflake
conn = snowflake.connector.connect(
    user='ELIASALMADA1234',
    password='Ichi2017',
    account='pzbgdyt-aib83585',
    warehouse='COMPUTE_WH',
    database='SCHEMA_TAXIS_NYC_ECODRIVE',
    schema='PUBLIC'
)

# Nombre del stage en Snowflake donde deseas cargar los archivos
stage_name = 'DATALAKE_TAXIS_NYC'

# Obtener la fecha actual y calcular la fecha de tres meses atrás
current_date = datetime.now()
last_month_end = current_date.replace(day=1) - timedelta(days=1)
three_months_ago = last_month_end.replace(day=1) - timedelta(days=last_month_end.day - 1)

# Obtener el año y el mes del archivo Parquet correspondiente a tres meses atrás
year_three_months_ago = three_months_ago.year
month_three_months_ago = three_months_ago.month

# Construir el nombre del archivo Parquet
file_name = f"yellow_tripdata_{year_three_months_ago}-{month_three_months_ago:02}.parquet"

# URL del archivo Parquet
file_link = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"

# Descargar el archivo Parquet desde la URL
response = requests.get(file_link)

# Crear un archivo temporal para almacenar los datos con el nombre deseado
temp_file = tempfile.NamedTemporaryFile(suffix='.parquet', prefix=file_name, delete=False)
temp_file_path = temp_file.name
temp_file.write(response.content)
temp_file.close()  # Cerrar el archivo temporal antes de cambiar el nombre

# Cambiar el nombre del archivo temporal
final_file_path = os.path.join(tempfile.gettempdir(), file_name)
os.rename(temp_file_path, final_file_path)

# Cargar el archivo Parquet en el stage de Snowflake
with conn.cursor() as cursor:
    put_statement = f"PUT 'file://{final_file_path}' @\"SCHEMA_TAXIS_NYC_ECODRIVE\".\"PUBLIC\".\"{stage_name}\""
    cursor.execute(put_statement)

# Cerrar la conexión
conn.close()


# Conexión a Snowflake
conn = snowflake.connector.connect(
    user='ELIASALMADA1234',
    password='Ichi2017',
    account='pzbgdyt-aib83585',
    warehouse='COMPUTE_WH',
    database='SCHEMA_TAXIS_NYC_ECODRIVE',
    schema='PUBLIC'
)

# Consulta para obtener el nombre del último archivo Parquet
query = f"""
SELECT metadata$filename
FROM @SCHEMA_TAXIS_NYC_ECODRIVE.PUBLIC.DATALAKE_TAXIS_NYC
ORDER BY metadata$filename = '{file_name}' DESC
LIMIT 1
"""

# Ejecutar la consulta
cursor = conn.cursor()
cursor.execute(query)

# Obtener el nombre del archivo Parquet
filename = cursor.fetchone()[0]


# Construir la ruta completa del archivo local descargado
filepath = os.path.join(filename)

# Configurar SparkSession
spark = SparkSession.builder \
    .appName("Read Parquet from GitHub") \
    .getOrCreate()

temp_file = tempfile.NamedTemporaryFile(prefix=filepath, delete=False)
temp_file_path = temp_file.name
temp_file.write(response.content)
temp_file.close()  # Cerrar el archivo temporal antes de cambiar el nombre

final_file_path = os.path.join(tempfile.gettempdir(), file_name)
os.rename(temp_file_path, final_file_path)

df_total = spark.read.parquet(final_file_path)




# Configurar SparkSession
spark = SparkSession.builder \
    .appName("Read Parquet from GitHub") \
    .getOrCreate()

# URL del archivo Parquet en GitHub
parquet_url = "https://github.com/Data-Synergy/EcoDriverNY/raw/main/data/daily_weather_data.parquet"

file_name = "water_temp"

# Descargar el archivo Parquet
response = requests.get(parquet_url)
parquet_data = BytesIO(response.content)

temp_file = tempfile.NamedTemporaryFile(suffix='.parquet', prefix=file_name, delete=False)
temp_file_path = temp_file.name
temp_file.write(response.content)
temp_file.close()  # Cerrar el archivo temporal antes de cambiar el nombre

final_file_path = os.path.join(tempfile.gettempdir(), file_name)
os.rename(temp_file_path, final_file_path)

# Leer el archivo Parquet en un DataFrame de Spark
daily_weather_data_spark = spark.read.parquet(final_file_path)


df_total_fh = df_total [['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount', 'congestion_surcharge', 'airport_fee']]

# Convierte la columna 'tpep_pickup_datetime' a tipo timestamp
df_total_fh = df_total_fh.withColumn('tpep_pickup_datetime', F.to_timestamp(df_total_fh['tpep_pickup_datetime']))

# Extrae la parte de la fecha y asigna a una nueva columna 'date_only'
df_total_fh = df_total_fh.withColumn('date_only', F.to_date(df_total_fh['tpep_pickup_datetime']))
daily_weather_data_spark = daily_weather_data_spark [['date', 'temperature_2m_mean', 'precipitation_sum']]
daily_weather_data = daily_weather_data_spark

# Convierte la columna 'date' a tipo timestamp
daily_weather_data = daily_weather_data.withColumn('date', F.to_timestamp(daily_weather_data['date']))

# Extrae la parte de la fecha y asigna a una nueva columna 'date_only'
daily_weather_data = daily_weather_data.withColumn('date_only', F.to_date(daily_weather_data['date']))

# Realizar la unión de DataFrames en PySpark
merged_df = df_total_fh.join(daily_weather_data, on='date_only', how='left')

# Mostrar el DataFrame resultante
#merged_df.show()

# Reemplazar los valores nulos en la columna 'passenger_count' con 1

merged_df = merged_df.withColumn('passenger_count', when(merged_df['passenger_count'].isNull(), 1).otherwise(merged_df['passenger_count']))

# Reemplazar los valores nulos en la columna 'congestion_surcharge' con 0
merged_df = merged_df.withColumn('congestion_surcharge', when(merged_df['congestion_surcharge'].isNull(), 0).otherwise(merged_df['congestion_surcharge']))

# Reemplazar los valores nulos en la columna 'airport_fee' con 0
merged_df = merged_df.withColumn('airport_fee', when(merged_df['airport_fee'].isNull(), 0).otherwise(merged_df['airport_fee']))



# Mostrar el DataFrame resultante
#merged_df.show()

merged_df_sin_nulos = merged_df.na.drop()
# Reemplazar los valores distintos de cero por 1 en la columna 'temperature_2m_mean'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('precipitation_sum', when(merged_df_sin_nulos['precipitation_sum'] != 0, 1).otherwise(0))

# Reemplazar los valores distintos de cero por 1 en la columna 'congestion_surcharge'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('congestion_surcharge', when(merged_df_sin_nulos['congestion_surcharge'] != 0, 1).otherwise(0))

# Reemplazar los valores distintos de cero por 1 en la columna 'airport_fee'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('airport_fee', when(merged_df_sin_nulos['airport_fee'] != 0, 1).otherwise(0))

# Mostrar el DataFrame resultante
#merged_df_sin_nulos.show()
# Convertir la columna 'tpep_pickup_datetime' a tipo timestamp
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('tpep_pickup_datetime', F.to_timestamp(merged_df_sin_nulos['tpep_pickup_datetime']))

# Extraer la hora de la columna 'tpep_pickup_datetime' y asignarla a la nueva columna 'franja_horaria'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('franja_horaria', hour(merged_df_sin_nulos['tpep_pickup_datetime']))

# Mostrar el DataFrame resultante
#merged_df_sin_nulos.show()

# Convertir las columnas 'tpep_pickup_datetime' y 'tpep_dropoff_datetime' a tipo datetime si no lo están
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('tpep_pickup_datetime', to_timestamp(merged_df_sin_nulos['tpep_pickup_datetime']))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('tpep_dropoff_datetime', to_timestamp(merged_df_sin_nulos['tpep_dropoff_datetime']))

# Calcular la duración del viaje en minutos y redondear el resultado a 2 decimales
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('duracion_viaje_minutos',
                                                     round(((F.col('tpep_dropoff_datetime').cast('long') - F.col('tpep_pickup_datetime').cast('long')) / 60), 2))
# Cerrar SparkSession


# Define la ventana de partición
window_spec = Window.partitionBy('date_only', 'franja_horaria')

# Agrupar por fecha y franja horaria y sumar los viajes en cada grupo
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_viajes', F.count('passenger_count').over(window_spec))

# Agrupar por fecha y franja horaria y sumar los pasajeros en cada grupo
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_pasajeros', F.sum('passenger_count').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y sumamos 'trip_distance'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_distancias', F.sum('trip_distance').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y sumamos 'total_amount'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_tarifas', F.sum('total_amount').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y promediamos 'congestion_surcharge'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_congestion', F.avg('congestion_surcharge').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y promediamos 'airport_fee'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_aeropuerto', F.avg('airport_fee').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y promediamos 'temperature_2m_mean'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_temperatura', F.avg('temperature_2m_mean').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y promediamos 'precipitation_sum'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_presipitaciones', F.avg('precipitation_sum').over(window_spec))

# Aquí agrupamos por 'date_only' y 'franja_horaria' y sumamos 'duracion_viaje_minutos'
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_duracion_viajes_minutos', F.sum('duracion_viaje_minutos').over(window_spec))


# Redondear todas las salidas a 2 decimales
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_viajes', F.round('suma_viajes', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_pasajeros', F.round('suma_pasajeros', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_distancias', F.round('suma_distancias', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_tarifas', F.round('suma_tarifas', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_congestion', F.round('promedio_congestion', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_aeropuerto', F.round('promedio_aeropuerto', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_temperatura', F.round('promedio_temperatura', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('promedio_presipitaciones', F.round('promedio_presipitaciones', 2))
merged_df_sin_nulos = merged_df_sin_nulos.withColumn('suma_duracion_viajes_minutos', F.round('suma_duracion_viajes_minutos', 2))

# Mostrar el DataFrame resultante
#merged_df_sin_nulos.show()

# Lista de columnas a eliminar
columnas_a_eliminar = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'duracion_viaje_minutos','passenger_count', 'trip_distance', 'total_amount', 'congestion_surcharge', 'airport_fee', 'pickup_date', 'date', 'temperature_2m_mean', 'precipitation_sum']

# Eliminar las columnas
merged_df_sin_nulos = merged_df_sin_nulos.drop(*columnas_a_eliminar)

# Mostrar el DataFrame resultante
#merged_df_sin_nulos.show()
# Eliminar filas completamente duplicadas
merged_df_sin_nulos = merged_df_sin_nulos.dropDuplicates()
merged_df_sin_nulos_pandas = merged_df_sin_nulos.toPandas()

import tempfile
import os

# Crear un archivo temporal para almacenar el DataFrame en formato Parquet
temp_file = tempfile.NamedTemporaryFile(suffix='.parquet', prefix='ml2_', delete=False)
temp_file_path = temp_file.name

# Guardar el DataFrame en formato Parquet
merged_df_sin_nulos_pandas.to_parquet(temp_file_path)



# Ruta del archivo Parquet final
final_file_path = temp_file_path 

fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Crear el nombre del archivo Parquet con la fecha actual
parquet_filename = f"DATALAKE_ML_FR_HR{fecha_actual}.parquet"


# Crear un archivo temporal para almacenar el DataFrame
temp_file = tempfile.NamedTemporaryFile(suffix='.csv', prefix='ml2_', delete=False)
temp_file_path = temp_file.name

# Guardar el DataFrame en formato CSV
merged_df_sin_nulos_pandas.to_csv(temp_file_path, index=False)

# Ruta del archivo temporal
final_file_path = temp_file_path 

fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Crear el nombre del archivo CSV con la fecha actual
csv_filename = f"DATALAKE_ML_FR_HR{fecha_actual}.csv"

# Mover el archivo temporal al nombre final
csv_output_path = os.path.join(csv_filename)
os.rename(temp_file_path, csv_output_path)

# Imprimir la ruta del archivo CSV final
print("Ruta del archivo CSV:", csv_output_path)

# Conexión a Snowflake
conn = snowflake.connector.connect(
    user='ELIASALMADA1234',
    password='Ichi2017',
    account='pzbgdyt-aib83585',
    warehouse='COMPUTE_WH',
    database='SCHEMA_TAXIS_NYC_ECODRIVE',
    schema='PUBLIC'
)

# Nombre del stage de Snowflake
stage_name = "DATALAKE_ML_FR_HR"

# Cargar el archivo CSV en el stage de Snowflake
try:
    with conn.cursor() as cursor:
        put_statement = f"PUT 'file://{csv_output_path}' @\"SCHEMA_TAXIS_NYC_ECODRIVE\".\"PUBLIC\".\"{stage_name}\""
        cursor.execute(put_statement)
    print("Archivo CSV cargado exitosamente en el stage de Snowflake.")
except Exception as e:
    print("Error al cargar el archivo CSV en el stage de Snowflake:", str(e))
finally:
    conn.close()


# Conexión a Snowflake
conn = snowflake.connector.connect(
    user='ELIASALMADA1234',
    password='Ichi2017',
    account='pzbgdyt-aib83585',
    warehouse='COMPUTE_WH',
    database='SCHEMA_TAXIS_NYC_ECODRIVE',
    schema='PUBLIC'
)


# Ejecutar la consulta
cursor = conn.cursor()


query =f"""COPY INTO "SCHEMA_TAXIS_NYC_ECODRIVE"."PUBLIC"."ML_FR_HR_WH"
FROM '@"SCHEMA_TAXIS_NYC_ECODRIVE"."PUBLIC"."DATALAKE_ML_FR_HR"'
FILES = ('{csv_output_path}.gz')
FILE_FORMAT = (
    TYPE=CSV,
    SKIP_HEADER=1,
    FIELD_DELIMITER=',',
    TRIM_SPACE=FALSE,
    FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
    REPLACE_INVALID_CHARACTERS=TRUE,
    DATE_FORMAT=AUTO,
    TIME_FORMAT=AUTO,
    TIMESTAMP_FORMAT=AUTO
)
ON_ERROR=ABORT_STATEMENT;"""


cursor.execute(query)

conn.close()
