from datetime import datetime
from time import sleep


def calcula_tempo(func, *args):
    def wrapper(*args, **kwargs):
        inicio = datetime.now().timestamp()
        func(*args, **kwargs)
        fim = datetime.now().timestamp()
        print(f'A funcao {func.__name__} demorou {fim - inicio} segundos')
    return wrapper


@calcula_tempo
def funcao_lista():
    listinha = []
    for i in range(10000000):
        listinha.append(i)
        print(i)
    return listinha[:3]
