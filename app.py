import pandas as pd
import streamlit as st
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Carga del conjunto de datos
df_electric_tnCO2 = pd.read_csv("data/electric_tnCO2_100mi.csv")

# Dividir la columna y asignar nombres a las nuevas columnas
df_split = df_electric_tnCO2['Category;Model;Model Year;Manufacturer;Fuel;↑ All-Electric Range;Alternative Fuel Economy City;Alternative Fuel Economy Highway;Alternative Fuel Economy Combined;Engine Type;Engine Size;tnco2/100mi;price'].str.split(';', expand=True)
df_split.columns = ['Category', 'Model', 'Model Year', 'Manufacturer', 'Fuel', '↑ All-Electric Range', 
                    'Alternative Fuel Economy City', 'Alternative Fuel Economy Highway', 
                    'Alternative Fuel Economy Combined', 'Engine Type', 'Engine Size', 'tnco2/100mi', 'price']
df_electric_tnCO2 = pd.concat([df_electric_tnCO2, df_split], axis=1)
df_electric_tnCO2.drop(columns=['Category;Model;Model Year;Manufacturer;Fuel;↑ All-Electric Range;Alternative Fuel Economy City;Alternative Fuel Economy Highway;Alternative Fuel Economy Combined;Engine Type;Engine Size;tnco2/100mi;price'], inplace=True)

# Selección de columnas relevantes para el modelo de recomendación
relevant_columns = ['Model', 'Category', 'Manufacturer', '↑ All-Electric Range', 
                    'Alternative Fuel Economy City', 'Alternative Fuel Economy Highway', 
                    'Alternative Fuel Economy Combined', 'Engine Type', 'Engine Size', 'tnco2/100mi']

# Preprocesamiento de datos (si es necesario)
# ...

# Entrenamiento del modelo de recomendación
tfidf = TfidfVectorizer(stop_words='english')
model_desc = tfidf.fit_transform(df_electric_tnCO2[relevant_columns].astype(str).apply(' '.join, axis=1))  # Convertir cada fila en una cadena
similarity_matrix = cosine_similarity(model_desc, model_desc)

# Streamlit app
st.title("VRS (Vehicule Recommendation System)")

# Imagen de la pantalla de inicio
st.image("https://raw.githubusercontent.com/Data-Synergy/EcoDriverNY/main/img/banner.png", use_column_width=True)

# Añadir secciones al panel izquierdo
st.sidebar.title("Navegación")

option = st.sidebar.selectbox(
    'Seleccione una opción',
    ('VRS (Vehicule Recommendation System)', 'Distribution', 'Resume')
)

# Sección de VRS (Vehicule Recommendation System)
if option == 'VRS (Vehicule Recommendation System)':
    st.header("Bienvenido")
    st.write("Este es un sistema que te ayuda a encontrar vehículos eléctricos similares al que deseas comprar para la flota, basado en sus características técnicas.")
    st.write("Por favor, selecciona el fabricante, modelo y categoría del vehículo que deseas comprar para recibir recomendaciones.")

    # Interfaz de usuario
    # Obtener valores únicos de las columnas 'Manufacturer' y 'Model'
    fabricantes_unicos = df_electric_tnCO2['Manufacturer'].unique()
    categorias_unicas = df_electric_tnCO2['Category'].unique()

    # Input para el fabricante, modelo y categoría
    fabricante_input = st.selectbox("Seleccione el fabricante de su vehículo:", fabricantes_unicos)
    categoria_input = st.selectbox("Seleccione la categoría de su vehículo:", categorias_unicas)

    if fabricante_input:
        modelos_fabricante = df_electric_tnCO2[(df_electric_tnCO2['Manufacturer'] == fabricante_input) & (df_electric_tnCO2['Category'] == categoria_input)]['Model'].unique()
        modelo_input = st.selectbox("Seleccione el modelo de su vehículo:", modelos_fabricante)

        if st.button("Obtener Recomendaciones"):
            if modelo_input:
                # Filtrar el DataFrame para obtener todas las filas que coincidan con el fabricante seleccionado y la categoría seleccionada
                filtered_df = df_electric_tnCO2[(df_electric_tnCO2['Manufacturer'] == fabricante_input) & (df_electric_tnCO2['Category'] == categoria_input)]
                
                if not filtered_df.empty:
                    # Encuentra el índice del modelo ingresado
                    idx = filtered_df[filtered_df['Model'] == modelo_input].index[0]
                    
                    # Calcula la similitud coseno entre el modelo ingresado y todos los demás modelos
                    sim_scores = list(enumerate(similarity_matrix[idx]))
                    
                    # Ordena los modelos según su similitud
                    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                    
                    # Obtiene los índices de los modelos recomendados
                    recommended_indices = [i[0] for i in sim_scores][:5]
                    
                    # Obtiene los fabricantes y modelos de los modelos recomendados, eliminando duplicados
                    recommended_vehicles = df_electric_tnCO2.iloc[recommended_indices][['Model', 'Manufacturer']].drop_duplicates()
                    
                    # Imprime los fabricantes y modelos recomendados
                    st.write("Vehículos recomendados de otros fabricantes:")
                    st.write(recommended_vehicles.drop_duplicates())
                else:
                    st.write("No se encontraron resultados para el fabricante y categoría seleccionados.")
            else:
                st.write("Por favor seleccione un modelo.")  

