import matplotlib.pyplot as plt
from bitcoin import PlotColumns


def num_transacciones(block_data, representar='N'):
    '''
    La  función analiza los datos de bloques y presenta por pantalla un mensaje
    para cada bloque donde se expone el número de transacciones producidas
    Además, se incluye la representación gráfica de los resultados, por defecto
    se crea una imagen png en la carpeta "img". Si el argumento de entrada
    eje x y eje y.

    :param  block_data: diccionario con la información de bloques (resultante de ejecutar
                        la función de lectura.
            representar: 'Y' la función representa por pantalla la gráfica junto
                         al mensaje.
                         'N' (valor por defecto) la función no representa la
                         gráfica junto al mensaje

    :return mensaje por pantalla con info sobre bloque y num. transacciones
            'numtransacciones.png' en la carpeta de proyecto 'img'
    '''

    # Creamos dos listas vacias, que serán los futuros ejes de los gráficos
    x = []
    y = []

    # Inicializamos un diccionario con los resultados
    results = {}

    # Iteramos para cada elemento del diccionario de entrada
    for i in block_data:
        num_tran = block_data[i]['nTx']

        # Añadimos la información a las listas de ejes para representar
        x.append(i)
        y.append(num_tran)

        # Añadimos la info a un diccionario que retornaremos como solución
        results[i] = num_tran

        # Imprimimos por pantalla un mensaje donde se expone el bloque analizado
        # y el número de transacciones ocurridas en él
        print("El bloque '{}' tiene \t{} transacciones"
              .format(i, num_tran))

    # Definimos datos para el eje x y para el eje y
    x = x
    y = y
    titulo_x = 'Identificador hash de cada bloque'
    titulo_y = 'Número de transacciones / bloque'
    plot_title = 'NÚMERO DE TRANSACCIONES EJECUTADAS EN CADA BLOQUE'
    size = (50, 45)  # Parámetro con el tamaño del gráfico resultante
    plot_name = 'A1_NumTransacciones.png'

    # Llamamos a la función que dibuja el gráfico
    PlotColumns.plot_col_graph(x, y, titulo_x, titulo_y, plot_title,
                               size, plot_name, representar)

    return results