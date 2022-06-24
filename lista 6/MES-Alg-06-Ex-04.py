# Evitando duplicatas
lista = []
while True:
    palavra = input('Digite uma palavra (enter para parar):')
    if palavra in lista:
        continue
    if palavra== '':
        break
    lista.append(palavra)

for palavra in lista:
    print(palavra)