#FATORAÇÃO NUMÉRICA
numero = int(input('Digite um número inteiro (maior ou igual a 2):'))
fator=2
if numero<2:
    print('erro')
while numero>2:
    while fator<=numero:
        if numero%fator==0:
            print(fator)
            numero = numero/fator
        else:
            fator= fator+1