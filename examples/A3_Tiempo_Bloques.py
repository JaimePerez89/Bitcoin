from bitcoin import LecturaInputs
from bitcoin import TiempoMedio

# Funciones de lectura de los inputs ubicados en la carpeta /data/
block_data = LecturaInputs.lectura_blocks()

# Apartado 3: Tiempo entre bloques consecutivos
'''
Parámetros de entrada:
    - block_data resultante de la lectura del fichero "blocks.json"
    - representar: que puede tomar dos valores:
        * Y:   se muestra por pantalla una gráfica con los resultados
               y se almacena un png en la carpeta "img"
        * N:    únicamente se almacena un png en la carpeta "img"

El png generado tiene el nombre "A3_tiempobloquesconsecutivos.png"
'''
results_A3 = TiempoMedio.tiempo_medio_bloques(block_data, representar='N')

# Nota: Tiempo medio de ejecución 14 segundos aprox.