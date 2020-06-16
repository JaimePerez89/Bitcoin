import matplotlib.pyplot as plt
import os


def plot_col_graph(x, y, titulo_x, titulo_y, plot_title, size, name, representar='N'):
    '''
    Función que genera un gráfico de barras a partir de los parámetros de entrada

    :param x: datos eje x
    :param y: datos eje y
    :param titulo_x: título eje x
    :param titulo_y: título eje y
    :param plot_title: título del gráfico
    :param size: tamaño del gráfico. Por ejemplo: size = (20, 10)
    :param name: nombre del fichero png generado
    :param representar: parámetro que nos indica si queremos devolver el gráfico
            por pantalla o no. Puede tomar los valores 'Y' o 'N'
    :return: fig: se retorna un gráfico para que en caso que el parámetro representar
            sea 'Y' se pueda presentar el gráfico por pantalla
    '''
    plt.style.use('ggplot')  # Utilizaremos el tema ggplot

    # Definimos el tamaño en función del parámetro de entrada
    fig = plt.figure(figsize=size)
    # Añadimos datos en el eje x y en el eje y
    plt.bar(x, y)

    # Añadimos informaición en los ejes
    plt.xticks(range(len(x)), x, fontsize=8, rotation=90)
    plt.xlabel(titulo_x, fontsize=18)
    plt.ylabel(titulo_y, fontsize=18)
    plt.title(plot_title, fontsize=30)

    # Guardo la imagen en la carpeta img con el nombre indicado
    data_folder = '../img/'
    full_path = os.path.join(data_folder, name)
    plt.savefig(full_path, dpi=100)

    # Analizo el parámetro de entrada para estudiar si representamos la gráfica
    if representar == 'N':
        plt.close(fig)
    else:
        plt.show()
        plt.close(fig)

    return fig