# Contagem de elementos
def countRange(lista,min,max):
    x= []
    for numero in lista:
        if numero>=min and numero<max:
            x.append(numero)
    return len(x)

def main():
    lista=[]
    while True:
        numero= input('Informe um número para adicionar na lista (enter para parar):')
        if numero=='':
            break
        lista.append(int(numero))
    minimo = int(input('Informe qual será o valor mínimo:'))
    maximo = int(input('Informe qual será o valor maximo:'))
    
    print('Quantidade de elementos na lista maiores/iguais que o valor mínimo e menores que o valor máximo:\n', countRange(lista,minimo,maximo))

if __name__=="__main__":
    main()