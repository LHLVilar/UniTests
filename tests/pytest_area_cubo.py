import pytest

import main


def teste_area_cubo_positivo():
    lado = 5

    resultado_esperado = 125

    resultado_obtido = main.area_cubo(lado)

    assert resultado_esperado == resultado_obtido

def teste_area_cubo_negativo():
    lado = -5
    main.area_cubo(lado)
    resultado_esperado = None

    resultado_obtido = main.area_cubo(lado)

    assert resultado_esperado == resultado_obtido