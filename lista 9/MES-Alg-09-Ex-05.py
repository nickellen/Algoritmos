# Numerar as linhas de um arquivo

fonte = input('Informe o arquivo de entrada: ')
destino = input('Informe o arquivo de saída: ')

with open(fonte, "r") as fonte, open(destino, "w") as destino:
    i = 1
    while True:
        linha = fonte.readline()
        if not linha: 
            break
        destino.write(f'{i}: {linha}')
        i += 1

fonte.close()
destino.close()