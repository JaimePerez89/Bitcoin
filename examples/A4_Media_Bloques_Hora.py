from bitcoin import LecturaInputs
from bitcoin import TamanioHorarioBloques


# Funciones de lectura de los inputs ubicados en la carpeta /data/
block_data = LecturaInputs.lectura_blocks()

# Apartado 4: Media del tamaño del bloque por hora
'''
Parámetros de entrada:
    - block_data resultante de la lectura del fichero "blocks.json"
    - representar: que puede tomar dos valores:
        * Y:   se muestra por pantalla una gráfica con los resultados
               y se almacena un png en la carpeta "img"
        * N:    únicamente se almacena un png en la carpeta "img"

El png generado tiene el nombre "A4_tamañomediobloques.png"
'''
results_A4 = TamanioHorarioBloques.media_size_bloque_hr(block_data, representar='N')

# Nota: Tiempo medio de ejecución 1 segundo aprox.