# Negativos, zeros e positivos
lista = []
while True:
    numero = input('Digite um número(enter para parar):')
    if numero=='':
        break
    lista.append(int(numero))

negativos= ''
zeros = ''
positivos= ''
for numero in lista:
    if numero<0:
        negativos+= str(numero)+ ' '
for numero in lista:
    if numero==0:
        zeros+= str(numero) +' '
for numero in lista:
    if numero>0:
       positivos+= str(numero)+ ' '

print(f'Negativos: {negativos}\nZeros: {zeros}\nPositivos: {positivos}')