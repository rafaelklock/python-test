from ..classes_python.calculadora_class import Calculadora
from pytest import fixture


@fixture
def soma():
    return Calculadora.soma


@fixture
def subtracao():
    return Calculadora.subtracao


@fixture
def multiplicacao():
    return Calculadora.multiplicacao


@fixture
def divisao():
    return Calculadora.divisao


def test_soma_verdadeiro(soma):
    assert soma(1, 1) == 2


def test_subtacao_verdadeiro(subtracao):
    assert subtracao(1, 2) == 0


