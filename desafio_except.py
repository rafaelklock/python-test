

def divisao():
    try:
        v_a = int(input())
        v_b = int(input())
        resultado = v_a / v_b
        print(f"\nResultado:", resultado)

    except ZeroDivisionError:
        print("Nao pode dividir um numero por zero amigo")

    except ValueError:
        print('ValueError em Python!!!')

    finally:
        print("Final")


divisao()

