# Nome do mês e número de dias.
mes = str(input('Informe o nome do mês:'))

if (mes== 'janeiro') or (mes=='março') or (mes=='maio') or (mes=='julho') or (mes=='agosto') or (mes=='outubro') or (mes=='dezembro'):
    print('31 dias')
elif (mes=='abril') or (mes=='junho') or (mes=='setembro') or (mes=='novebro'):
    print('30 dias')
elif (mes=='fevereiro'):
    print('28 ou 29 dias')
else:
    print('ERRO')