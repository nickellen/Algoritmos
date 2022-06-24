# A lista está ordenada?
def lista_ordenada(lista):
    lista_crescente = sorted(lista)
    lista_decrescente = sorted(lista, reverse=True)
    if lista_crescente==lista or lista_decrescente==lista:
        return True
    else:
        return False

def main():
    lista=[]
    while True:
        numero = input('Informe um número(enter para continuar):')
        if numero=='':
            break
        lista.append(int(numero))

    if lista_ordenada(lista):
        print('\nA lista já está em ordem de classificação.')
    else:
        print('\nA lista ainda não está em ordem de classificação.')

if __name__=='__main__':
    main()