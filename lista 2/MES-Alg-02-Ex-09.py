# Data invertida.

data = int(input('Digite a data no formato DDMMAA:'))

DD = data // 10000

v1 = data % 10000
MM = ( v1 // 100) * 100

AA = ( v1 % 100) * 10000

resultado = DD + MM + AA

print ('Data no formato AAMMDD:', resultado)