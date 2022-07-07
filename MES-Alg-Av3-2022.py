# Aluno: Monique Ellen dos Santos

# ------------------------ QUESTAO 1 -----------------------------------
def conversao(string):
    notas = {'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}
    if string in notas:
        return notas[string]
    return -1

def main():
    while True:
        nota_conceito = input('Informe uma nota-conceito:')
        if conversao(nota_conceito.upper())==-1:
            print('Nota-conceito inválida!')
        else:
            print('Valor numérico:', conversao(nota_conceito.upper()))

if __name__=="__main__":
    main()

# ------------------------ QUESTAO 2 -----------------------------------
def conversao(string):
    notas = {'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}
    if string in notas: return notas[string]

def main():
    while True:
        soma = 0
        media= 0
        while True:

            try:
                nota = input('Informe uma nota:')
                if nota=="" and soma!=0:
                    break
                soma+= conversao(nota.upper())
                media+=1

            except TypeError:
                print('Nota inválida!')

        print('Média das notas:', soma/media)

if __name__=="__main__":
    main()

# ------------------------ QUESTAO 3 -----------------------------------
def prox_num_primo(n):
    n = n+1
    for i in range(2,n):
        if n%i==0:
            n+=1
    return n

def main():
    while True:
        try:
            numero = int(input('Informe um número inteiro positivo:'))
            if numero<=0:
                continue
            print(f'Próximo número primo maior que {numero}: {prox_num_primo(numero)}')

        except ValueError:
            continue

if __name__=="__main__":
    main()

# ------------------------ QUESTAO 4 -----------------------------------
import random

def criaBaralho():
    lista =[]
    for valor in ['A','2','3','4','5','6','7','8','9','D','J','Q','K']:
        for naipe in ['s','c','o','p']:
            lista.append(valor+naipe)
    return lista

def embaralha(lista):
    for i, elemento in enumerate(lista):
        i2 = random.randint(0,51)
        elemento2 = lista[i2]

        lista.insert(i,elemento2)
        lista.remove(elemento2)

        lista.insert(i2,elemento)
        lista.remove(elemento)

    return lista
    
def main():
    baralho = criaBaralho()
    print('Baralho:\n', baralho)
    print('Baralho embaralhado:\n', embaralha(baralho))

if __name__=="__main__":
    main()
