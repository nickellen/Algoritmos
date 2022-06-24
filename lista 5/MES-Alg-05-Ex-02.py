#Tarifa do taxi
valor_inicial = 4
valor_variavel = 0.25
metros = 140
def tarifa(x):
    x = x*1000
    n = x //metros
    x = valor_variavel*n + valor_inicial
    return x

def main():
    distancia = float(input('Informe a distância percorrida em quilômetros:'))
    print('O valor total da corrida é de: R$', format(tarifa(distancia), '.2f'))

if __name__== '__main__':
    main()