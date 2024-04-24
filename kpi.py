import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import base64

# Configuración de GitHub
REPO_OWNER = "Data-Synergy"
REPO_NAME = "EcoDriverNY"
TOKEN = "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"

# Función para guardar en GitHub
def guardar_en_github(dataframe):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/data/flotaElectrica.csv"
    headers = {
        "Authorization": f"token {TOKEN}"
    }

    # Convertir DataFrame a CSV en memoria
    csv_data = dataframe.to_csv(index=False)

    # Codificar el contenido CSV en Base64
    content_base64 = base64.b64encode(csv_data.encode()).decode()

    # Crear el payload para la API de GitHub
    payload = {
        "message": "Actualizar CSV",
        "content": content_base64,
    }

    # Obtener el contenido actual del archivo
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_sha = response.json()["sha"]
        payload["sha"] = file_sha
    elif response.status_code == 404:
        # Si el archivo no existe, se creará uno nuevo
        pass
    else:
        st.error(f"Error al obtener el archivo CSV de GitHub: {response.text}")
        return

    # Hacer la solicitud PUT para actualizar o crear el archivo
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200 or response.status_code == 201:
        st.success("¡Archivo CSV actualizado en GitHub!")
    else:
        st.error(f"Error al actualizar CSV en GitHub: {response.text}")


# Función para registrar el uso de vehículos eléctricos
def usoelectrico(Fecha: datetime, millas_electrico_turno_1: float,
                  millas_electrico_turno_2: float, millas_electrico_turno_3: float,
                  millas_convencionales_turno_1: float, millas_convencionales_turno_2: float,
                  millas_convencionales_turno_3: float):

    try:
        # Intenta cargar el archivo CSV si existe
        flotaElectrica = pd.read_csv("data/flotaElectrica.csv")
    except FileNotFoundError:
        # Si el archivo no existe, crea un DataFrame vacío
        flotaElectrica = pd.DataFrame(columns=['Fecha', "Millas Eléc T1", "Millas Eléc T2", "Millas Eléc T3", "Millas Conv T1", "Millas Conv T2", "Millas Conv T3", "% Millas T1", "% Millas T2", "% Millas T3", '% Participación Flota Eléctrica'])

    if Fecha.strftime('%Y-%m-%d') in flotaElectrica["Fecha"].astype(str).values:
        st.warning("¡La fecha ya está ingresada!")
    else:
        millas_totales_electricos_dia = millas_electrico_turno_1 + millas_electrico_turno_2 + millas_electrico_turno_3
        millas_totales_convencionales_dia = millas_convencionales_turno_1 + millas_convencionales_turno_2 + millas_convencionales_turno_3
        millas_totales_turno_1 = millas_electrico_turno_1 + millas_convencionales_turno_1
        millas_totales_turno_2 = millas_electrico_turno_2 + millas_convencionales_turno_2
        millas_totales_turno_3 = millas_electrico_turno_3 + millas_convencionales_turno_3
        total_millas_dia = millas_totales_turno_1 + millas_totales_turno_2 + millas_totales_turno_3
        porcentaje_millas_electricos_turno_1 = (millas_electrico_turno_1 / millas_totales_turno_1) * 100
        porcentaje_millas_electricos_turno_2 = (millas_electrico_turno_2 / millas_totales_turno_2) * 100
        porcentaje_millas_electricos_turno_3 = (millas_electrico_turno_3 / millas_totales_turno_3) * 100
        porcentaje_millas_turno_1 = (millas_totales_turno_1 / total_millas_dia) * 100
        porcentaje_millas_turno_2 = (millas_totales_turno_2 / total_millas_dia) * 100
        porcentaje_millas_turno_3 = (millas_totales_turno_3 / total_millas_dia) * 100
        kpi_porcentaje_participacion_flota_electrica_diario = ((porcentaje_millas_electricos_turno_1 * porcentaje_millas_turno_1) + (porcentaje_millas_electricos_turno_2 * porcentaje_millas_turno_2) + (porcentaje_millas_electricos_turno_3 * porcentaje_millas_turno_3)) / 100
        datos_diarios = pd.DataFrame(columns=['Fecha', "Millas Eléc T1", "Millas Eléc T2", "Millas Eléc T3", "Millas Conv T1", "Millas Conv T2", "Millas Conv T3", "% Millas T1", "% Millas T2", "% Millas T3", '% Participación Flota Eléctrica'])
        valores = [Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3,
            millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3, porcentaje_millas_turno_1, porcentaje_millas_turno_2, porcentaje_millas_turno_3, 
            kpi_porcentaje_participacion_flota_electrica_diario]
        df_temporal = pd.DataFrame([valores], columns=datos_diarios.columns)
        flotaElectrica = pd.concat([flotaElectrica, df_temporal], ignore_index=True)

        # Guardar en CSV localmente
        flotaElectrica.to_csv("data/flotaElectrica.csv", index=False)

        # Guardar en GitHub
        guardar_en_github(flotaElectrica)

    return flotaElectrica

