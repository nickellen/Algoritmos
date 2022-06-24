# Unidades de tempo (novamente).

s = int(input('Digite uma quantidade de tempo em segundos:'))

minutos = s // 60
horas = minutos // 60
dias = horas // 24

HH = horas % 24
MM = minutos % 60
SS = s % 60

print ('Tempo equivalente em D:HH:MM:SS')
print (dias,":", "{:02d}".format(HH), ":", "{:02d}".format(MM), ':', "{:02d}".format(SS))