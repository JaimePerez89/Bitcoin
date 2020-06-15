import matplotlib.pyplot as plt
import os


def plot_col_graph(x, y, titulo_x, titulo_y, plot_title, size, name, representar='N'):
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