#Data de feriado
dia = int(input('Informe o dia:'))
mes = str(input('Informe o mês:'))

if dia== 1 and mes== 'janeiro':
    print('Feriado de Confraternização universal')
elif dia== 21 and mes== 'abril':
    print('Feriado de Tiradentes')
elif dia== 1 and mes== 'maio':
    print('Feriado de Dia do trabalho')
elif dia==7  and mes== 'setembro':
    print('Feriado de Idependência do Brasil')
elif dia==12  and mes== 'outubro':
    print('Feriado de Nossa Senhora Aparecida')
elif dia==2  and mes== 'novembro':
    print('Feriado de Finados')
elif dia==15  and mes== 'novembro':
    print('Feriado de Proclamação da República')
elif dia==25  and mes== 'dezembro':
    print('Feriado de Natal')
else:
    print('O dia e mês informados não correspondem a um feriado nacional')