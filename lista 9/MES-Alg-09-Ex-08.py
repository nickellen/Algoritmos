# Frequência de palavras
import sys

set = {}
simbolos =[',','!','?',';',':','.','-',
            '(',')','[',']','{','}','<','>',
            '=','+','*','%','$','#','@','&',
            '^','~','`','|','\'',
            '1','2','3','4','5','6','7','8','9','0']

try:
    with open(sys.argv[1], "r") as arquivo:

        for line in arquivo:
            for word in line.split():

                for simbolo in simbolos:
                    word = word.replace(simbolo, '').lower()

                if word!='':
                    if word in set:
                        set[word] += 1
                    else:
                        set[word] = 1
        
        for key in set.keys():
            maior = set[key]
            break
        
        for key, valor in set.items():
            if valor > maior:
                maior = valor
                maior_palavra = key
        try:
            print(f'Palavra que aparece com maior frequência:\n{maior_palavra} - {maior} vezes')
        except NameError:
            print('Nenhuma palavra aparece com maior frequência!')
        arquivo.close()

except FileNotFoundError:
    print('Arquivo não encontrado!')