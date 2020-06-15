import datetime
import matplotlib.pyplot as plt


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

    # Representamos gráficamente los resultados
    plt.style.use('ggplot')  # Utilizaremos el tema ggplot

    # Definimos un tamaño que nos resulte cómodo de visualizar
    fig = plt.figure(figsize=(60, 40))
    plt.bar(block_x, delta_time_y)
    plt.xticks(range(len(block_x)), block_x, fontsize=8, rotation=90)
    # La etiqueta x solo vamos a incluir la referencia de un bloque. La referencia del anterior
    # la vamos a omitir para no saturar más aún el gráfico
    plt.xlabel('Identificador hash de cada bloque', fontsize=18)
    plt.ylabel('Diferencia de tiempos entre cada bloque consecutivo (s)', fontsize=18)
    plt.title('DIFERENCIA DE TIEMPOS ENTRE BLOQUES CONSECUTIVOS (segundos)', fontsize=30)
    plt.savefig('../img/A3_tiempobloquesconsecutivos.png', dpi=100)

    # Analizo el parámetro de entrada para estudiar si representamos la gráfica
    if representar == 'N':
        plt.close(fig)
    else:
        plt.show()
        plt.close(fig)

    return