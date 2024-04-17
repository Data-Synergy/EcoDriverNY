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
    database='DATALAKE',
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
    put_statement = f"PUT 'file://{final_file_path}' @\"DATALAKE\".\"PUBLIC\".\"{stage_name}\""
    cursor.execute(put_statement)

# Cerrar la conexión
conn.close()
