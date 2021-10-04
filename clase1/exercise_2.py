# California Housing
# - Analísis de información estructurada
# - Librerías
# Importar el archivo california_housing_train.xlsx.
#! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/california_housing_train.xlsx"

# Este archivo contiene un conjunto de datos de viviendas de California, el cual fue extraido del censo de nacional de 1990. 
# Para mas info sobre el set de datos: https://developers.google.com/machine-learning/crash-course/california-housing-data-description

# Extraer la siguiente información:
#	1. ¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
#	2. ¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas? Rta: 2466.31
#	3. ¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814

# ★★ 4. Obtener la media y la varianza de la propiedad 'median_house_value'. Rta: 207300.91 - 13451442293.57
#	Tip: ¡Pueden investigar funciones de numpy para conseguir la media y la varianza! numpy.var

import pandas as pd
import numpy as np

def question1(dataframe):
	print('¿Cuantas casas hay con valor \'median_house_value\' mayor a 80000 tomando de la longitud -120 a -118?')
	filtered_df = dataframe[(dataframe['median_house_value'] > 80000) & (dataframe['longitude'] >= -120) & (dataframe['longitude'] <= -118)]
	amount = len(filtered_df)
	print(amount)
	return filtered_df

def question2(dataframe):
	print('¿Cual es el promedio de habitaciones por manzana (\'total_rooms\') de estas casas?')
	average = sum(dataframe['total_rooms']) / len(dataframe)
	print(round(average,2))

def question3(dataframe):
	print('¿Cual es la casa más cara? ¿Cuántas hay con este valor?')
	max_value = dataframe['median_house_value'].max()
	print(max_value)
	print(len(dataframe[ dataframe['median_house_value'] == max_value ]))

def question4(dataframe):
	print('Obtener la media y la varianza de la propiedad \'median_house_value\'.')
	mean = np.mean(dataframe['median_house_value'])
	variance = np.var(dataframe['median_house_value'])
	print(round(mean,2))
	print(round(variance,2))

df = pd.read_excel('california_housing_train.xlsx')
filtered_df = question1(df)
question2(filtered_df)
question3(df)
question4(df)