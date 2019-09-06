def calc_ano_bisexto(ano):
        result = int(ano) % 4
        if result == '0':
            return result


if __name__ == '__main__':
    year = input('insert year: ')
    print(calc_ano_bisexto(year))

