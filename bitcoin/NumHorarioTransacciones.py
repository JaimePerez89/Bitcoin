import datetime
from bitcoin import PlotColumns


def cantidad_transacciones_hr(txs_data, representar='N'):
    '''
    Función que contabiliza y acumula el número de transacciones en función de la hora
    de inicio de las mismas, devolviendo por pantalla un mensaje.
    Si se indica con el parámetro "representar", junto al mensaje, se representa
    gráficamente los resultados mediante un gráfico de barras

    :param block_data: diccionario con la información de transacciones (resultante
                        de ejecutar la función de lectura.
    :param representar: 'Y' la función representa por pantalla la gráfica junto
                         al mensaje.
                         'N' (valor por defecto) la función no representa la
                         gráfica junto al mensaje
    :return: results (dict): diccionario con los resultados
             mensaje por pantalla con info sobre el número de transacciones que se producen
                para cada hora.
            'A5_NumHorarioTransacciones.png' en la carpeta de proyecto 'img'
    '''

    # Inicializamos dos listas que nos servirán para representar los
    # resultados
    hora_ejex = []
    num_transacciones_y = []

    # Inicializamos un diccionario donde guardaremos los resultados durante los bluques
    num_transacciones = {}

    # Inicializamos un diccionario donde guardaremos los resultados finales
    results = {}

    for i in txs_data:
        # Obtengo la hora de inicio de la transaccion
        time = txs_data[i]['time']
        time = datetime.datetime.fromtimestamp(time)
        hora = time.hour

        # Para cada hora del día creamos una key en el diccionario num_transacciones
        # Para cada transacción, insertaremos un valor unitario en la lista
        # cuya key coincidad con su hora de inicio
        # Para no crear de antemano todas las opciones del diccionario
        # Recurrimemos a un try-except para, cuando no exista la key, crearla
        try:
            # Si ya existe la key, agregamos el tamaño a la lista
            num_transacciones[hora].append(1)
        except:
            # Si no existe la key, devolverá un error y se ejecutará este código
            # que creará esa key e iniciará una lista con el valor unitario
            num_transacciones[hora] = [1]

    # Recorremos el diccionario con los resultados para mostrar por pantalla
    # la cantidad de transacciones ejecutadas en cada hora.
    # Para que nos salga ordenado, vamos a recorrerlo hora a hora, y no por keys
    for j in range(24):
        # Obtenemos la suma de los unitarios de la lista para esa hora
        try:
            cantidad = sum(num_transacciones[j])
        except:
            # En caso de no tener bloques para esa hora, asignamos al valor
            # medio el valor cero
            cantidad = 0

        print("El número de transacciones ejecutadas durante la hora {} fue {}"
              .format(j, cantidad))

        # Además de mostrar el resultado, agregamos la info a las lista que nos
        # servirán para representar los ejes en la gráfica
        hora_ejex.append(j)
        num_transacciones_y.append(cantidad)

        # Añadimos al diccionario de resultados
        results[j] = cantidad

    # Definimos datos para el eje x y para el eje y
    x = hora_ejex
    y = num_transacciones_y
    titulo_x = 'Hora del día'
    titulo_y = 'Número de transacciones por hora'
    plot_title = 'CANTIDAD DE TRANSACCIONES OCURRIDAS DURANTE CADA HORA'
    size = (20, 10)  # Parámetro con el tamaño del gráfico resultante
    plot_name = 'A5_NumHorarioTransacciones.png'

    # Llamamos a la función que dibuja el gráfico
    PlotColumns.plot_col_graph(x, y, titulo_x, titulo_y, plot_title,
                               size, plot_name, representar)

    return results