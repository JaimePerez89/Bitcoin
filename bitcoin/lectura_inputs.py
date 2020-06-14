import json


def lectura_blocks():
    '''
    Función que lee el archivo input de bloques (blocks.json) ubicado en la carpeta data.
    Almacenando únicamente la información deseada en un diccionario "block_data"
    :args: -
    :return: diccionario block_data
    '''

    # Creamos un diccionario vacio que almacenará la información deseada del input
    block_data = {}

    # Dado que la ubicación del archivo será fija en el proyecto, le pasamos el path directamente
    with open('../data/blocks.json', 'r') as f:
        for line in f:
            df_line = json.loads(line)
            # Almacenamos la información que deseamos en el diccionario previamente creado
            # De forma que la key del diccionario será el hash identificativo del bloque
            # Y los items serán a su vez diccionarios con la información deseada en forma de listas
            block_data[df_line['hash']] = {'size': df_line['size'], 'tx': df_line['tx'],
                                           'time': df_line['time'], 'nTx': df_line['nTx'],
                                           'previousblockhash': df_line['previousblockhash']}
    return block_data


def lectura_transacciones():
    '''
    Función que lee el archivo input de transacciones (txs.json) ubicado en la carpeta data.
    Almacenará únicamente la información deseada en un diccionario "txs_data"
    :args: -
    :return: diccionario txs_data
    '''

    # Creamos un diccionario vacío que almacenará la información deseada del input
    txs_data = {}

    # Dado que la ubicación del archivo será fija, podemos pasar directamente el path a la función
    with open('../data/txs.json', 'r') as f:
        for line in f:
            df_line = json.loads(line)
            # Inicializamos una lista vacía donde guardaremos todos los valores "values"
            # de cada uno de los elementos del "vout" que contiene una transacción
            # Para cada línea del input, se pondrá a cero
            values = []

            # Iteramos sobre vout para obtener los values
            for i in df_line['vout']:
                values.append(i['value'])  # Lo añadimos al ventor inicializado antes

            # Almacenamos la información que deseamos en el diccionario previamente creado
            # La key del diccionario será el identificador de cada transacción "txid"
            # El contenido de cada key será un diccionario con los siguientes items:
            #    - el hash identificativo del bloque al que pertenece la transacción
            #    - una lista con todos los valores de "vout" de las transacciones
            #    - el tiempo registrado de inicio de la transacción
            txs_data[df_line['txid']] = {'blockhash': df_line['blockhash'],
                                         'values': values,
                                         'time': df_line['time']}
    return txs_data