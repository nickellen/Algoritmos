# Números perfeitos
def divisores(n):
    lista= []
    for divisor in range(1,n):
        if n%divisor==0:
            lista.append(divisor)
    return lista

def numeros_perfeitos(n):
    soma= 0
    for numero in divisores(n):
        soma+=numero
    if soma==n:
        return True
    return False

def main():
    print('Número perfeitos de 1 a 10.000:')
    for numero in range(1,10001):
        if numeros_perfeitos(numero):
            print('-', numero)

if __name__=="__main__":
    main()
    
