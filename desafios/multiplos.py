
def soma_dos_multiplos(valor):
    soma = 0
    for i in range(valor):
        if (i % 5 == 0) or (i % 3 == 0):
            soma = int(i) + int(soma)
            print(i)
    print('resultado soma:', soma)


soma_dos_multiplos(10)
