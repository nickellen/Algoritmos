# Palíndromo
import string
def palindromo(texto):
    return len(texto)<=1 or texto[0]==texto[-1] and palindromo(texto[1:-1])

def remove(texto):
    if texto=='':
        return texto
    elif texto[0] in string.punctuation or texto[0]==" ":
        return remove(texto[1:])
    return texto[0]+ remove(texto[1:])

def main():
    texto = input('Informe uma palavra ou frase:')
    if palindromo(remove(texto)):
        print('É palíndromo!')
    else:
        print('Não é palíndromo!')

if __name__=='__main__':
    main()