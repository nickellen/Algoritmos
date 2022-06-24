#DECIMAL PARA BINÁRIOS
numero = int(input('Informe um número decimal:'))
resultado = ""
while numero!=0:
    resto = numero%2
    resultado= str(resto)+ resultado
    numero =int(numero/2)

print('Número binário calculado:',resultado)