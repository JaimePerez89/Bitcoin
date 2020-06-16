import unittest
from bitcoin import LecturaInputs

class Test_Lecturas(unittest.TestCase):

    def test_dict(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        self.assertEqual(type(LecturaInputs.lectura_blocks()), type(dict_test))
        self.assertEqual(type(LecturaInputs.lectura_transacciones()), type(dict_test))

    def test_cant_bloques(self):
        # Compruebo que la longitud del diccionario es igual al numero de
        # bloques que se proponen en la PEC
        self.assertEqual( len(LecturaInputs.lectura_blocks().keys()) , 144)

if __name__ == '__main__':
    unittest.main()