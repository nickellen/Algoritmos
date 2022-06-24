#Média aritmética
x = 0
n=0
valor = float(input('Informe um valor(0 para parar):'))

while valor!=0:
    x = x + valor
    n = n+1
    valor = float(input('Informe um valor(0 para parar):'))
    if valor==0:
        media = x/n
        print('Média:', media)
        break
else:
    print('Erro: o primeiro valor fornecido não deve ser 0.')