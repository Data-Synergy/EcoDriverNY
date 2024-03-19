![](https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/banner.png)

<div>
    <div align='center'>
    <a href=".........." target="_blank" target="_blank">
          <img  src="img/h.png"/>
       </a>
   <a href="https://drive.google.com/drive/folders/1tHkd8Ms763gyxMZmXncMByoX8jnl0LhZ">
          <img  src="img/p.png"/>
      </a>
      </div>
</div>


# Introducción
“OneNYC 2050” es una iniciativa de la ciudad de Nueva York que busca abordar los desafíos futuros mediante la transformación hacia una ciudad alimentada 100% por energías renovables, eliminando el uso de los combustibles fósiles.

En este sentido la empresa de taxis 'EcoDriveNY' se encuentra en un momento crucial para su expansión y transformación hacia la sostenbilidad, adaptandose a las tendencias del mercado y promoviendo un trnasporte de pasajeros más limpio en Nueva York.

La movilidad urbana sostenible es una prioridad creciente en el contexto global y en este sentido la ciudad de Nueva York no es la excepción, en los últimos años, varios líderes de esta ciudad se han unido en la iniciativa ‘OneNYC 2050′ para construir alternativas que permitan a todos los habitantes de la conocida ‘Capital del mundo’ combatir los desafíos que se aproximan, entre ellos, transformar la manera de consumir energía en la ciudad, que gradualmente se convertiría en energía 100 % renovable, para decirle adiós a los combustibles fósiles.

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


# Alcance del Proyecto

El proyecto abarcará desde la recopilación y depuración de datos de múltiples fuentes, incluyendo información proporcionada por la Comisión de Taxis y Limusinas de Nueva York y otros organismos relevantes, hasta la implementación y puesta en producción de modelos de machine learning. 

El informe final proporcionará a la emprea una compresión profunda de los desafios y oportunidades relacionados con la sostenibilidad en el transporte de pasajeros en la ciudad de Nueva York; Implementación gradual de vehiculos elétricos, estrategias de marketing sostenible y la optimización de la operación de la flota

Además se pretende que el proyecto contribuya, más allá de las fronteras de la empresa, al avance del conocimiento en el campo de la movilidad urbana sostenible y se posicione como un referente para otras empresas del sector.

# Metodologia de Trabajo 


![Metodologia](https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/Metodologia%20de%20Trabajo.gif)

<details>
  <summary style="cursor: s-resize; user-select: none; position: relative;"> SPRINTS #1 </summary>

  <p>
    <img src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/1.png" alt="Diagrama">
  </p>
</details>
<details>
  <summary style="cursor: s-resize; user-select: none; position: relative;"> SPRINTS #2 </summary>

  <p>
    <img src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/sprint2.png" alt="Diagrama">
  </p>
</details>
<details>
  <summary style="cursor: s-resize; user-select: none; position: relative;"> SPRINTS #3 </summary>

  <p>
    <img src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/sprint%203.png" alt="Diagrama">
  </p>
</details>


# Stack Tecnológico 

 ![Stack_Tecnologico](https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/Arquitectura_EcoDRIVE.jpg)

 
# Proceso ETL (Extraer-Tranformar-Carga)
En el contexto de nuestras operaciones de procesamiento de datos, hemos implementado un riguroso proceso ETL (Extracción, Transformación, Carga) utilizando el orquestador de flujo avanzado. Este proceso ha sido cuidadosamente diseñado para abordar las complejidades inherentes de los datos relacionados con diversos modos de transporte en la ciudad de Nueva York.

⛏️ **Extracción de Data y Limpieza y Transformación de Data****
Para obtener una fuente de datos confiable y completa, realizamos un proceso de web scraping en el sitio web oficial de la Comisión de Taxis y Limusinas de la ciudad de Nueva York. Utilizamos esta técnica para recopilar archivos Parquet que contienen datos históricos sobre viajes realizados en varios tipos de vehículos, incluidos taxis amarillos, taxis verdes, vehículos de alquiler y vehículos de alquiler de gran volumen.

Además, mejoramos nuestro conjunto de datos incorporando información histórica sobre las concentraciones de monóxido de carbono (CO) en Manhattan a través de la API OpenWeather. Este enfoque integral nos permitió enriquecer nuestra comprensión de los factores ambientales que pueden influir en los patrones de movilidad de la ciudad.


💽 **Carga en el Data Warehouse**
Una vez que los datos estuvieron limpios, estandarizados y enriquecidos, procedimos a exportarlos a nuestro Data Warehouse, específicamente a tablas de BigQuery. Este paso es crucial para permitir análisis avanzados y consultas de alto rendimiento que impulsen nuestros procesos de toma de decisiones estratégicas.


# Fuentes de Datos
Nuestro proyecto se basa en datos de diversas fuentes para realizar un análisis exhaustivo. Estas fuentes de datos son esenciales para proporcionar información sobre diferentes aspectos del transporte y el impacto ambiental en Manhattan, Nueva York.

Comisión de Taxis y Limusinas de Nueva York (TLC) : utilizamos datos históricos y actuales sobre viajes de varios tipos de servicios de transporte público en la ciudad de Nueva York. Esta fuente de datos ofrece información valiosa sobre los servicios de taxi, incluidos los taxis amarillos, los taxis verdes y más. Puede acceder a los datos en [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) .

Datos de contaminación del aire de la API de OpenWeather.org : recopilamos datos sobre la calidad del aire en función de las coordenadas de Manhattan. Esta fuente de datos nos permite monitorear los niveles de contaminación del aire y su impacto en la ciudad. Para obtener más información, visite OpenWeather.org API - [Contaminación del aire](https://openweathermap.org/api/air-pollution) 
[Enviromental and Health Dat aPortal](https://a816-dohbesp.nyc.gov/IndicatorPublic/)

Datos del proyecto sobre ruido : para comprender la contaminación acústica en Manhattan, utilizamos datos filtrados para zonas y vecindarios específicos. Estos datos nos ayudan a evaluar los niveles de ruido en diferentes áreas y sus posibles efectos. Puede acceder a los datos en [Datos del proyecto de ruido](https://noiseproject.org/data-download/)


# Equipo


<table align='center'>
  <tr>
    <td align='center'>
      <div >
        <a href="https://github.com/Karrion1987" target="_blank" rel="author">
          <img width="110" src="https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/Group%2033.png"/>
        </a>
        <a href="https://github.com/Karrion1987" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Allan Alvarez</br><small>Data Scientist</small></h4>
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
          <img width="110" src="https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/Group%2037.png"/>
        </a>
        <a href="https://github.com/karinakozlowski" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Karina Kozlowski</br><small>Data Science</small></h4>
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
          <img width="110" src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/Group%2036.png"/>
        </a>
        <a href="https://github.com/EliasIchi" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Elias Almada</br><small>Data Analyst</small></h4>
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
          <img width="110" src="https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/Group%2038.png"/>
        </a>
        <a href="https://github.com/dunietmg" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Duniet Marrero Garcia</br><small> Data Engineer</small></h4>
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
          <img width="110" src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/Group%2034.png"/>
        </a>
        <a href="https://github.com/paulusbrizzi" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Pablo Brizzi</br><small>Data Engineer.</small></h4>
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
          <img width="110" src="https://github.com/Data-Synergy/EcoDriverNY/blob/main/img/Group%2035.png"/>
        </a>
        <a href="https://github.com/TRAZE42" target="_blank" rel="author">
          <h4 style="margin-top: 1rem;">Paul Jauregui</br><small>Data Analyst</small></h4>
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
  


  
