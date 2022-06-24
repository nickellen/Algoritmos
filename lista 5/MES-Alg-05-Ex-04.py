# Mediana de três valores:
def mediana(x,y,z):
    return (x+y+z) - min(x,y,z)- max(x,y,z)

def main():
    lista= []
    for i in range(0,3):
        valor= int(input('Informe um valor:'))
        lista.append(valor)
    print('O valor da mediana é:', mediana(lista[0], lista[1], lista[2]))

if __name__=="__main__":
    main()