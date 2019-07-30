
def lista_menor_10(lista):
    numero_user = int(input('Digite numero: '))
    for i in lista:
        if i < numero_user:
            out_lista = [];
            out_lista.append(i)
    return(out_lista)



if __name__ == "__main__":
    A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(lista_menor_10(A))

