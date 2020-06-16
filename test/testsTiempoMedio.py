import unittest
from bitcoin import LecturaInputs
from bitcoin import TiempoMedio


class Tiempo_Medio_Horario(unittest.TestCase):

    def test_dict_tam_bloques(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        # Necesitamos cargar los datos de txs_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual(type(TiempoMedio.tiempo_medio_bloques(block_data, 'N')),
                         type(dict_test))

    def test_cant_horas(self):
        # Compruebo que el número de horas es de 24

        # Necesitamos cargar los datos de txs_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual(len(TiempoMedio.tiempo_medio_bloques(block_data, 'N').keys()),
                         144)


if __name__ == '__main__':
    unittest.main()