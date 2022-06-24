#Soma dos dígitos de um inteiro.

numero_4D = int(input('Digite um número inteiro de 4 dígitos:'))

D1 = numero_4D // 1000
v1 = numero_4D % 1000

D2 =  v1 // 100
v2 = v1 % 100

D3 = v2 // 10
v3 = v2 % 10

D4 = v3 

resultados = D1+D2+D3+D4
print ('Soma dos dígitos do número:', resultados)