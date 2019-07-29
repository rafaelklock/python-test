salario = int(input('salario: '))
imposto = input('Imposto em %: ')

if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)

taxa =          (imposto * 0.01)
salario_real =  (salario - (salario * taxa))


if imposto < 10. :
    valor_imposto = "Baixo"
elif imposto >= 10. and taxa <= 27. :
    valor_imposto = "Médio"
elif imposto > 27. :
    valor_imposto = "Alto"
else:
    print("Imposto inválido")


print("Salario líquido:",salario_real)
print("Imposto:",taxa)
print("Seu imposto está:",valor_imposto)