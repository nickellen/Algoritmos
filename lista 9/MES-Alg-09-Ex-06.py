# Encontrar a palavra mais longa de um arquivo

arquivo = input('Informe o caminho do arquivo: ')
with open(arquivo, "r") as arquivo:
    lista = []
    palavras = arquivo.read().split()
    maior = palavras[0]

    for palavra in palavras:
        if len(palavra) > len(maior):
            maior = palavra
        elif len(palavra)==len(maior):
            lista.append(palavra)
    lista.append(maior)

    print(f'Tamanho da maior palavra: {len(maior)} caracteres\n')
    
    print('Todas as palavras do arquivo com esse tamanho:')

    for elemento in lista:
        if len(maior) == len(elemento):
            print(elemento)

    arquivo.close()