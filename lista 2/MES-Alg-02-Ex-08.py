# Centena, dezena, unidade (novamente). 

numero = int(input('Digite um número de três algarismos:'))

centena = numero // 100

n1 = numero % 100

dezena = (n1 // 10 )* 10

unidade = (n1 % 10) * 100

resultado = centena + dezena + unidade

print ('N=', numero)
print ('M=', resultado)