### OBJETIVO DEL PROYECTO

El presente proyecto se encuadra dentro de las Pruebas de Evalución Continua de la asignatura
 Programación para la Ciencia de Datos del master da Análisis de Datos de la universidad UOC.

El objetivo será desarrollar un paquete en Python capaz de realizar un análisis sencillo de
 datos de una serie de transacciones de Bitcoin.

### ESTRUCTURA DEL PROYECTO

La estructura de directorios es la siguiente:

* bitcoin: incluye todos los archivos .py con las funciones a utilizar durante el análisis.
    * En concreto, el archivo "basic_analysis.py" incluye la llamada a todas las funciones
    en el orden solicitado en el enunciado.
    
* data: carpeta destinada a los archivos "inputs" de nuestro programa. 
Será necesario su creación por parte de los usuarios. Además, se deberán incluir en esta carpeta
 los ficheros originales proporcionados junto a la práctica:
    * "blocks.json"
    * "txs.json"
    
* doc: carpeta donde se incluye la documentación relacionada con el proyeco. En concreto:
    * Enunciado pdf de la PEC4
    
* examples: incluye un ejemplo por cada apartado solicitado en la PEC4. (Los ejemplos se
presentan de forma independiente para mayor flexibilidad, aunque sería posible realizar
la carga de los datos mediante las funciones de lectura una única vez)
    * A1_Num_Transacciones.py
    * A2_Valor_Transacciones.py
    * A3_Tiempo_Bloques.py
    * A4_Media_Bloques_Hora.py
    * A5_Num_Transacciones_Hora.py

* img: carpeta con imágenes resultantes de la ejecución de las funciones de cada apartado.
No es necesario referenciar el path durante la ejecución del código ya que se conoce de antemano.
      
* test: incluye ficheros .py con pruebas realizadas a los ficheros de trabajo,
 así como resultados de los mismos.
 
* INSTALL.md: fichero con las instrucciones previas al uso del proyecto.

* LICENCE.txt: fichero con los datos de la licencia incluida en el proyecto.

* README.md: fichero con información útil para el proyecto

* requirements.txt: fichero con la relación de módulos adicionales necesarios para la ejecución
del código

### PARTICULARIDADES
Las funciones que presentan los resultados de cada apartado disponen de un parámetro (Y o N) que
permite la representación inline de la gráfica. Por defecto, el parámetro coge el valor "N".

En el entorno de la máquina virtual, matplotlib viene configurado de tal forma que si queremos
representar la gráfica inline nos devuelve el siguiente warning:
* matplotlib is currently using agg which is a non-gui backend so cannot show the figure

La instalación del módulo "tkinter" y el uso de "matplotlib.use('TkAgg')" lo solucionaría, pero
como la instalación del módulo es a través del terminal "sudo apt-get install python3-tk", y con el
objetivo de no modificar dicha máquina virtual más alla del entorno virtual creado para esta PEC,
no se va a instalar esta opción.

Adicionalmente al parámetro anterior, las funciones guardan en la carpeta "/img" todas las imágenes
por lo que no se ha considerado crítica la instalación del módulo "tkinter"