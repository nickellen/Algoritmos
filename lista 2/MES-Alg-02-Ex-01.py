# Unidades de tempo.

dias = int(input('Digite o número de dias:'))
h =  int(input('Digite o número de horas:'))
min = int(input('Digite o número de minutos:'))
s = int(input('Digite o número de segundos:'))

s1= (3600 * 24 ) * dias
s2= 3600 * h
s3 = 60 * min

total = s1 + s2+ s3 + s

print ('Quantidade total de segundos:', total, 'segundos')