#Cor da casa do tabuleiro
posiçao = input('Informe uma posição:')

coluna = posiçao[0]
linha = int(posiçao[1])
par = linha%2

if coluna== 'a' or coluna== 'c' or coluna=='e' or coluna=='g':
    if par== 0:
        print('Quadrado branco')
    else:
        print('Quadrado preto')

elif coluna== 'b' or coluna=='d' or coluna=='f' or coluna=='h':
    if par== 0:
        print('Quadrado preto')
    else:
        print('Quadrado branco')