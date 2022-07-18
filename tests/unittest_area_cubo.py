import unittest

import main


class Teste_atividade_6(unittest.TestCase):
    def teste_area_cubo_positivo(self):

        lado = 5
        resultado_esperado = 125

        resultado_obtido = main.area_cubo(lado)

        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here


if __name__ == '__main__':
    unittest.main()
