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

    # Dado que la ubicación del archivo será fija en el proyecto, se la pasamos directamente
    with open('../data/blocks.json', 'r') as f:
        for line in f:
            df_line = json.loads(line)
            # Almacenamos la información que deseamos en el diccionario previamente creado
            # De forma que la key del diccionario será el hash identificativo del bloque
            # Y los items serán la información en formato de lista con el orden mostrado a continuación
            block_data[df_line['hash']] = [df_line['size'], df_line['tx'], df_line['time'], df_line['nTx'],
                                           df_line['previousblockhash']]
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

            # Añadimos al diccionario final solo la información que deseamos
            # Las keys del diccionario serán los identificadores de cada transacción "txid"
            # El contenido de cada key será una lista con el hash identificativo del bloque
            # al que pertenece, una lista con todos los valores de las transacciones, y el
            # tiempo registrado de inicio de la transacción
            txs_data[df_line['txid']] = [df_line['blockhash'], values, df_line['time']]
    return txs_data
