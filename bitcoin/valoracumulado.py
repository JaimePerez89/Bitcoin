

def valor_acumulado_txs(block_data, txs_data, representar='N'):
    '''

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

    # Representamos gráficamente los resultados
    plt.style.use('ggplot')  # Utilizaremos el tema ggplot

    # Definimos un tamaño que nos resulte cómodo de visualizar
    fig = plt.figure(figsize=(60, 40))
    plt.bar(block_x, valor_acumulado_y)
    plt.xticks(range(len(block_x)), block_x, fontsize=8, rotation=90)
    plt.xlabel('Identificador hash de cada bloque', fontsize=18)
    plt.ylabel('Valor acumulado de las transacciones / bloque', fontsize=18)
    plt.title('VALOR ACUMULADO DE LAS TRANSACCIONES EJECUTADAS EN CADA BLOQUE', fontsize=30)
    plt.savefig('../img/valoracumulado.png', dpi=100)

    # Analizo el parámetro de entrada para estudiar si representamos la gráfica
    if representar == 'N':
        plt.close(fig)
    else:
        plt.show()
        plt.close(fig)
    return

