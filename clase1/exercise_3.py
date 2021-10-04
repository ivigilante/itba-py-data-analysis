# Llévame en tu bicicleta
# - Analisís de información estructurada
# - Librerías
# El gobierno de la Ciudad de Buenos Aires recolecta datos acerca del uso de los servicios de bicicletas públicas (ecobici) y publica parte de ellos: https://data.buenosaires.gob.ar/dataset/bicicletas-publicas

# Para este ejemplo usaremos los primeros 10000 viajes de la base de datos del 2021. 
# Están invitados a analizar todos los viajes, pero para ello les recomendamos descargar el archivo y 
# ejecutar su programa en forma local (no en Google Golab).

# Se quiere conocer más acerca del uso que le dan los usuarios al sistema, por lo cual su tarea será extraer la siguiente información:

# 1. ¿Qué porcentaje de los viajes se completaron en estado NORMAL?
# 2. ¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)
# 3. ¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
# 4. ¿Cuántas estaciones diferentes fueron utilizadas?
# 5. Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
# 	Tip: Recuerden investigar los métodos que tienen los DataFrames para ver si alguno de ellos les ayuda a resolver un problema particular.

# ! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/recorridos-realizados-2021-sample.csv"