def cumplimientoKPI(Fecha_analisis : datetime):
    # Convertir la fecha de análisis a formato de cadena
    fecha_analisis_str = Fecha_analisis.strftime('%Y-%m-%d')

    # importamos la tabla de la función
    flotaElectrica = pd.read_csv("data/flotaElectrica.csv")
    
    if fecha_analisis_str not in flotaElectrica["Fecha"].values:
        return "Esta fecha no está registrada."
    else:
        porcentaje_actual = flotaElectrica["% Participación Flota Eléctrica"][flotaElectrica["Fecha"] == fecha_analisis_str].values[0]
        indice = flotaElectrica[flotaElectrica["Fecha"] == fecha_analisis_str].index[0]
        
        if indice == 0:
            return "No hay un porcentaje anterior registrado."
        
        porcentaje_anterior = flotaElectrica["% Participación Flota Eléctrica"][indice - 1]
        diferencia = porcentaje_actual - porcentaje_anterior
        
        if diferencia >= 0:
            return f"Se cumplió el objetivo por {diferencia.round(2)}%."
        else:
            return f"No se cumplió el objetivo por {diferencia.round(2)}%."


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
        usoelectrico(Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3,
                      millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3)
        st.success('¡Registro exitoso!')

    # Mostrar los últimos 3 registros
    st.subheader('Últimos 3 Registros')
    ultimos_registros = pd.read_csv("data/flotaElectrica.csv").tail(3)
    st.write(ultimos_registros)

    # Mostrar información sobre las fechas registradas en GitHub
    try:
        # Intenta cargar el archivo CSV desde GitHub
        url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/data/flotaElectrica.csv"
        flotaElectrica = pd.read_csv(url)
        if not flotaElectrica.empty:
            primera_fecha = flotaElectrica["Fecha"].iloc[0]
            ultima_fecha = flotaElectrica["Fecha"].iloc[-1]
            total_registros = flotaElectrica.shape[0]
            st.write(f"Primera fecha registrada: {primera_fecha}")
            st.write(f"Última fecha registrada: {ultima_fecha}")
            st.write(f"Total de registros: {total_registros}")
        else:
            st.write("No hay registros disponibles.")
    except Exception as e:
        st.write(f"Error al cargar datos desde GitHub: {e}")

# Interfaz de usuario con Streamlit para la página de cumplimiento KPI
def cumplimiento():
    st.title('Cumplimiento del KPI de Participación de Flota Eléctrica')
    fecha_analisis = st.date_input('Fecha de Análisis:', value=datetime.today())
    resultado = cumplimientoKPI(fecha_analisis)
    st.write(f"Fecha de análisis: {fecha_analisis}")
    st.write(resultado)

# Ejecutar la aplicación
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    tabs = ["Registro de Uso de Vehículos Eléctricos", "Cumplimiento del KPI de Participación de Flota Eléctrica"]
    choice = st.sidebar.radio("Ir a", tabs)
    if choice == tabs[0]:
        registro()
    elif choice == tabs[1]:
        cumplimiento()

import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import base64

