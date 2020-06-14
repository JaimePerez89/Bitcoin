import matplotlib.pyplot as plt

def num_transacciones(data, representar='N'):
    '''
    La  función analiza los datos de bloques y presenta por pantalla un mensaje
    para cada bloque donde se expone el número de transacciones producidas
    Además, se incluye la representación gráfica de los resultados, por defecto
    se crea una imagen png en la carpeta "img". Si el argumento de entrada
    eje x y eje y.

    :param  blocks_data: diccionario con la información de bloques (resultante de ejecutar
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

    # Iteramos para cada elemento del diccionario de entrada
    for i in data:
        # Añadimos la información a las listas de ejes
        x.append(i)
        y.append(data[i]['nTx'])

        # Imprimimos por pantalla un mensaje donde se expone el bloque analizado
        # y el número de transacciones ocurridas en él
        print("El bloque '{}' tiene \t{}\t transacciones".format(i, data[i]['nTx']))

    # Representamos gráficamente los resultados
    plt.style.use('ggplot')  # Utilizaremos el tema ggplot

    # Definimos un tamaño que nos resulte cómodo de visualizar
    fig = plt.figure(figsize=(60, 40))
    plt.bar(x, y)
    plt.xticks(range(len(x)), x, fontsize=8, rotation=90)
    plt.xlabel('Identificador hash de cada bloque', fontsize=18)
    plt.ylabel('Número de transacciones / bloque', fontsize=18)
    plt.title('NÚMERO DE TRANSACCIONES EJECUTADAS EN CADA BLOQUE', fontsize=30)
    plt.savefig('../img/numtransacciones.png', dpi=100)

    # Analizo el parámetro de entrada para estudiar si representamos la gráfica
    if representar == 'N':
        plt.close(fig)
    else:
        plt.show()
        plt.close(fig)
    return