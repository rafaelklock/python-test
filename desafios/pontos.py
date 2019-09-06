import io


def add_dots(stringzona):
    return '.'.join(list(stringzona))


def del_dots(stringzona):
    resultado = stringzona.split('.')
    final = ''
    for i in resultado:
        final = final + i
    return final


string_sem_pontos= 'test'
string_com_pontos = 't.e.s.t'

print(add_dots(string_sem_pontos))
print(del_dots(string_com_pontos))
