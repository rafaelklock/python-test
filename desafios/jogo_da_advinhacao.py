import random


def main():
    numero_randomico = random.randrange(1, 101)
    numero_escolhido = ''
    contador = 0
    while numero_escolhido != 'sair':
        contador += 1
        numero_escolhido = input('Chute um numero: ')
        if numero_escolhido == 'sair':
            exit()

        if int(numero_escolhido) == numero_randomico:
            print(f'Acertou, depois de {contador}')
            exit()
        elif int(numero_escolhido) > numero_randomico:
            print('o numero esta muito alto')
        else:
            print('o numero esta muito baixo')



if __name__ == '__main__':
    print('estou rodando')
    main()


