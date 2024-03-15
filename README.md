# Eco Driver NY
![](https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/banner.png)

<div>
    <div align='center'>
    <a href=".........." target="_blank" target="_blank">
          <img  src="https://github.com/karinakozlowski/Data_Siniestros_Viales/blob/main/6_Assets/BotonAPP.png"/>
       </a>
   <a href="..................">
          <img  src="https://github.com/karinakozlowski/Data_Siniestros_Viales/blob/main/6_Assets/Boton01.png"/>
      </a>
      </div>
</div>



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
La movilidad urbana sostenible es una prioridad creciente en el contexto global y en este sentido la ciudad de Nueva York no es la excepción, en los últimos años, varios líderes de esta ciudad se han unido en la iniciativa ‘OneNYC 2050′ para construir alternativas que permitan a todos los habitantes de la conocida ‘Capital del mundo’ combatir los desafíos que se aproximan, entre ellos, transformar la manera de consumir energía en la ciudad, que gradualmente se convertiría en energía 100 % renovable, para decirle adiós a los combustibles fósiles.
En este sentido, la empresa de taxis “EcoDriveNy” se encuentra en un momento crucial para su expansión y transformación. Con una visión hacia un futuro menos contaminado y una adaptación a las tendencias de mercado actuales, se propone un proceso integral de análisis y transición hacia la sostenibilidad en el transporte de pasajeros en la “ciudad que nunca duerme”.

# Objetivos del Proyecto

📊 Analizar los costos y beneficios de los vehículos eléctricos comparados con los convencionales y la viabilidad en su implementación.

🧠 Evaluar la disponibilidad y requerimientos de la infraestructura de carga para la implementación gradual de vehículos eléctricos a la flota de la empresa.

🚕 Analizar el impacto ambiental y sonoro generado por el transporte de pasajeros en la ciudad de Nueva York, calidad del aire, emisiones de CO2, y correlación con los patrones de movimiento de los vehículos.

🧠   Implementar modelos de machine learning que analicen y predigan patrones de movilidad, demanda de transporte y su relación con factores ambientales, enfocados en optimizar la operación de la flota, la eficiencia del servicio y reducir el impacto ambiental.
Proponer estrategias de marketing innovadoras y sostenibles para promover el uso de transporte de pasajeros más ecológico, campañas microsegmentadas y materiales de comunicación que resalten los beneficios ambientales del transporte sostenible.

 Desarrollar un modelo de Machine Learning para la predicción de CO2: Otro objetivo fundamental es crear un modelo de Machine Learning capaz de predecir la concentración de dióxido de carbono (CO2) en el aire de Manhattan para los próximos meses y años. Este modelo proporcionará una mejor comprensión de las tendencias de las emisiones de carbono y ayudará a tomar decisiones informadas sobre políticas ambientales y de transporte.

 
📊 Cree un panel de análisis de viajes interactivo: para brindar una visión integral de la movilidad en Manhattan, planeamos desarrollar un panel interactivo que muestre análisis detallados de los viajes en taxi, así como de empresas de transporte urbano de alto volumen como Uber y Lyft, en los 69 kilómetros de la ciudad. barrios. Este panel permitirá a la empresa explorar patrones de viaje, tendencias de demanda y otros datos relevantes, tomando decisiones basadas en datos para mejorar la movilidad urbana y reducir el impacto ambiental.


🚕 Promover la adopción de vehículos eléctricos: Uno de nuestros principales objetivos es convencer al propietario del proyecto de la efectividad de los vehículos eléctricos como solución para reducir la contaminación ambiental causada por los servicios de transporte que utilizan combustibles fósiles, como los taxis. Nuestro objetivo es presentar argumentos sólidos respaldados por datos y análisis que demuestren los beneficios económicos y ambientales de la transición a los vehículos eléctricos.


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

# Alcance del Proyecto

El proyecto abarcará desde la recopilación y depuración de datos de múltiples fuentes, incluyendo información proporcionada por la Comisión de Taxis y Limusinas de Nueva York y otros organismos relevantes, hasta la implementación y puesta en producción de modelos de machine learning. 
Se explorarán diversas métricas e indicadores relacionados con la duración de los viajes, la demanda de transporte, la calidad del aire, la contaminación sonora y otros factores relevantes.
El informe final proporcionará a la empresa una comprensión profunda de los desafíos y oportunidades relacionados con la sostenibilidad en el transporte de pasajeros en la ciudad de Nueva York. Los resultados incluirán recomendaciones concretas para la implementación de vehículos eléctricos, estrategias de marketing sostenible y la optimización de la operación de la flota. 
Además se pretende que el proyecto contribuya, más allá de las fronteras de la empresa, al avance del conocimiento en el campo de la movilidad urbana sostenible y se posicione como un referente para otras empresas del sector.


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
  


  