# Configuración de GitHub
REPO_OWNER = "Data-Synergy"
REPO_NAME = "EcoDriverNY"
TOKEN = "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"

# Función para guardar en GitHub
def guardar_en_github(dataframe):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/data/flotaElectrica.csv"
    headers = {
        "Authorization": f"token {TOKEN}"
    }

    # Convertir DataFrame a CSV en memoria
    csv_data = dataframe.to_csv(index=False)

    # Codificar el contenido CSV en Base64
    content_base64 = base64.b64encode(csv_data.encode()).decode()

    # Crear el payload para la API de GitHub
    payload = {
        "message": "Actualizar CSV",
        "content": content_base64,
    }

    # Obtener el contenido actual del archivo
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_sha = response.json()["sha"]
        payload["sha"] = file_sha
    elif response.status_code == 404:
        # Si el archivo no existe, se creará uno nuevo
        pass
    else:
        st.error(f"Error al obtener el archivo CSV de GitHub: {response.text}")
        return

    # Hacer la solicitud PUT para actualizar o crear el archivo
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200 or response.status_code == 201:
        st.success("¡Archivo CSV actualizado en GitHub!")
    else:
        st.error(f"Error al actualizar CSV en GitHub: {response.text}")


# Función para registrar el uso de vehículos eléctricos
def usoelectrico(Fecha: datetime, millas_electrico_turno_1: float,
                  millas_electrico_turno_2: float, millas_electrico_turno_3: float,
                  millas_convencionales_turno_1: float, millas_convencionales_turno_2: float,
                  millas_convencionales_turno_3: float):

    try:
        # Intenta cargar el archivo CSV si existe
        flotaElectrica = pd.read_csv("data/flotaElectrica.csv")
    except FileNotFoundError:
        # Si el archivo no existe, crea un DataFrame vacío
        flotaElectrica = pd.DataFrame(columns=['Fecha', "Millas Eléc T1", "Millas Eléc T2", "Millas Eléc T3", "Millas Conv T1", "Millas Conv T2", "Millas Conv T3", "% Millas T1", "% Millas T2", "% Millas T3", '% Participación Flota Eléctrica'])

    if Fecha.strftime('%Y-%m-%d') in flotaElectrica["Fecha"].astype(str).values:
        st.warning("¡La fecha ya está ingresada!")
    else:
        millas_totales_electricos_dia = millas_electrico_turno_1 + millas_electrico_turno_2 + millas_electrico_turno_3
        millas_totales_convencionales_dia = millas_convencionales_turno_1 + millas_convencionales_turno_2 + millas_convencionales_turno_3
        millas_totales_turno_1 = millas_electrico_turno_1 + millas_convencionales_turno_1
        millas_totales_turno_2 = millas_electrico_turno_2 + millas_convencionales_turno_2
        millas_totales_turno_3 = millas_electrico_turno_3 + millas_convencionales_turno_3
        total_millas_dia = millas_totales_turno_1 + millas_totales_turno_2 + millas_totales_turno_3
        porcentaje_millas_electricos_turno_1 = (millas_electrico_turno_1 / millas_totales_turno_1) * 100
        porcentaje_millas_electricos_turno_2 = (millas_electrico_turno_2 / millas_totales_turno_2) * 100
        porcentaje_millas_electricos_turno_3 = (millas_electrico_turno_3 / millas_totales_turno_3) * 100
        porcentaje_millas_turno_1 = (millas_totales_turno_1 / total_millas_dia) * 100
        porcentaje_millas_turno_2 = (millas_totales_turno_2 / total_millas_dia) * 100
        porcentaje_millas_turno_3 = (millas_totales_turno_3 / total_millas_dia) * 100
        kpi_porcentaje_participacion_flota_electrica_diario = ((porcentaje_millas_electricos_turno_1 * porcentaje_millas_turno_1) + (porcentaje_millas_electricos_turno_2 * porcentaje_millas_turno_2) + (porcentaje_millas_electricos_turno_3 * porcentaje_millas_turno_3)) / 100
        datos_diarios = pd.DataFrame(columns=['Fecha', "Millas Eléc T1", "Millas Eléc T2", "Millas Eléc T3", "Millas Conv T1", "Millas Conv T2", "Millas Conv T3", "% Millas T1", "% Millas T2", "% Millas T3", '% Participación Flota Eléctrica'])
        valores = [Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3,
            millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3, porcentaje_millas_turno_1, porcentaje_millas_turno_2, porcentaje_millas_turno_3, 
            kpi_porcentaje_participacion_flota_electrica_diario]
        df_temporal = pd.DataFrame([valores], columns=datos_diarios.columns)
        flotaElectrica = pd.concat([flotaElectrica, df_temporal], ignore_index=True)

        # Guardar en CSV localmente
        flotaElectrica.to_csv("data/flotaElectrica.csv", index=False)

        # Guardar en GitHub
        guardar_en_github(flotaElectrica)

    return flotaElectrica

