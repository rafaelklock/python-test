from pytest import fixture
from desafios import ano_bisexto


def test_bisexto_d4():
    assert ano_bisexto.calc_ano_bisexto(2000) == 0



