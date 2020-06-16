from bitcoin import LecturaInputs
from bitcoin import NumTransacciones

# Funciones de lectura de los inputs ubicados en la carpeta /data/
block_data = LecturaInputs.lectura_blocks()

# Apartado 1: número de transacciones por cada bloque
'''
Parámetros de entrada:
    - block_data resultante de la lectura del fichero "blocks.json"
    - representar: que puede tomar dos valores:
        * Y:   se muestra por pantalla una gráfica con los resultados
               y se almacena un png en la carpeta "img"
       * N:    únicamente se almacena un png en la carpeta "img"
       
El png generado tiene el nombre "A1_numtransacciones.png"
'''
results_A1 = NumTransacciones.num_transacciones(block_data, representar='N')

# Nota: Tiempo medio de ejecución 12 segundos aprox.