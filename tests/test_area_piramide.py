import pytest
import csv
import main

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: ${arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: ${fail}')


@pytest.mark.parametrize('lado, altura, resultado_esperado', ler_csv("C:\\Users\\lhvil\\PycharmProjects\\UniTests\\CSV\\piramide.csv"))
def teste_area_piramide_csv(lado, altura, resultado_esperado):

    resultado_obtido = main.area_piramide(int(lado), int(altura) )


    assert resultado_obtido == int(resultado_esperado)