def cumplimientoKPI(Fecha_analisis : datetime):
    # Convertir la fecha de análisis a formato de cadena
    fecha_analisis_str = Fecha_analisis.strftime('%Y-%m-%d')

    # importamos la tabla de la función
    flotaElectrica = pd.read_csv("data/flotaElectrica.csv")
    
    if fecha_analisis_str not in flotaElectrica["Fecha"].values:
        return "Esta fecha no está registrada."
    else:
        porcentaje_actual = flotaElectrica["% Participación Flota Eléctrica"][flotaElectrica["Fecha"] == fecha_analisis_str].values[0]
        indice = flotaElectrica[flotaElectrica["Fecha"] == fecha_analisis_str].index[0]
        
        if indice == 0:
            return "No hay un porcentaje anterior registrado."
        
        porcentaje_anterior = flotaElectrica["% Participación Flota Eléctrica"][indice - 1]
        diferencia = porcentaje_actual - porcentaje_anterior
        
        if diferencia >= 0:
            return f"Se cumplió el objetivo por {diferencia.round(2)}%."
        else:
            return f"No se cumplió el objetivo por {diferencia.round(2)}%."


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
        usoelectrico(Fecha, millas_electrico_turno_1, millas_electrico_turno_2, millas_electrico_turno_3,
                      millas_convencionales_turno_1, millas_convencionales_turno_2, millas_convencionales_turno_3)
        st.success('¡Registro exitoso!')

    # Mostrar los últimos 3 registros
    st.subheader('Últimos 3 Registros')
    ultimos_registros = pd.read_csv("data/flotaElectrica.csv").tail(3)
    st.write(ultimos_registros)

    # Mostrar información sobre las fechas registradas en GitHub
    try:
        # Intenta cargar el archivo CSV desde GitHub
        url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/data/flotaElectrica.csv"
        flotaElectrica = pd.read_csv(url)
        if not flotaElectrica.empty:
            primera_fecha = flotaElectrica["Fecha"].iloc[0]
            ultima_fecha = flotaElectrica["Fecha"].iloc[-1]
            total_registros = flotaElectrica.shape[0]
            st.write(f"Primera fecha registrada: {primera_fecha}")
            st.write(f"Última fecha registrada: {ultima_fecha}")
            st.write(f"Total de registros: {total_registros}")
        else:
            st.write("No hay registros disponibles.")
    except Exception as e:
        st.write(f"Error al cargar datos desde GitHub: {e}")

# Interfaz de usuario con Streamlit para la página de cumplimiento KPI
def cumplimiento():
    st.title('Cumplimiento del KPI de Participación de Flota Eléctrica')
    fecha_analisis = st.date_input('Fecha de Análisis:', value=datetime.today())
    resultado = cumplimientoKPI(fecha_analisis)
    st.write(f"Fecha de análisis: {fecha_analisis}")
    st.write(resultado)

# Ejecutar la aplicación
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    tabs = ["Registro de Uso de Vehículos Eléctricos", "Cumplimiento del KPI de Participación de Flota Eléctrica"]
    choice = st.sidebar.radio("Ir a", tabs)
    if choice == tabs[0]:
        registro()
    elif choice == tabs[1]:
        cumplimiento()

