# Copy
# Uso de librerรญas
# Manejo de archivos
# Armar una funciรณn que copie un archivo .xlsx, y lo guarde como "Copia 1 -  ๐๐๐๐๐๐ ", de ya existir debe guardarlo como Copia 2 -, Copia 3 - , ...

# Usar la libreria os para chequear si existe el archivo:

# Tips:
# os.path.exists( ๐๐๐๐๐๐ ) devolverรก True si ya existe
# Se puede importar con: import os

# Asumo que hay que usar pandas y read_excel - to_excel para practicar

import pandas as pd
import os

def copyExcelFile(filename):
    n_copy = 1
    df = pd.read_excel(filename)
    dst_filename = f'Copia {n_copy} - ' + filename
    while os.path.exists(dst_filename):
        n_copy += 1
        dst_filename = f'Copia {n_copy} - ' + filename
    df.to_excel(dst_filename)
    return dst_filename

filename = 'Datos.xlsx'
print(f'Copying {filename}...')
dst_filename = copyExcelFile(filename)
print('Copy finished: ', dst_filename)
