import numpy as np
import pandas as pd
from google.colab import drive

#Se accede al drive y se crean las rutas de acceso
drive.mount('/content/drive')
interb="/content/drive/MyDrive/interb.xlsx"
mayor="/content/drive/MyDrive/mayor.xlsx"

#Lectura de los archivos y creación de los diferentes dataframes
extracto_df = pd.read_excel(interb)
mayor_df = pd.read_excel(mayor)
cruza_df_mayor_extracto = pd.DataFrame(columns=['Fecha', 'Importe'])
no_coinciden_df_mayor_extracto = pd.DataFrame(columns=['Fecha', 'Importe'])
cruza_df_extract_mayor = pd.DataFrame(columns=['Fecha', 'Importe'])
no_coinciden_df_extract_mayor = pd.DataFrame(columns=['Fecha', 'Importe'])

# Obtener el número total de filas en mayor_df
total_filas = len(mayor_df)

# Contador de filas recorridas
filas_recorridas = 0


# Recorrer fila por fila de mayor_df
for index_mayor, row_mayor in mayor_df.iterrows():
    # Verificar si no quedan más filas sin recorrer en mayor_df
    if filas_recorridas >= total_filas:
        break

    # Variable de control para verificar si se encontraron coincidencias
    coincidencia_encontrada = False

    # Recorrer fila por fila de extracto_df
    for index_extracto, row_extracto in extracto_df.iterrows():
        # Comparar columnas
        if (row_mayor['Fecha'] == row_extracto['Fecha']) and (row_mayor['Importe'] == row_extracto['Importe']):
            # Agregar filas a cruza_df
            cruza_df_mayor_extracto = cruza_df_mayor_extracto.append(row_mayor)
            cruza_df_mayor_extracto = cruza_df_mayor_extracto.append(row_extracto)

            # Eliminar filas de mayor_df y extracto_df
            mayor_df = mayor_df.drop(index_mayor)
            extracto_df = extracto_df.drop(index_extracto)

            # Cambiar el estado de la variable de control
            coincidencia_encontrada = True
            break

    # Verificar si se encontraron coincidencias
    if not coincidencia_encontrada:
        # Agregar filas a no_coinciden_df
        no_coinciden_df_mayor_extracto = no_coinciden_df_mayor_extracto.append(row_mayor)

    # Incrementar el contador de filas recorridas
    filas_recorridas += 1






# Obtener el número total de filas en extracto_df
total_filas = len(extracto_df)

# Contador de filas recorridas
filas_recorridas = 0

# Recorrer fila por fila de extracto_df
for index_extracto, row_extracto in extracto_df.iterrows():
    # Verificar si no quedan más filas sin recorrer en extracto_df
    if filas_recorridas >= total_filas:
        break

    # Variable de control para verificar si se encontraron coincidencias
    coincidencia_encontrada = False

    # Recorrer fila por fila de mayor_df
    for index_mayor, row_mayor in mayor_df.iterrows():
        # Comparar columnas
        if (row_extracto['Fecha'] == row_mayor['Fecha']) and (row_extracto['Importe'] == row_mayor['Importe']):
            # Agregar filas a cruza_df
            cruza_df_extract_mayor = cruza_df_extract_mayor.append(row_extracto)
            cruza_df_extract_mayor = cruza_df_extract_mayor.append(row_mayor)

            # Eliminar filas de extracto_df y mayor_df
            extracto_df = extracto_df.drop(index_extracto)
            mayor_df = mayor_df.drop(index_mayor)

            # Cambiar el estado de la variable de control
            coincidencia_encontrada = True
            break

    # Verificar si se encontraron coincidencias
    if not coincidencia_encontrada:
        # Agregar filas a no_coinciden_df
        no_coinciden_df_extract_mayor = no_coinciden_df_extract_mayor.append(row_extracto)

    # Incrementar el contador de filas recorridas
    filas_recorridas += 1

#Resultado del cruzamiento:
resultado_cruza_sobrantes = pd.concat([no_coinciden_df_mayor_extracto, no_coinciden_df_extract_mayor], axis=0)
resultado_cruza_sobrantes


#Exportar a excel
resultado_cruza_sobrantes.to_excel('resultado_cruza_sobrantes.xlsx', index=False)