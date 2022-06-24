# Hipotenusa
from math import sqrt
def hipotenusa(x,y):
    hipotenusa= sqrt((x**2) + (y**2))
    return hipotenusa

def main():
    comp1 = float(input('Informe o comprimento do cateto oposto:'))
    comp2 = float(input('Informe o comprimento do cateto adjacente:'))
    print("Comprimento da hipotenusa:", hipotenusa(comp1, comp2))

if __name__=="__main__":
    main()