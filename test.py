import pandas as pd
import psycopg2
from datetime import datetime, timedelta

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

# Detalles de la conexión a PostgreSQL
host = "bivcrdepa3dc6zn6enju-postgresql.services.clever-cloud.com"
database = "bivcrdepa3dc6zn6enju"
user = "uyomkpixi8ntfsmrgzgi"
password = "F2kDStOnYq4NGphr65HyLtudOh63rq"
port = "50013"


# Intentar cargar el archivo Parquet en un DataFrame
try:
    df = pd.read_parquet(ruta_archivo)
    print(f"DataFrame cargado correctamente desde {ruta_archivo}")
except Exception as e:
    print(f"No se pudo cargar el archivo {nombre_archivo}: {e}")

# Establecer conexión a PostgreSQL
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Nombre de la tabla en PostgreSQL
table_name = "taxis_final"

# Crear un cursor
cur = conn.cursor()

# Iterar sobre las filas del DataFrame y ejecutar INSERT INTO para cada fila
for index, row in df.iterrows():
    cur.execute("""
    INSERT INTO taxis_final (
        VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance,
        RatecodeID, store_and_fwd_flag, PULocationID, DOLocationID, payment_type, fare_amount,
        extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount,
        congestion_surcharge, airport_fee
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# Confirmar la ejecución de la transacción
conn.commit()

# Cerrar el cursor y la conexión
cur.close()
conn.close()

print("Datos cargados en la tabla en PostgreSQL.")
