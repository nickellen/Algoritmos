# Anagramas novamente
import string
def anagramas(frase0,frase1):
    dic0={}
    dic1={}
    for elemento in frase0.upper():
        if elemento in string.punctuation or elemento==' ':
            continue
        else:
            if elemento in dic0:
                dic0[elemento]+=1
            else:
                dic0[elemento]=1

    for elemento in frase1.upper():
        if elemento in string.punctuation or elemento==' ':
            continue
        else:
            if elemento in dic1:
                dic1[elemento]+=1
            else:
                dic1[elemento]=1

    if dic0==dic1:
        return True
    return False

def main():
    while True:
        frase0 = input('Informe a primeira frase:')
        frase1 = input('Informe a segunda frase:')
        if anagramas(frase0,frase1):
            print('É um anagrama!')
        else:
            print('Não é um anagrama!')

if __name__=="__main__":
    main()