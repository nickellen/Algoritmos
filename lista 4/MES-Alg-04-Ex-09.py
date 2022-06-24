#Raiz quadrada
x = float(input('Informe o valor:'))
raiz = x/2

while abs((raiz*raiz)-x)> 1e-12:
    raiz = (raiz+(x/raiz))/2
else:
    print('Valor da raiz quadrada:', raiz)