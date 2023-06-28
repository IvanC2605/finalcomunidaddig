
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title('Titulo del Proyecto')

data = pd.read_excel('fallecidos_covid.xlsx', sheet_name='Worksheet')
print(data.head())
st.header('Datos de fallecidos por COVID-19')
st.dataframe(data)



# Obtener la lista única de ciudades
ciudades = np.sort(data['DEPARTAMENTO'].unique())
# Agregar una opción en el sidebar para seleccionar una ciudad
ciudad_seleccionada = st.sidebar.selectbox('Selecciona una ciudad', ciudades)

# Filtrar los datos por la ciudad seleccionada
datos_filtrados = data[data['DEPARTAMENTO'] == ciudad_seleccionada]

# Mostrar los datos filtrados en una tabla
st.header('Datos filtrados por ciudad')
st.dataframe(datos_filtrados)

def buscar_por_uuid(uuid):
    # Leer el archivo CSV o Excel y almacenar los datos en un DataFrame
   

    # Filtrar los datos por número UUID
    datos_filtrados = data[data['UUID'] == uuid]

    return datos_filtrados

# Interfaz del dashboard
def main():
    # Título y descripción del dashboard
    st.title('Búsqueda por UUID')
    st.write('Ingrese el número UUID para buscar en la base de datos')

    # Obtener el número UUID ingresado por el usuario
    uuid_buscado = st.number_input('Número UUID')

    # Realizar la búsqueda cuando se presione el botón "Buscar"
    if st.button('Buscar'):
        resultados = buscar_por_uuid(uuid_buscado)

        # Mostrar los resultados en una tabla
        st.header('Resultados de la búsqueda')
        if len(resultados) > 0:
            st.dataframe(resultados)
        else:
            st.write('No se encontraron resultados para el número UUID ingresado')

# Ejecutar el dashboard
if __name__ == '__main__':
    main()


def grafico_fallecidos_por_departamento():
    # Calcular la cantidad de fallecidos por departamento
    fallecidos_por_departamento = data['DEPARTAMENTO'].value_counts()

    # Crear el gráfico de barras con Plotly
    fig = px.bar(x=fallecidos_por_departamento.index, y=fallecidos_por_departamento.values,
                 labels={'x': 'Departamento', 'y': 'Cantidad de fallecidos'},
                 title='Cantidad de fallecidos por departamento')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

# Interfaz del dashboard
def main():
    # Título y descripción del dashboard
    st.title('Análisis de fallecidos por departamento')

    # Mostrar el gráfico cuando se presione el botón "Mostrar gráfico"
    if st.button('Mostrar gráfico'):
        grafico_fallecidos_por_departamento()

# Ejecutar el dashboard
if __name__ == '__main__':
    main()



def grafico_provincias_mas_victimas():
       # Calcular la cantidad de víctimas por provincia
    victimas_por_provincia = data['PROVINCIA'].value_counts()

    # Crear el gráfico circular con Plotly
    fig = px.pie(victimas_por_provincia, values=victimas_por_provincia.values,
                 names=victimas_por_provincia.index, title='Provincias con más víctimas de COVID')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

# Interfaz del dashboard
def main():
    # Título y descripción del dashboard
    st.title('Análisis de víctimas de COVID por provincia')

    # Mostrar el gráfico cuando se presione el botón "Mostrar gráfico"
    if st.button('Mostrar gráfico ' + str(id('Mostrar gráfico'))):
        grafico_provincias_mas_victimas()

# Ejecutar el dashboard
if __name__ == '__main__':
    main()
