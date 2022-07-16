# Frequência de letras
import sys

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇ'
set = {}

try:
    with open(sys.argv[1], "r") as arquivo:
        texto = arquivo.read()

        for letra in alfabeto:
            numero = texto.count(letra.lower())
            set[letra] = numero

        print('LETRAS\tFREQUENCIA')
        for key, valor in set.items():
            if valor!=0:
                print(f'{key}\t{valor%100}%')
        
        arquivo.close()

except FileNotFoundError:
    print('Arquivo não encontrado!')