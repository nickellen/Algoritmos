# MDC - Máximo Divisor Comum
def MDC(a,b):
    if b==0:
        return a
    return MDC(b,a%b)

n0 = int(input('Informe o primero número inteiro:'))
n1= int(input('Informe o segundo número inteiro:'))
print(f'Máximo dividor comum de {n0} e {n1}: {MDC(n0,n1)}')