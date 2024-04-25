import streamlit as st
import pandas as pd
from datetime import datetime
import mysql.connector

# Función para conectar a la base de datos MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Función para crear la base de datos si no existe
def crear_base_datos():
    try:
        conexion = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")
        conexion.close()
    except mysql.connector.Error as error:
        st.error(f'Error al crear la base de datos: {error}')

# Función para crear la tabla si no existe
def crear_tabla():
    try:
        conexion = conectar_mysql()
        cursor = conexion.cursor()
        cursor.execute(f"USE {MYSQL_DATABASE}")
        cursor.execute("""CREATE TABLE IF NOT EXISTS uso_vehiculos_electricos (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            Fecha DATE,
                            Millas_Elec_T1 FLOAT,
                            Millas_Elec_T2 FLOAT,
                            Millas_Elec_T3 FLOAT,
                            Millas_Conv_T1 FLOAT,
                            Millas_Conv_T2 FLOAT,
                            Millas_Conv_T3 FLOAT,
                            Porcentaje_Participacion_Flota_Electrica FLOAT
                        )""")
        conexion.close()
    except mysql.connector.Error as error:
        st.error(f'Error al crear la tabla: {error}')

# Función para registrar el uso de vehículos eléctricos en la base de datos MySQL
def usoelectrico(Fecha: datetime, millas_electrico_turno_1: float,
                  millas_electrico_turno_2: float, millas_electrico_turno_3: float,
                  millas_convencionales_turno_1: float, millas_convencionales_turno_2: float,
                  millas_convencionales_turno_3: float):

    try:
        # Conectar a la base de datos MySQL
        conexion = conectar_mysql()
        cursor = conexion.cursor()

        # Verificar si la tabla existe, de lo contrario, crearla
        crear_tabla()

        # Calcular el porcentaje de participación de la flota eléctrica
        total_millas_dia = millas_electrico_turno_1 + millas_electrico_turno_2 + millas_electrico_turno_3 + millas_convencionales_turno_1 + millas_convencionales_turno_2 + millas_convencionales_turno_3
        porcentaje_participacion_flota_electrica = ((millas_electrico_turno_1 + millas_electrico_turno_2 + millas_electrico_turno_3) / total_millas_dia) * 100

        # Insertar el registro en la tabla
        sql = """INSERT INTO uso_vehiculos_electricos 
                 (Fecha, Millas_Elec_T1, Millas_Elec_T2, Millas_Elec_T3, Millas_Conv_T1, Millas_Conv_T2, Millas_Conv_T3, Porcentaje_Participacion_Flota_Electrica) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3, 
               millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3, 
               porcentaje_participacion_flota_electrica)
        cursor.execute(sql, val)

        # Confirmar la inserción y cerrar la conexión
        conexion.commit()
        cursor.close()
        conexion.close()

        st.success('¡Registro exitoso en la base de datos!')

        return porcentaje_participacion_flota_electrica  # Retornar el porcentaje para mostrar en Streamlit

    except mysql.connector.Error as error:
        st.error(f'Error al registrar en la base de datos: {error}')

# Función para calcular el cumplimiento del KPI
def cumplimientoKPI(Fecha_analisis : datetime):
    # Convertir la fecha de análisis a formato de cadena
    fecha_analisis_str = Fecha_analisis.strftime('%Y-%m-%d')

    # Leer la tabla de la base de datos
    try:
        conexion = conectar_mysql()
        cursor = conexion.cursor()
        cursor.execute(f"USE {MYSQL_DATABASE}")
        cursor.execute("SELECT * FROM uso_vehiculos_electricos WHERE Fecha = %s", (Fecha_analisis,))
        flotaElectrica = cursor.fetchall()
        conexion.close()
    except mysql.connector.Error as error:
        st.error(f'Error al leer desde la base de datos: {error}')
        return

    if not flotaElectrica:
        return "No hay registros para esta fecha."

    # Calcular el porcentaje de participación de la flota eléctrica
    porcentaje_participacion_flota_electrica = flotaElectrica[0][-1]

    # Comparar con el KPI (por ejemplo, supongamos que el KPI es del 80%)
    kpi = 80  # Porcentaje de cumplimiento del KPI
    cumplimiento_porcentaje = (porcentaje_participacion_flota_electrica / kpi) * 100

    if cumplimiento_porcentaje >= 100:
        return f"Se cumplió el KPI al {cumplimiento_porcentaje:.2f}%."
    else:
        return f"No se cumplió el KPI. El porcentaje actual es {cumplimiento_porcentaje:.2f}%."

# Interfaz de usuario con Streamlit para la página de registro de uso de vehículos eléctricos
def registro():
    st.title('Registro de Uso de Vehículos Eléctricos')
    Fecha = st.date_input('Fecha:', value=datetime.today())
    millas_electrico_turno_1 = st.number_input('Millas Eléc. Turno 1:', value=0.0, step=0.1)
    millas_electrico_turno_2 = st.number_input('Millas Eléc. Turno 2:', value=0.0, step=0.1)
    millas_electrico_turno_3 = st.number_input('Millas Eléc. Turno 3:', value=0.0, step=0.1)
    millas_convencionales_turno_1 = st.number_input('Millas Conv. Turno 1:', value=0.0, step=0.1)
    millas_convencionales_turno_2 = st.number_input('Millas Conv. Turno 2:', value=0.0, step=0.1)
    millas_convencionales_turno_3 = st.number_input('Millas Conv. Turno 3:', value=0.0, step=0.1)

    if st.button('Registrar Uso'):
        porcentaje = usoelectrico(Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3,
                      millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3)
        st.write(f'¡Registro exitoso! Porcentaje de participación de la flota eléctrica: {porcentaje:.2f}%')

    # Mostrar los últimos 3 registros
    st.subheader('Últimos 3 Registros')
    try:
        conexion = conectar_mysql()
        cursor = conexion.cursor()
        cursor.execute(f"USE {MYSQL_DATABASE}")
        cursor.execute("SELECT * FROM uso_vehiculos_electricos ORDER BY Fecha DESC LIMIT 3")
        ultimos_registros = cursor.fetchall()
        conexion.close()
        ultimos_registros_df = pd.DataFrame(ultimos_registros, columns=['id', 'Fecha', 'Millas_Elec_T1', 'Millas_Elec_T2', 'Millas_Elec_T3', 
                                                                        'Millas_Conv_T1', 'Millas_Conv_T2', 'Millas_Conv_T3', 
                                                                        'Porcentaje_Participacion_Flota_Electrica'])
        st.write(ultimos_registros_df)
    except mysql.connector.Error as error:
        st.error(f'Error al leer desde la base de datos: {error}')

# Interfaz de usuario con Streamlit para la página de cumplimiento KPI
def cumplimiento():
    st.title('Cumplimiento del KPI de Participación de Flota Eléctrica')
    fecha_analisis = st.date_input('Fecha de Análisis:', value=datetime.today())
    resultado = cumplimientoKPI(fecha_analisis)
    st.write(f"Fecha de análisis: {fecha_analisis}")
    st.write(resultado)

# Ejecutar la aplicación
if __name__ == "__main__":
    # Aquí van las credenciales proporcionadas
    MYSQL_HOST = 'b66ffp1ohipmheztv2qe-mysql.services.clever-cloud.com'
    MYSQL_USER = 'uswedtxp1ee0rjl6'
    MYSQL_PASSWORD = 'GtRHMFbkKIcn5wFGjsSz'
    MYSQL_DATABASE = 'b66ffp1ohipmheztv2qe'

    crear_base_datos()

    st.set_page_config(layout="wide")
    tabs = ["Registro de Uso de Vehículos Eléctricos", "Cumplimiento del KPI de Participación de Flota Eléctrica"]
    choice = st.sidebar.radio("Ir a", tabs)
    if choice == tabs[0]:
        registro()
    elif choice == tabs[1]:
        cumplimiento()
