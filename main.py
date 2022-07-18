

def area_cubo(lado):
    area = lado ** 3
    if area > 0:
        return area
    else:
        return print('Não existe área zero')

def area_paralelogramo(lado, altura):
    return lado * altura

def area_piramide(lado, altura):
    return (lado * altura) / 2

if __name__ == '__main__':
    print(area_cubo(5))
    print(area_paralelogramo(2,5))
    print(area_piramide(2,5))
