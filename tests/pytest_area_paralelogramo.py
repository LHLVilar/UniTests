import pytest

import main

massa_teste = [
        (2, 2, 4),
        (3, -4, 12),
        (3, -5, 15)
    ]

@pytest.mark.parametrize('lado, altura, resultado_esperado', massa_teste)
def teste_area_parelelogramo_positivo(lado, altura, resultado_esperado):

    resultado_obtido = main.area_paralelogramo(lado,altura)

    assert resultado_obtido == resultado_esperado