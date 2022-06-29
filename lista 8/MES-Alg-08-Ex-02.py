# Sequencia de Fibonacci
def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

numero = int(input('Informe um valor:'))
print(fibonacci(numero))