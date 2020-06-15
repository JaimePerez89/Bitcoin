import matplotlib.pyplot as plt
from bitcoin import PlotColumns


def valor_acumulado_txs(block_data, txs_data, representar='N'):
    '''
    Función que devuelve por pantalla el valor acumulado de las transacciones ejecutadas
    para cada bloque.
    Adicionalmente, se genera una imagen png con la representación gráfica de los resultados,
    siendo además, mostrada por pantalla si el usuario así lo indica durante la llamada a la
    función.

    :param block_data: diccionario con la información de bloques (resultante de ejecutar
                        la función de lectura.
    :param txs_data: diccionario con la información de las transacciones (resultante de
                        ejecutar la función de lectura
    :param representar: parámetro que indica si deseamos representar la gráfica
                    'Y': la función representa por pantalla la gráfica junto al mensaje.
                    'N' (valor por defecto) la función no representa la gráfica
    :return: mensaje por pantalla con info sobre bloque y valor acumulado de las transacciones
            'valoracumulado.png' en la carpeta de proyecto 'img' con los resultados
    '''

    # Inicializo dos listas a las cuales les iremos insertando la información
    # del valor acumulado, con el objetivo de representar gráficamente los
    # resultados
    block_x = []
    valor_acumulado_y = []
    # Itero para cada bloque
    for i in block_data:
        # Para cada bloque inicializo una lista vacia donde acumularemos los valores
        # de cada transacción
        value = []
        # Itero para cada transacción del bloque i
        for j in block_data[i]['tx']:
            # Para cada transacción busco la lista de "values" en el fichero de txs
            # y se la inserto a la lista "value"
            value.extend(txs_data[j]['values'])

        # Una vez iterado por todas las transacciones de un bloque, realizo la suma
        # de los valores de cada una
        acum_value = sum(value)

        # Añado la información a las listas que representarán cada eje
        block_x.append(i)
        valor_acumulado_y.append(acum_value)

        # Imprimo por pantalla un mensaje donde se muestra para cada bloque, el valor
        # acumulado de las transacciones
        print("El valor acumulado de las transacciones para el bloque '{}' es {}"
              .format(i, acum_value))

    # Definimos datos para el eje x y para el eje y
    x = block_x
    y = valor_acumulado_y
    titulo_x = 'Identificador hash de cada bloque'
    titulo_y = 'Valor acumulado de las transacciones / bloque'
    plot_title = 'VALOR ACUMULADO DE LAS TRANSACCIONES EJECUTADAS EN CADA BLOQUE'
    size = (50, 45)  # Parámetro con el tamaño del gráfico resultante
    plot_name = 'A2_ValorAcumulado.png'

    # Llamamos a la función que dibuja el gráfico
    PlotColumns.plot_col_graph(x, y, titulo_x, titulo_y, plot_title,
                               size, plot_name, representar)

    return

