import unittest
from bitcoin import LecturaInputs
from bitcoin import NumHorarioTransacciones


class Tam_Horario_Bloques(unittest.TestCase):

    def test_dict_tam_bloques(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        # Necesitamos cargar los datos de txs_data
        txs_data = LecturaInputs.lectura_transacciones()

        self.assertEqual(type(NumHorarioTransacciones.cantidad_transacciones_hr(txs_data, 'N')),
                         type(dict_test))

    def test_cant_horas(self):
        # Compruebo que el número de horas es de 24

        # Necesitamos cargar los datos de txs_data
        txs_data = LecturaInputs.lectura_blocks()

        self.assertEqual(len(NumHorarioTransacciones.cantidad_transacciones_hr(txs_data, 'N').keys()),
                         24)


if __name__ == '__main__':
    unittest.main()