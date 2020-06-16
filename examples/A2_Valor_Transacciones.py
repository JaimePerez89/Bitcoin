from bitcoin import LecturaInputs
from bitcoin import ValorAcumulado

# Funciones de lectura de los inputs de la carpeta /data/
block_data = LecturaInputs.lectura_blocks()
txs_data = LecturaInputs.lectura_transacciones()

# Apartado 2: Valor acumulado de las transacciones en cada bloque
'''
Parámetros de entrada:
    - block_data resultante de la lectura del fichero "blocks.json"
    - txs_data resultante de la lectura del fichero "txs.json"
    - representar: que puede tomar dos valores:
        * Y:   se muestra por pantalla una gráfica con los resultados
               y se almacena un png en la carpeta "img"
        * N:    únicamente se almacena un png en la carpeta "img"

El png generado tiene el nombre "A2_valoracumulado.png"
'''
results_A2 = ValorAcumulado.valor_acumulado_txs(block_data, txs_data, representar='N')

# Nota: Tiempo medio de ejecución 26 segundos aprox.