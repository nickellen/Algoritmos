# Fatorial
def fatorial(x):
    if x==1:
        return x
    return x * fatorial(x-1)

numero = int(input('Informe um número para calcular o fatorial:'))
print(fatorial(numero))