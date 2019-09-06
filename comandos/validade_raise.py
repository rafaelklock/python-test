
class DataInvalidaNoTipo(Exception):
    pass


def validate(*args):
    for i in args:
        if i not in ('bigint', 'numeric'):
            raise DataInvalidaNoTipo(f"Tipo nao é valido. vc digitou: {i}")



