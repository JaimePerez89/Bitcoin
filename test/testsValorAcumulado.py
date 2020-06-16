import unittest
from bitcoin import LecturaInputs
from bitcoin import ValorAcumulado

class ValorAcumulado_Transacciones(unittest.TestCase):

    def test_dict_valoracumulado(self):
        # Comprobamos si las funciones nos retornan un diccionario
        dict_test = {}  # Creo uno vacio que nos sirva de referencia
        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()
        txs_data = LecturaInputs.lectura_transacciones()

        self.assertEqual(type(ValorAcumulado.valor_acumulado_txs(block_data, txs_data, 'N')),
                         type(dict_test))

    def test_cant_transacciones_vacumulado(self):
        # Compruebo que la longitud del diccionario es igual al numero de
        # bloques que se proponen en la PEC

        # Necesitamos cargar los datos de block_data
        block_data = LecturaInputs.lectura_blocks()
        txs_data = LecturaInputs.lectura_transacciones()

        self.assertEqual(len(ValorAcumulado.valor_acumulado_txs(block_data, txs_data, 'N').keys()),
                         144)


if __name__ == '__main__':
    unittest.main()