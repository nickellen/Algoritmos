# Conversão decimal para binário iterativa
def conversão(q):
    result=''
    while q!=0:
        r= q%2
        result = str(r)+ result
        q=q//2
    return result

numero = int(input('Informe um valor decimal para conversão binária:'))
print(conversão(numero))