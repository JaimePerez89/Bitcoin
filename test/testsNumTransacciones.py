import unittest
from bitcoin import LecturaInputs
from bitcoin import NumTransacciones


class Num_Transacciones(unittest.TestCase):

    def test_dict_transacciones(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual(type(NumTransacciones.num_transacciones(block_data, 'N')),
                         type(dict_test))


    def test_cant_transacciones(self):
        # Compruebo que la longitud del diccionario es igual al numero de
        # bloques que se proponen en la PEC

        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()

        self.assertEqual( len(NumTransacciones.num_transacciones(block_data, 'N').keys()),
                          144)

if __name__ == '__main__':
    unittest.main()