import datetime
import matplotlib.pyplot as plt
from bitcoin import PlotColumns


def media_size_bloque_hr(block_data, representar='N'):
    '''
    Función que agrupa el tamaño de cada bloque en función de la hora de inicio
    y devuelve por pantalla el tamaño medio horario.
    Si se indica con el parámetro "representar", junto al mensaje se representan
    gráficamente los resultados mediante un gráfico de barras

    :param block_data: diccionario con la información de bloques (resultante de ejecutar
                        la función de lectura.
    :param representar: 'Y' la función representa por pantalla la gráfica junto
                         al mensaje.
                         'N' (valor por defecto) la función no representa la
                         gráfica junto al mensaje
    :return: mensaje por pantalla con info sobre el tamaño medio de los bloques en función
                de la hora de inicio
            'tamañomediobloques.png' en la carpeta de proyecto 'img'
    '''

    # Inicializamos dos listas que nos servirán para representar los
    # resultados
    hora_ejex = []
    tamaño_medio_y = []

    # Inicializamos un diccionario donde guardaremos los resultados
    media_bloque = {}

    for i in block_data:
        # Obtengo el dato del tamaño del bloque
        size = block_data[i]['size']

        # Obtengo la hora de inicio del bloque
        time = block_data[i]['time']
        time = datetime.datetime.fromtimestamp(time)
        hora = time.hour

        # Vamos a insertar el tamaño en una lista dentro de un diccionario
        # La key del diccionario identificará la hora
        # Para no crear de antemano todas las opciones del diccionario
        # Recurrimemos a un try-except para cuando no exista la key, crearla
        try:
            # Si ya existe la key, agregamos el tamaño a la lista
            media_bloque[hora].append(size)
        except:
            # Si no existe la key, devolverá un error y se ejecutará este código
            # que creará esa key e iniciará una lista con el valor del tamaño
            media_bloque[hora] = [size]

    # Recorremos el diccionario con los resultados para mostrar por pantalla
    # la media de los tamaños.
    # Para que nos salga ordenado, vamos a recorrer hora a hora, y no por keys
    for j in range(24):
        # Obtenemos el valor medio para esa hora
        try:
            valor_medio = sum(media_bloque[j]) / len(media_bloque[j])
        except:
            # En caso de no tener bloques para esa hora, asignamos al valor
            # medio el valor cero
            valor_medio = 0

        print("El valor medio de los tamaños para la hora {} es {}"
              .format(j, valor_medio))

        # Además de mostrar el resultado, agregamos la info a las lista que nos
        # servirán para representar los ejes en la gráfica
        hora_ejex.append(j)
        tamaño_medio_y.append(valor_medio)

    # Definimos datos para el eje x y para el eje y
    x = hora_ejex
    y = tamaño_medio_y
    titulo_x = 'Hora del día'
    titulo_y = 'Tamaño medio de los bloques'
    plot_title = 'TAMAÑO MEDIO DE LOS BLOQUES PARA CADA HORA'
    size = (20, 10)  # Parámetro con el tamaño del gráfico resultante
    plot_name = 'A4_TamañoMedioBloques.png'

    # Llamamos a la función que dibuja el gráfico
    PlotColumns.plot_col_graph(x, y, titulo_x, titulo_y, plot_title,
                               size, plot_name, representar)

    return