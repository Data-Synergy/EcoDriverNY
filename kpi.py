import streamlit as st
import pandas as pd
from datetime import datetime

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
        flotaElectrica.to_csv("data/flotaElectrica.csv", index=False)

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

# Interfaz de usuario con Streamlit para la página de cumplimiento KPI
def cumplimiento():
    st.title('Cumplimiento del KPI de Participación de Flota Eléctrica')
    fecha_analisis = st.date_input('Fecha de Análisis:', value=datetime.today())
    resultado = cumplimientoKPI(fecha_analisis)
    st.write(f"Fecha de análisis: {fecha_analisis}")
    st.write(resultado)

# Ejecutar la aplicación
if _name_ == "_main_":
    st.set_page_config(layout="wide")
    tabs = ["Registro de Uso de Vehículos Eléctricos", "Cumplimiento del KPI de Participación de Flota Eléctrica"]
    choice = st.sidebar.radio("Ir a", tabs)
    if choice == tabs[0]:
        registro()
    elif choice == tabs[1]:
        cumplimiento()
