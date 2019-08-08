from math import pi

class CalcAreaRetangulo:
    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    def calc_area_retangulo(self):
        resultado = self._altura * self._largura
        return print(resultado)


class CalcAreaCirculo:
    def __init__(self, raio):
        self._raio = raio

    def calc_area_circulo(self):
        return print(f"Resultado: {pi * ( self._raio ** 2)}")


if __name__ == '__main__':
    inputraio = float(input('Raio: '))
    calc_area_circulo = CalcAreaCirculo(raio=inputraio)
    calc_area_circulo.calc_area_circulo()
    print(pi)

