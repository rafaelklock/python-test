# pytest pontos.py
from desafios.pontos import add_dots
from desafios.pontos import del_dots


def test_add_dots():
    result = add_dots('test')
    assert result == 't.e.s.t'


def test_del_dots():
    result = del_dots('t.e.s.t')
    assert result == 'test'


def test_add_dots_vazio():
    result = add_dots('')
    assert result == ''


