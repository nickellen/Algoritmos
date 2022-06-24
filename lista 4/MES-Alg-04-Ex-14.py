#BINARIO PARA DECIMAL
x = 0
base2 = str(input('Informe um número binário:'))
total = 0 
base2 = base2[: :-1]

for bit in base2:
    numero = (2**x) * int(bit)
    x+=1
    total = total+numero

print('Número decimal calculado:', total)