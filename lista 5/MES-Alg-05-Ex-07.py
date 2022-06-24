#Triângulo válido?
def triangulo_valido(x,y,z):
    if (x>= y+z) or (y>= x+z) or (z>= y+x):
        return False
    return True

def main():
    valor1 = int(input('Informe um valor:'))
    valor2 = int(input('Informe um valor:'))
    valor3 = int(input('Informe um valor:'))
    if triangulo_valido(valor1, valor2, valor3):
        print('É possível formar um triângulo')
    else:
        print('Não é possível formar um triângulo')

if __name__=='__main__':
    main()