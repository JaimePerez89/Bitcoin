import unittest
from bitcoin import LecturaInputs
from bitcoin import TamanioHorarioBloques


class Tam_Horario_Bloques(unittest.TestCase):

    def test_dict_tam_bloques(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual(type(TamanioHorarioBloques.media_size_bloque_hr(block_data, 'N')),
                         type(dict_test))

    def test_cant_horas(self):
        # Compruebo que el número de horas es de 24

        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual(len(TamanioHorarioBloques.media_size_bloque_hr(block_data, 'N').keys()),
                         24)


if __name__ == '__main__':
    unittest.main()