# Jogo de bingo
import random
def dicionário_bingo():
    dicionario = {'B':'','I':'','N':'','G':'','O':''}
    inicio=1
    fim=16
    for chave in dicionario:
        lista= []
        while len(lista)<5:
            numero = random.randrange(inicio,fim)
            if numero not in lista:
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
    # verificar linhas
    conjunto = set()
    verdadeiro = {0,0,0,0,0}
    
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

def zerar_cartela(cartela,sorteados):
    for chave in cartela:
        lista = cartela[chave]

        for elemento in lista:
            if elemento in sorteados:
                index = lista.index(elemento)
                lista.pop(index)
                lista.insert(index, 0)

    return cartela_vencedora(cartela)

def main():
    media = 0
    minimo = 76
    maximo = 1
    for partidas in range(1,1001): 
        chamadas = 0
        lista=[]

        for chamada in range(1,76):
            lista.append(chamada)
        random.shuffle(lista)

        cartela= dicionário_bingo()
        sorteados = set()

        for elemento in lista:
            sorteados.add(elemento)
            chamadas+=1
            if zerar_cartela(cartela,sorteados):

                if chamadas < minimo:
                    minimo = chamadas
                elif chamadas > maximo:
                    maximo = chamadas

                media+=chamadas
                break
        
    media = media//partidas
    print('Quantidade de chamadas para uma cartela vencedora (simulação de 1000 partidas):')
    print(f'Mínimo: {minimo}\nMédia: {media}\nMáximo: {maximo}')

if __name__=="__main__":
    main()