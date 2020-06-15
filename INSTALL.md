# PROCESO DE INSTALACIÓN

Para el correcto uso del paquete es necesario que el usuario realice una serie de operaciones previas.

* El usuario deberá instalar un entorno virtual preferiblemente en python 3.6 o posterior. Para ello,
el usuario puede ayudarse del entorno proporcionado por PyCharm. El resultado del proceso será la
creación de la carpeta "venv" (library root).

* El usuario deberá instalar manualmente las librerias adicionales no incluidas en el entorno python.
Estas librerias se encuentran en el archivo "requirements.txt".

* El usuario deberá crear en la raiz del proyecto una carpeta con el nombre "data" e incluir manualmente
los inputs proporcionados en el enunciado de la práctica:
    * blocks.json (/Bitcoin/data/blocks.json)
    * txs.json (/Bitcoin/data/txs.json)