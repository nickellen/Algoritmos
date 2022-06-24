#Ano bissexto
ano = int(input('Informe ano:'))

if ano%400 == 0:
    print('Ano bissexto')
elif ano%100 == 0:
    print('Não é ano bissexto')
elif ano%4 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')