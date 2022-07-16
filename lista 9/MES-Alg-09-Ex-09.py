# Remoção de comentários
import sys

fonte = input('Informe o caminho do arquivo de entrada:')
destino = input('Informe o caminho do arquivo de saída:')

try:
    with open(fonte, 'r') as fonte, open(destino, 'w') as destino:
        for line in fonte:

            words = line.split()
            lista= line.split('#')
            print(lista)
            i=0

            for word in words:
                if word[0] == '#' or word =='#':
                    destino.write(lista[0])
                    i=1
                    if lista[0]!='':
                        destino.write('\n')
                    break

            if i==0:
                destino.write(line)

        fonte.close()
        destino.close()

except FileNotFoundError:
    print("Arquivo não encontrado!")

except IOError:
    print('Erro de entrada e saída!')