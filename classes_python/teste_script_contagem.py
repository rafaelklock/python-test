"""
Criar doism scripts que ao imputar uma string
 retorne outra no formato dos exemplos abaixo
(a partir da contagem dos caracteres)
"""
from itertools import count

frase = input('Digite uma frase: ')

for i in frase:
    a = i.count('a')
    if a == 1:
        a += 1
    print(a)

