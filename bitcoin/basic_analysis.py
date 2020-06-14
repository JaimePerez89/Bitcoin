from LecturaInputs import lectura_blocks, lectura_transacciones
from NumTransacciones import num_transacciones
from ValorAcumulado import valor_acumulado_txs
from TiempoMedio import tiempo_medio_bloques
from TamañoHorarioBloques import media_size_bloque_hr
from NumHorarioTransacciones import cantidad_transacciones_hr

# Funciones de lectura de los inputs
block_data = lectura_blocks()
txs_data = lectura_transacciones()

# Apartado 1: número de transacciones para cada bloque
num_transacciones(block_data, 'N')

# Apartado 2: Valor acumulado de las transacciones en cada bloque
valor_acumulado_txs(block_data, txs_data, 'N')

# Apartado 3: Tiempo entre bloques consecutivos
tiempo_medio_bloques(block_data, 'N')

# Apartado 4: Media del tamaño del bloque por hora
media_size_bloque_hr(block_data, 'N')

# Apartado 5: Número de transacciones por hora
cantidad_transacciones_hr(txs_data, 'N')