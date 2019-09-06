# CALCULADORA Python
# Rafael Klock
def soma(a,b):          print(f"\n --> resultado da soma: {float(a) + float(b)}\n")
def subtracao(a,b):     print(f"resultado da sub: {a - b}")
def divisao(a,b):       print(f"resultado da div: {a / b}")
def multiplicacao(a,b): print(f"resultado da mult: {a * b}")

def divisor(a,b):
    if (int(a) % int(b)) == 0 :
        print(f"\n --> {b} é divisor de {a}")
    else: 
        print(f"\n --> {b} não é divisor de {a}")


valor_input = input('\nBem vindo a calculadora!\n\nInforme sua equaçao: ')

if '+' in valor_input:
    valores = valor_input.split('+')
    operacao = '+'
    valor_a = valores[0]
    valor_b = valores[1]
    soma(valor_a,valor_b)

if '%' in valor_input:
    valores = valor_input.split('%')
    operacao = '%'
    valor_a = valores[0]
    valor_b = valores[1]
    divisor(valor_a,valor_b)


