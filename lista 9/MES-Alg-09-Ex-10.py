# Um livro sem "e"
import sys

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇ'
set = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,'Ç':0}

try:
    with open(sys.argv[1], "r", encoding='utf 8') as arquivo:
        for line in arquivo:
            linha = line.split()
            for word in linha:
                for simbolo in alfabeto:
                    if simbolo in word.upper():
                        set[simbolo]+=1

        print('Letra - Quantidade de palavras com a letra')
        
        lista = []
        menor = min(set.values())
        for key in set.keys():
            if set[key]==menor:
                lista.append(key)


        for key, valor in set.items():
            print(f'{key} - {valor}    ', end='')

        
        print('\nLetra(s) menos usada(s):', ' - '.join(lista))
        arquivo.close()

except FileNotFoundError:
    print('Arquivo não encontrado!')