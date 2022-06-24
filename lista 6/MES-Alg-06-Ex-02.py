# Ordem decrescente
lista = []
while True:
    numero = int(input('Informe um número(0 para parar):'))
    if numero ==0:
        break
    lista.append(numero)

lista.sort(reverse=True)
print('Números em ordem descrescente:')
for x in lista:
    print(x)