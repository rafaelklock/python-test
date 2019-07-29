import os
import time

clear = lambda: os.system('clear')
salario = int(input('\nSalario: '))
imposto = 27.

while imposto > 0.:
    clear()
    imposto = input('\n\nImposto: ou (0) para sair: ')

    if not imposto:
            imposto = 27.
    elif imposto == 's':
        clear()
        print("xau")
        break
    else:
            imposto = float(imposto)
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
    time.sleep(1)


        