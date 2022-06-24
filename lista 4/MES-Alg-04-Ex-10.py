#Palíndromo
palavra = input('Informe uma palavra:')
tamanho = len(palavra)
i=0
y = (-1)
while i< tamanho:
    if palavra[i]!= palavra[y]:
        print('Não é palíndromo')
        break
    i+=1
    y-=1
else: 
    print('É palíndromo')