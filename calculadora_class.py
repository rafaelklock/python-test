"""
Classe que faz alguns calculos em python
"""

from math import pi

class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def divisao(self, a, b):
        return a / b

    def multiplicacao(self, a, b):
        return a * b

    def area_retangulo(self, altura, largura):
        return altura * largura

    def area_circulo(self, raio):
        return pi * (raio ** 2)





