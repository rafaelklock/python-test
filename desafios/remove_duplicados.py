
def remove_numeros_duplicados(arquivo1, arquivo2):
    pass

def abre_arquivo(arquivo):
    dados_arquivo = open(arquivo, 'r')
    return dados_arquivo.read()


if __name__ == '__main__':
    print('#### inicio ####')
    # abrir arquivos baixados com open()
    arquivo_aberto = abre_arquivo('primenumbers.txt').split('\n')

