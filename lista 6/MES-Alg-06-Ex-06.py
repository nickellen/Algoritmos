# Lista de divisores
def divisores(n):
    lista= []
    for numero in range(1,n):
        if n%numero==0:
            lista.append(numero)
    return lista

def main():
    while True:
        numero = int(input('Digite um número:'))
        print(f'Divisores de {numero}: {divisores(numero)}')

if __name__=="__main__":
    main()