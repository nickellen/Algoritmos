#Tabela de descontos
print('Preço original:\t\tValor do desconto:\tPreço com desconto:')
valor=4.95
while valor<25:
    desconto = valor**0.6
    total = valor- desconto
    print(f'{valor}\t\t\t{desconto:.2f}\t\t\t{total:.2f}')
    valor+= 5