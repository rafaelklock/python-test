from math import pi


class Circulo:
    def __init__(self, raio):
        self._raio = raio

    def calcula_perimetro(self):
        return 2 * pi * self._raio

    def calcula_area(self):
        #    return (pow(self._raio, 2)) * pi
        return pi * (self._raio ** self._raio)

    def calula_diametro(self):
        return self._raio * 2


if __name__ == '__main__':
    circulo = Circulo(int(input('Raio: ')))
    area = circulo.calcula_area()
    perimetro = circulo.calcula_perimetro()
    diametro = circulo.calula_diametro()
    print('Area: ', round(area))  # round faz o aredondamento do valor.
    print("Perímetro: ", round(perimetro))
    print("Diametro: ", diametro)
