import unittest

aniversarios_dic = {
    'Vinicius Melo': '24/09/1993',
    'Rafael Klock': '20/04/1991',
    'Vagner Cordeiro': '16/07/1987',
}


def aniversario(nome):



def main():
    print(aniversarios_dic.keys())
    print('Qual niver vc quer retornar? ')
    nome = input()
    data_niver = aniversario(nome)
    print(f'{nome} nasceu no dia {data_niver}')


class TestAniversario(unittest.TestCase):

    def test_vinicius(self):
        data_niver = aniversario('Vinicius Melo')
        self.assertEqual(data_niver, '24/09/1993')

    def test_vazio(self):
        data = aniversario('')
        with self.assertRaises(Exception):
            aniversario('')



