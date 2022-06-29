#Fibonacci com memorização de resultado
memoria ={0:0,1:1}
def fibonacci2(x):
    if x in memoria:
        return memoria[x]
    valor = fibonacci2(x-1) + fibonacci2(x-2)
    memoria[x]=valor
    return valor

numero = int(input('Informe um valor:'))
print(fibonacci2(numero))