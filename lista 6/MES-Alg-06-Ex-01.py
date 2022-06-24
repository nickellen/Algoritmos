# Ordem crescente
lista = []
while True:
    numero = int(input('Informe um número(0 para parar):'))
    if numero ==0:
        break
    lista.append(numero)

lista.sort()
print('Números em ordem crescente:')
for numero in lista:
    print(numero)