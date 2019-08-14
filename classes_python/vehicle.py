
class Veiculo:
    def __init__(self, nome, cor, valor):
        self._nome = nome
        self._cor = cor
        self._valor = valor

    def descricao(self):
        return f"Carro: {self.__class__.__name__}, Cor: {self._cor}, Valor: {self._valor}, Nome: {self._nome}"


class Bug(Veiculo):
    pass


class Conversivel(Veiculo):
    pass


if __name__ == '__main__':
    carro1 = Conversivel(nome='Ferrari', valor='US$ 60.000', cor='Vermelho')
    carro2 = Bug(nome='Troller', valor=50000, cor='Azul')

    print(f"Carro1: {carro1.descricao()}")
    print(f"Carro2: {carro2.descricao()}")