# Sección de Distribución
elif option == 'Distribution':
    st.header("Distribución de Datos")

      # Gráfico de barras para la distribución de fabricantes
    st.subheader("Distribución de Fabricantes")
    fabricante_counts = df_electric_tnCO2['Manufacturer'].value_counts()
    
    # Paleta de colores personalizada basada en el volumen
    custom_palette = sns.color_palette("crest", len(fabricante_counts))
    sns.set_palette(custom_palette)
    
    st.bar_chart(fabricante_counts)
    # Otros gráficos de distribución
    # Puedes agregar más gráficos de barras o cualquier otro tipo de gráfico aquí

# Sección de Resumen
elif option == 'Resume':
    st.header("Resumen")

    st.write("El proyecto EcoDriveNY se presenta como una iniciativa integral para la transición de la flota de taxis en la ciudad de Manhattan hacia vehículos eléctricos. Basado en una serie de aspectos clave, el proyecto demuestra ser tanto rentable como viable, ofreciendo una serie de beneficios que van más allá de la simple reducción de emisiones de carbono:")
    st.markdown("""
    1. **Marco legislativo sólido:** La legislación de Nueva York que exige el cambio hacia vehículos eléctricos para taxis antes del 2035 proporciona un marco regulatorio sólido y un fuerte impulso político para el proyecto.
    2. **Eficiencia operativa:** Los vehículos eléctricos ofrecen una autonomía adecuada que permite operar durante dos turnos de 8 horas sin necesidad de recargar, lo que maximiza el tiempo de servicio del vehículo y reduce los tiempos de inactividad.
    3. **Reducción de costos operativos:** Con costos operativos significativamente menores y menos mantenimiento requerido en comparación con los vehículos de combustión interna, los taxis eléctricos ofrecen ahorros significativos en combustible y mantenimiento a lo largo de su vida útil.
    4. **Beneficios medioambientales:** La transición hacia vehículos eléctricos contribuye a la reducción de las emisiones de gases de efecto invernadero y mejora la calidad del aire en la ciudad, posicionando a Manhattan como un líder en sostenibilidad y acción climática.
    5. **Infraestructura de carga:** La implementación de una infraestructura de carga eléctrica robusta y accesible es fundamental para el éxito del proyecto, con la instalación de estaciones de carga rápida y ultrarrápida en lugares estratégicos en toda la ciudad.
    6. **Apoyo gubernamental y financiero:** El gobierno y otras entidades pueden proporcionar una serie de incentivos financieros, subsidios y programas de financiamiento para facilitar la transición hacia vehículos eléctricos, incluyendo créditos fiscales, subvenciones y financiamiento preferencial para la instalación de infraestructura de carga.
    """)
