# Bingo: verificando uma cartela vencedora
import random
def dicionário_bingo(sorteados):
    dicionario = {'B':'','I':'','N':'','G':'','O':''}
    inicio=1
    fim=16
    for chave in dicionario:
        lista= []
        while len(lista)<5:
            numero = random.randrange(inicio,fim)
            if numero not in lista:
                if numero in sorteados:
                    lista.append(0)
                else:
                    lista.append(numero)
        dicionario[chave]=lista
        inicio+=15
        fim+=15

    return dicionario

def cartela_bingo(dicionario):
    print('-----------------------------------')
    for chave in dicionario:
        print( chave,'\t', end='')
    print('\n-----------------------------------')

    for i in range(5):
        for chave in dicionario:
            print(dicionario[chave][i],'\t', end='')
        print()
    return ''

def cartela_vencedora(dicionario):
    conjunto = set()
    verdadeiro = {0,0,0,0,0}

    # verificar linhas
    for i in range(5):
        for chave in dicionario:
            conjunto.add(dicionario[chave][i])
        if conjunto.issubset(verdadeiro):
            return True
        conjunto.clear()
    
    # verificar colunas
    for chave in dicionario:
        for numero in dicionario[chave]:
            conjunto.add(numero)
        if conjunto.issubset(verdadeiro):
            return True
        conjunto.clear()

    # verificar diagonais
    i = 0
    for chave in dicionario:
        conjunto.add(dicionario[chave][i])
        i+=1
    if conjunto.issubset(verdadeiro):
        return True
    conjunto.clear()
    
    i = 4 
    for chave in dicionario:
        conjunto.add(dicionario[chave][i])
        i-=1
    if conjunto.issubset(verdadeiro):
        return True
    return False

def main():
    sorteados = set()
    while len(sorteados)<5:
        numero = random.randrange(1,76)
        if numero not in sorteados:
            sorteados.add(numero)
    
    cartela_diagonal = {'B': [7, 11, 12, 8, 0], 'I': [25, 27, 19, 0, 25], 'N': [40, 39, 0, 33, 44], 'G': [49, 0, 58, 48, 60], 'O': [0, 73, 63, 75, 62]}
    
    cartela_horizontal = {'B': [0, 11, 12, 8, 9], 'I': [0, 27, 19, 29, 25], 'N': [0, 40, 39, 33, 44], 'G': [0, 55, 58, 48, 60], 'O': [0, 73, 63, 75, 62]}
    
    cartela_vertical = {'B': [5, 9, 15, 10, 4], 'I': [0, 0, 0, 0, 0], 'N': [36, 38, 44, 33, 45], 'G': [50, 48, 56, 60, 51], 'O': [67, 64, 70, 75, 62]}
    
    cartela_aleatória = dicionário_bingo(sorteados)

    cartelas = [cartela_diagonal, cartela_horizontal ,cartela_vertical ,cartela_aleatória]

    for elemento in cartelas:
        if cartela_vencedora(elemento):
            print('CARTELA VENCEDORA:')
        else:
            print('CARTELA NÃO VENCEDORA:')
        print(cartela_bingo(elemento))
        
if __name__=="__main__":
    main()