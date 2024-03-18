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
    credentials_json = {
  "type": "service_account",
  "project_id": "automatizacion-taxis-nyc",
  "private_key_id": "2ddcc1ed9bce99b427c2b451aa0c3d63b1e39c51",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCxKKiLczdaG8H7\nm9XlWKNqM+sRbwFI2gtQFClPJWNsjAoBe/W8GLvr7Q3CJ6iwAW7tku6ohJyawD6R\nDkBiaM5RCSqo8SgWgZGcWb86HmF1GT10OFiZETqnxy/D7LL8e754YFy48Pp7S2qM\n9xeAqZhh8qJnMpb8b3UstizansviV6Dn33iB1EiSZ+pDhsll4KzZwd3V0ewt/uga\nQjWLhKWoKKAdEMSUMy+eUqZOA309cXnZYVNlMpOpXUgl8braLo2yUSyicbcJVaL5\nLY8YqtAwlgmVFDpM3bIZJ02V0b2o6SCZrZ0jAFdMluv3yWML1TsT/2ffo48Bz6GS\nBASbTkevAgMBAAECggEACNhG0e+Gq/EG1lEJdNHgFsVQzyYDomeAeRcImPL868Zy\nGXDe6+0wNK85KKBiQ6dOqn3TfIZiazd96DAV9tPUuScEAjtIDRea9XtlmLk7lGUW\nNF87zSiXDRlcwSNoLELhV5E4D+O4Hb++KhuMCNhuyzUZ9p0H/MJzzy+pPaD//OTd\nwzJaJBZRgpGlRdJMvsbravkgLIqrrmF700Lg5TmlwbknfMRF73MKakWxamarB0AB\naSHsKyjJImWDXndxh/MXJtXqXZwOQjQMlD/RmqjP18v4waU2i5MZIUyhFX9x0FTE\ngL9hsdo+u39PnSqR1Se16HsIzmD9zuSsAb0Ju6iUwQKBgQDoWg/Cpy84UzzidX61\nEwhgUJvMrtuZu7NqUoYLn0Lm1qBqCH5FH/e/wEiJvLsawCGQbvC1aWZHLAJOrk8E\nXYFuR5OapYsyUgh/n+vab6ESule0/3p9xJBI1GLl8AinjXyY0ztzhjTT1qKk+eqJ\n20DfYBeEGffjumgVOuKjhoxGHQKBgQDDMIpxIBXqn0/40xKE54bCD12HAc9/biKi\nVoukmC9cSSra2/INPvPvw74WTQ0freV0R8DyFbLtGfC+UdxMIO5J1B++xzHzo7ej\no2WNCJ1CvAw2uhAFE8DWdcOXrUFQ9frcd+cEljpBSksJTTDr/SIzoQ34URwBqhr1\nnmc11pxrOwKBgCbtj95o7Dxflb/LN6NWwPyCBNhSI3CqRfD2Sob/89GA+/dH3P/v\nzy5NJNoOyLo+nmD4dVOviPc7pFdSVOLCV8EGNPCf86ZGoC3huT4rnazpk3A7rWYM\n3K+XBcrIYGrSBaIFIdzFC2zCdRV22ZinJ0NFcisrvqBkxrNn3jjPfgjxAoGASvI8\nditnvurk/hmtprJvn9vegZREZB2Z1tN8UvrMVJcTiW2ih0uAxrNWLaHwRBW1YOyc\nPVfvl/K56ZntCJ4sYNS+S7aYi4B1ZrO6rmh8Wb9ywSC4PfrTtIULURYJWljYtgak\nAbLdM2yfWzb0beiIVWKlxo7+PfVe3Kix4I5DCTkCgYBt3R+wMNkkirgTob9JlpWB\nBCS+a6wqBUX6fSjx5yScTNz/GYQT4Cx96GsuQSgI0fSHTMwZRCAXHDfyHWFn/AMX\nD16VwAG68fQmNN1JhpyvNYiH6ja3jD5VMXqGq+73DlFMR6Q4tUwoeXm3zoxUijOo\nWBveGmLRDI8DRzeAYh+UvQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "cloudstorage@automatizacion-taxis-nyc.iam.gserviceaccount.com",
  "client_id": "104343921881522348990",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cloudstorage%40automatizacion-taxis-nyc.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Crear un cliente de Google Cloud Storage con las credenciales proporcionadas
fs = gcsfs.GCSFileSystem(token=credentials_json["GCP_BUCKET"])

# Guardar el DataFrame como un archivo Parquet en el bucket
with fs.open(f"{bucket_name}/{nombre_archivo}", "wb") as f:
    df_automatizado.to_parquet(f)

print(f"DataFrame guardado correctamente en gs://{bucket_name}/{nombre_archivo}")
