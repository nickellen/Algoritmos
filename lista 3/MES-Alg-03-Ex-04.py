# Polígono regular.
lados = int(input('Digite a quantidade de lados de um polígono regular:'))

if lados==3:
    print('Triângulo equilátero')
elif lados== 4:
    print('Quadrado')
elif lados== 5:
        print('Pentágono regular')
elif lados== 6:
    print('Hexágono regular')
elif lados== 7:
    print('Heptágono regular')
elif lados== 8:
        print('Octógono regular')
elif lados== 9:
    print('Eneágono regular')
elif lados== 10:
        print('Decágono regular')
else:
    print('ERRO: Valor deve ser de 3 a 10 lados')