from bitcoin import LecturaInputs
from bitcoin import NumHorarioTransacciones

# Funciones de lectura de los inputs de la carpeta /data/
txs_data = LecturaInputs.lectura_transacciones()


# Apartado 5: Número de transacciones por hora
'''
Parámetros de entrada:
    - txs_data resultante de la lectura del fichero "txs.json"
    - representar: que puede tomar dos valores:
        * Y:   se muestra por pantalla una gráfica con los resultados
               y se almacena un png en la carpeta "img"
        * N:    únicamente se almacena un png en la carpeta "img"

El png generado tiene el nombre "A5_numhorariotransacciones.png"
'''
NumHorarioTransacciones.cantidad_transacciones_hr(txs_data, representar='N')

# Nota: Tiempo medio de ejecución 14 segundo aprox.