import streamlit as st
import snowflake.connector
import pandas as pd
from datetime import datetime

snowflake_credentials = {
    'user': 'ELIASALMADA1234',
    'password': 'Ichi2017',
    'account': 'pzbgdyt-aib83585',
    'warehouse': 'COMPUTE_WH',
    'database': 'SCHEMA_TAXIS_NYC_ECODRIVE',
    'schema': 'PUBLIC'
}

# Establecer la conexión a Snowflake al inicio de la aplicación
conexion = snowflake.connector.connect(**snowflake_credentials)

def ejecutar_consulta(sql_query):
    try:
        cursor = conexion.cursor()
        cursor.execute(sql_query)
        registros = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(registros, columns=columnas)
        return df
    except snowflake.connector.errors.DatabaseError as e:
        st.error(f"Error al ejecutar consulta: {e}")
        return None
    finally:
        cursor.close()

def subir_datos_a_base_de_datos(conn, fecha, millas_electrico_turno_1, millas_electrico_turno_2,
                                millas_electrico_turno_3, millas_convencionales_turno_1,
                                millas_convencionales_turno_2, millas_convencionales_turno_3):
    try:
        cursor = conn.cursor()
        
        cursor.execute(f"""INSERT INTO SCHEMA_TAXIS_NYC_ECODRIVE.PUBLIC.USO_VEHICULOS_ELECTRICOS (Fecha, Millas_Elec_T1, Millas_Elec_T2, Millas_Elec_T3, 
                            Millas_Conv_T1, Millas_Conv_T2, Millas_Conv_T3) 
                            VALUES ('{fecha}', {millas_electrico_turno_1}, {millas_electrico_turno_2}, 
                            {millas_electrico_turno_3}, {millas_convencionales_turno_1}, 
                            {millas_convencionales_turno_2}, {millas_convencionales_turno_3})""")
        
        conn.commit()
        st.success("Datos insertados correctamente en base de datos.")

    except snowflake.connector.errors.DatabaseError as e:
        st.error(f"Error al insertar datos en base de datos: {e}")

    finally:
        # Cerrar el cursor
        cursor.close()

def mostrar_interfaz():
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')

    # Mostrar el campo de fecha con la fecha actual pero no editable
    st.write("Fecha:", fecha_actual)

    # Ingresar las millas con un valor mínimo de 0
    millas_electrico_turno_1 = st.number_input("Millas Eléc. Turno 1", value=0.0, min_value=0.0)
    millas_electrico_turno_2 = st.number_input("Millas Eléc. Turno 2", value=0.0, min_value=0.0)
    millas_electrico_turno_3 = st.number_input("Millas Eléc. Turno 3", value=0.0, min_value=0.0)
    millas_convencionales_turno_1 = st.number_input("Millas Conv. Turno 1", value=0.0, min_value=0.0)
    millas_convencionales_turno_2 = st.number_input("Millas Conv. Turno 2", value=0.0, min_value=0.0)
    millas_convencionales_turno_3 = st.number_input("Millas Conv. Turno 3", value=0.0, min_value=0.0)

    if st.button("Registrar Uso"):
        # Verificar que los valores sean mayores que 0
        if (millas_electrico_turno_1 > 0 and millas_electrico_turno_2 > 0 and millas_electrico_turno_3 > 0 and
            millas_convencionales_turno_1 > 0 and millas_convencionales_turno_2 > 0 and millas_convencionales_turno_3 > 0):
            subir_datos_a_base_de_datos(conexion, fecha_actual, millas_electrico_turno_1, millas_electrico_turno_2,
                                        millas_electrico_turno_3, millas_convencionales_turno_1,
                                        millas_convencionales_turno_2, millas_convencionales_turno_3)
        else:
            st.warning("Los valores deben ser mayores que 0.")

    if st.button("Mostrar resultados"):
        sql_query = """
        SELECT
    FECHA,
    SUM(MILLAS_ELEC_T1) AS SUMA_MILLAS_ELEC_T1,
    SUM(MILLAS_ELEC_T2) AS SUMA_MILLAS_ELEC_T2,
    SUM(MILLAS_ELEC_T3) AS SUMA_MILLAS_ELEC_T3,
    SUM(MILLAS_CONV_T1) AS SUMA_MILLAS_CONV_T1,
    SUM(MILLAS_CONV_T2) AS SUMA_MILLAS_CONV_T2,
    SUM(MILLAS_CONV_T3) AS SUMA_MILLAS_CONV_T3,
    CONCAT(ROUND((SUM(MILLAS_TOTAL) / SUM(MILLAS_ANTERIOR)) * 100, 2), '%') AS PORCENTAJE_PARTICIPACION_FLOTA_ELECTRICA
FROM
    (
    SELECT *,
    (MILLAS_ELEC_T1 +
    MILLAS_ELEC_T2 +
    MILLAS_ELEC_T3 +
    MILLAS_CONV_T1 +
    MILLAS_CONV_T2 +
    MILLAS_CONV_T3) AS MILLAS_TOTAL,
    LAG(MILLAS_TOTAL, 1) OVER (ORDER BY id ASC) AS MILLAS_ANTERIOR
    FROM SCHEMA_TAXIS_NYC_ECODRIVE.PUBLIC.USO_VEHICULOS_ELECTRICOS
    ) AS A
GROUP BY FECHA;
        """
        resultados = ejecutar_consulta(sql_query)
        if resultados is not None:
            st.write(resultados)
            st.success("Consulta ejecutada correctamente.")


# Crear la interfaz gráfica con Streamlit
st.title("Análisis de Uso de Vehículos Eléctricos")
mostrar_interfaz()
