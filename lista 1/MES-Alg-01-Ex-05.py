# Cálculo de retorno de recicláveis
quantidade1 = int(input('Quantidade de vasilhames de um litro ou menos:'))
quantidade2 = int(input('Quantidade de vasilhames de mais de um litro:'))

tipo1 = 0.10 * quantidade1
tipo2 = 0.25 * quantidade2

total = tipo1 + tipo2

print (f'Valor total de crédito: R${total:,.2f}')