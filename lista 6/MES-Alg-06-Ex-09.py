# Abaixo e acima da média
lista= []
while True:
    numero= input('Digite um número(enter para parar):')
    if numero=='':
        break
    lista.append(numero)

soma=0
for numero in lista:
    soma+=int(numero)
media= soma//len(lista)
print('Média dos números fornecidos:', media)

l0=''
l1=''
l2=''
for numero in lista:
    numero=int(numero)
    if numero<media:
        l0+=str(numero)+' '
    elif numero==(media):
        l1+=str(numero)+' '
    else:
        l2+=str(numero)+' '

print('Valores abaixo da media:', l0)
print('Valores médios:', l1)
print('Valores acima da média:', l2)