# Busca reversa
def buscaReversa(dicionario, valor):
    lista =[]
    for chave in dicionario:
        if dicionario[chave]== valor:
            lista.append(chave)
    return lista

def main():
    dicionario = {}
    while True:
        chave = input('Informe uma chave:(enter para parar):')
        if chave=='':
            break
        valor = input('Informe um valor:')
        dicionario[chave]= valor

    valor = input('Informe um valor para ser buscado no dicionário:')
    print('LISTA DAS CHAVES ENCONTRADAS:', buscaReversa(dicionario,valor))

if __name__=='__main__':
    main()