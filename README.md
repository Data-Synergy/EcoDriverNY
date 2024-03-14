# Eco Driver NY




# Indice
- [Introducción](#introducción)
- [Objetivos](#Objetivos)
- [Stack Tecnológico](#Stack-Tecnológico)
- [Proceso ETL (Extraer-Tranformar-Carga)](https://github.com/Data-Synergy/EcoDriverNY/blob/main/README.md#proceso-etl-extraer-tranformar-carga))
- [Diagrama Gantt](#gantt-diagram)
- [Performance de Indicadores Claves (KPIs)](#Performance-de-Indicadores-Claves-(KPIs))
- [Modelo Machine Learning](https://github.com/Data-Synergy/EcoDriverNY/blob/main/README.md#modelo-machine-learning)
- [API](#api)
- [Fuentes de Datos](#Fuentes-de-Datos)
- [Equipo](#Equipo)


# Introducción

# Objetivos

🚕 Promover la adopción de vehículos eléctricos: Uno de nuestros principales objetivos es convencer al propietario del proyecto de la efectividad de los vehículos eléctricos como solución para reducir la contaminación ambiental causada por los servicios de transporte que utilizan combustibles fósiles, como los taxis. Nuestro objetivo es presentar argumentos sólidos respaldados por datos y análisis que demuestren los beneficios económicos y ambientales de la transición a los vehículos eléctricos.

🧠 Desarrollar un modelo de Machine Learning para la predicción de CO2: Otro objetivo fundamental es crear un modelo de Machine Learning capaz de predecir la concentración de dióxido de carbono (CO2) en el aire de Manhattan para los próximos meses y años. Este modelo proporcionará una mejor comprensión de las tendencias de las emisiones de carbono y ayudará a tomar decisiones informadas sobre políticas ambientales y de transporte.

📊 Cree un panel de análisis de viajes interactivo: para brindar una visión integral de la movilidad en Manhattan, planeamos desarrollar un panel interactivo que muestre análisis detallados de los viajes en taxi, así como de empresas de transporte urbano de alto volumen como Uber y Lyft, en los 69 kilómetros de la ciudad. barrios. Este panel permitirá a la empresa explorar patrones de viaje, tendencias de demanda y otros datos relevantes, tomando decisiones basadas en datos para mejorar la movilidad urbana y reducir el impacto ambiental.

# Stack Tecnológico 

# Proceso ETL (Extraer-Tranformar-Carga)
En el contexto de nuestras operaciones de procesamiento de datos, hemos implementado un riguroso proceso ETL (Extracción, Transformación, Carga) utilizando el orquestador de flujo avanzado, Mage.ai, el reemplazo actual de Apache Airflow. Este proceso ha sido cuidadosamente diseñado para abordar las complejidades inherentes de los datos relacionados con diversos modos de transporte en la ciudad de Nueva York.

⛏️ **Extracción de Data**
Para obtener una fuente de datos confiable y completa, realizamos un proceso de web scraping en el sitio web oficial de la Comisión de Taxis y Limusinas de la ciudad de Nueva York. Utilizamos esta técnica para recopilar archivos Parquet que contienen datos históricos sobre viajes realizados en varios tipos de vehículos, incluidos taxis amarillos, taxis verdes, vehículos de alquiler y vehículos de alquiler de gran volumen.

Además, mejoramos nuestro conjunto de datos incorporando información histórica sobre las concentraciones de monóxido de carbono (CO) en Manhattan a través de la API OpenWeather. Este enfoque integral nos permitió enriquecer nuestra comprensión de los factores ambientales que pueden influir en los patrones de movilidad de la ciudad.

🧹 **Limpieza y Transformación de Data**

💽 **Carga en el Data Warehouse**
Una vez que los datos estuvieron limpios, estandarizados y enriquecidos, procedimos a exportarlos a nuestro Data Warehouse, específicamente a tablas de BigQuery. Este paso es crucial para permitir análisis avanzados y consultas de alto rendimiento que impulsen nuestros procesos de toma de decisiones estratégicas.

# Fuentes de Datos
Nuestro proyecto se basa en datos de diversas fuentes para realizar un análisis exhaustivo. Estas fuentes de datos son esenciales para proporcionar información sobre diferentes aspectos del transporte y el impacto ambiental en Manhattan, Nueva York.

Comisión de Taxis y Limusinas de Nueva York (TLC) : utilizamos datos históricos y actuales sobre viajes de varios tipos de servicios de transporte público en la ciudad de Nueva York. Esta fuente de datos ofrece información valiosa sobre los servicios de taxi, incluidos los taxis amarillos, los taxis verdes y más. Puede acceder a los datos en [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) .

Datos de contaminación del aire de la API de OpenWeather.org : recopilamos datos sobre la calidad del aire en función de las coordenadas de Manhattan. Esta fuente de datos nos permite monitorear los niveles de contaminación del aire y su impacto en la ciudad. Para obtener más información, visite OpenWeather.org API - [Contaminación del aire](https://openweathermap.org/api/air-pollution) 
[Enviromental and Health Dat aPortal](https://a816-dohbesp.nyc.gov/IndicatorPublic/)

Datos del proyecto sobre ruido : para comprender la contaminación acústica en Manhattan, utilizamos datos filtrados para zonas y vecindarios específicos. Estos datos nos ayudan a evaluar los niveles de ruido en diferentes áreas y sus posibles efectos. Puede acceder a los datos en [Datos del proyecto de ruido](https://noiseproject.org/data-download/)

# Diagrama Gantt

# Performance de Indicadores Claves (KPIs)

# Modelo Machine Learning 

# API

# Equipo


<table align='center'>
  <tr>
    <td align='center'>
      <div >
        <a href="https://github.com/Karrion1987" target="_blank" rel="author">
          <img width="110" src="https://avatars.githubusercontent.com/u/138166529?v=4"/>
        </a>
        <a href="https://github.com/Karrion1987" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Allan Alvarez</br><small>............</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/Karrion1987" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/allan-alvarez-gonzalez-6783a2256/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>
    </td>
    <td align='center'>
      <div >
        <a href="https://github.com/karinakozlowski" target="_blank" rel="author">
          <img width="110" src="https://raw.githubusercontent.com/karinakozlowski/imagenes/main/No%20country2.jpg"/>
        </a>
        <a href="https://github.com/karinakozlowski" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Karina Kozlowski</br><small>Data Engineer</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/karinakozlowski" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/karina-kozlowski-625535217/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>
    </td>
    <td align='center'>
      <div >
        <a href="https://github.com/EliasIchi" target="_blank" rel="author">
          <img width="110" src="https://avatars.githubusercontent.com/u/124707045?v=4"/>
        </a>
        <a href="https://github.com/EliasIchi" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Elias Almada</br><small>.............</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/EliasIchi" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/elias-almada-795a54158/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>
    </td>
  </tr>
  </table>
  <table align='center'>
<tr>
<td align='center'>
      <div >
        <a href="https://github.com/dunietmg" target="_blank" rel="author">
          <img width="110" src="https://avatars.githubusercontent.com/u/138503506?v=4"/>
        </a>
        <a href="https://github.com/dunietmg" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Duniet Marrero Garcia</br><small>............</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/dunietmg" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/duniet-marrero-garcia/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>
    </td>
<td align='center'>
      <div >
        <a href="https://github.com/paulusbrizzi" target="_blank" rel="author">
          <img width="110" src="https://media.licdn.com/dms/image/D4D03AQGx5U99T09Hzw/profile-displayphoto-shrink_400_400/0/1698425666147?e=1715817600&v=beta&t=a1b7NyKoTMcZH6I4fMaTzSm8HlZd0TdWS9wDfOV5-qs"/>
        </a>
        <a href="https://github.com/paulusbrizzi" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Pablo Brizzi</br><small>...........</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/paulusbrizzi" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/pablojbrizzi/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>

  <td align='center'>
      <div >
        <a href="https://github.com/TRAZE42" target="_blank" rel="author">
          <img width="110" src="https://media.licdn.com/dms/image/D4E03AQEQweg5Ecvn9A/profile-displayphoto-shrink_800_800/0/1693008264319?e=1715817600&v=beta&t=rvqNVGo-C3rT5WYvMeFVaRu1Yqtq05RcQB-CkcNQk-I"/>
        </a>
        <a href="https://github.com/TRAZE42" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Paul Jauregui</br><small>...........</small></h4>
        </a>
        <div style='display: flex; flex-direction: column'>
        <a href="https://github.com/TRAZE42" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=172B4D&logo=GitHub&logoColor=FFFFFF&label="/>
        </a>
        <a href="https://www.linkedin.com/in/paul-andr%C3%A9-/" target="_blank">
          <img style='width:8rem' src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
        </a>
        </div>
      </div>
    </td>
  


  
