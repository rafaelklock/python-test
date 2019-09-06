from decimal import Decimal

total = Decimal('0')

def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal('0')

if __name__ == '__main__':
    with open('../banco/data/data/ExecucaoFinanceira.csv', 'r') as data:
        splited_data = [ line.split(';') for line in data ]
        total = sum([dec(element, 5) for element in splited_data])


    print("total: {}".format(total))

