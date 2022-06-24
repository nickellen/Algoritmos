#Valor das entradas
valor=0
while True:
    idade=input('Informe a idade:')
    if not idade:
        break
    else:
        idade=int(idade)
        if idade<3:
            valor+=0
        elif idade<13 and idade>2:
            valor+= 14
        elif idade>64:
            valor+=18
        else:
            valor+=23

print(f'Valor das entradas:R${valor:.2f}')