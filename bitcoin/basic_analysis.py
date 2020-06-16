from LecturaInputs import lectura_blocks, lectura_transacciones
from NumTransacciones import num_transacciones
from ValorAcumulado import valor_acumulado_txs
from TiempoMedio import tiempo_medio_bloques
from TamañoHorarioBloques import media_size_bloque_hr
from NumHorarioTransacciones import cantidad_transacciones_hr

# Funciones de lectura de los inputs
# Sería la carga previa de los datos
block_data = lectura_blocks()
txs_data = lectura_transacciones()

# Todas las soluciones se almacenan en un diccionario "result_AX"
# Por defecto, se mostrarán por pantalla los resultados

# El parámetro de reprensetar, por defecto "N", activa o desactiva
# si queremos que se nos muestre el gráfico de resultados por pantalla
# o no. Independientemente del parámetro, se almacena un png en /img

# Apartado 1: número de transacciones para cada bloque
result_A1 = num_transacciones(block_data, representar='N')

# Apartado 2: Valor acumulado de las transacciones en cada bloque
result_A2 = valor_acumulado_txs(block_data, txs_data, representar='N')

# Apartado 3: Tiempo entre bloques consecutivos
result_A3 = tiempo_medio_bloques(block_data, representar='N')

# Apartado 4: Media del tamaño del bloque por hora
result_A4 = media_size_bloque_hr(block_data, representar='N')

# Apartado 5: Número de transacciones por hora
result_A5 = cantidad_transacciones_hr(txs_data, representar='N')