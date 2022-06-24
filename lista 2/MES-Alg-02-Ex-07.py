# Centena, dezena, unidade.

numero = int(input('Digite um número de três algarismos:'))

n1 = numero // 100
centena = n1 * 100

n2 = numero % 100

dezena = (n2 // 10 )* 10
unidade = n2 % 10

print ('Valor da centena:', centena)
print ('Valor da dezena:', dezena)
print ('Valor da unidade:', unidade)