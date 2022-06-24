#Níveis de barulho
volume = int(input('Informe um nível de volume em decibéis:'))

if volume== 130:
    print('Barulho de uma britadeira')
elif volume>130:
    print ('Barulho maior que o de uma britadeira')
elif volume>106<130:
    print('Nível de volume entre o barulho de uma britadeira e cortador de grama')
elif volume== 106:
    print('Barulho de um cortador de grama')
elif volume>70<106:
    print('Nível de volume entre o barulho de um cortador de grama e despertador')
elif volume== 70:
    print('Barulho de um despertador')
elif volume >40<70:
    print('Nível de volume entre o barulho de um despertador e uma sala silenciosa')
elif volume== 40:
    print('Barulho de uma sala silenciosa')
else:
    print('Barulho menor que o de uma sala silenciosa')