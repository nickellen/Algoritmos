# Conversão decimal para binário recursiva
def conversão(q):
    if q in {1,0}:
        return str(q)
    return conversão(q//2) + str(q%2)

numero = int(input('Informe um valor decimal para conversão binária:'))
print(conversão(numero))