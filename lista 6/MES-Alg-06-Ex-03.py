# Removendo extremos
def nova_copia(lista, n):
    for vezes in range(n):
        maior=lista[0]
        for numero in lista:
            if numero>maior:
                maior= numero
        lista.remove(maior)
    for vezes in range(n):
        menor=lista[0]
        for numero in lista:
            if numero<menor:
                menor= numero
        lista.remove(menor)
    return lista

def main():
    lista = []
    while True:
        numero= input('Informe um número(espaço para parar):')
        if numero=='':
            if len(lista)<=4:
                input('Erro: informe pelo menos 4 valores(enter para continuar):')
                continue
            else:
                break
        lista.append(int(numero))
    print('Nova lista:', nova_copia(lista.copy(), 2))
    print('Lista original:', lista)

if __name__=='__main__':
    main()
