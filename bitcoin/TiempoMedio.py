import datetime
import matplotlib.pyplot as plt
from bitcoin import PlotColumns


def tiempo_medio_bloques(block_data, representar='N'):
    '''

    :param block_data: diccionario con la información de bloques (resultante de ejecutar
                        la función de lectura.
    :param representar: 'Y' la función representa por pantalla la gráfica junto
                         al mensaje.
                         'N' (valor por defecto) la función no representa la
                         gráfica junto al mensaje
    :return: mensaje por pantalla con info sobre bloques consecutivos y tiempo transcurrido
                entre ellos en segundos
            'tiempobloquesconsecutivos.png' en la carpeta de proyecto 'img'
    '''

    # Inicializamos dos listas vacias que nos servirán como ejes para la representación
    # gráfica de los resultados
    block_x = []
    delta_time_y = []

    # Iteramos para cada uno de los bloques
    for i in block_data:
        # Obtenemos la fecha de inicio del bloque
        tiempo_actual = block_data[i]['time']
        tiempo_actual = datetime.datetime.fromtimestamp(tiempo_actual)

        # Para obtener la fecha de inicio del bloque anterior
        # Obtenemos el bloque previo al actual
        bloque_previo = block_data[i]['previousblockhash']
        # Obtenemos cuando se ejecutó

        try:
            tiempo_previo = block_data[bloque_previo]['time']
            tiempo_previo = datetime.datetime.fromtimestamp(tiempo_previo)

            # Calculamos la diferencia entre la ejecución de los bloques
            delta = tiempo_actual - tiempo_previo

            # Añadimos los datos a las listas de los ejes de representación gráfica
            block_x.append(i)
            delta_time_y.append(delta.total_seconds())

            # Mostramos el resultado por pantalla
            print("El tiempo trancurrido entre el bloque '{}' y el bloque '{}' ha sido de {} segundos"
                  .format(i, bloque_previo, delta.total_seconds()))

        except:
            print("No se dispone de tiempo de referencia previo para el bloque {}".format(i))

    # Definimos datos para el eje x y para el eje y
    x = block_x
    y = delta_time_y
    titulo_x = 'Identificador hash de cada bloque'
    titulo_y = 'Diferencia de tiempos entre cada bloque consecutivo (s)'
    plot_title = 'DIFERENCIA DE TIEMPOS ENTRE BLOQUES CONSECUTIVOS (segundos)'
    size = (50, 45)  # Parámetro con el tamaño del gráfico resultante
    plot_name = 'A3_TiempoBloquesConsecutivos.png'

    # Llamamos a la función que dibuja el gráfico
    PlotColumns.plot_col_graph(x, y, titulo_x, titulo_y, plot_title,
                               size, plot_name, representar)

    return block_x, delta_time_y