# Cartela de bingo
import random
def dicionario_bingo():
    dicionario = {'B':'','I':'','N':'','G':'','O':''}
    inicio =1
    fim =16
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

def main():
    print('CARTELA DE BINGO:')
    print(cartela_bingo(dicionario_bingo()))

if __name__=="__main__":
    main()