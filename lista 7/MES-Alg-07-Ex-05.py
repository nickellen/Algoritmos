# Anagramas
def anagrama(p0,p1):
    dic0={}
    dic1={}
    for elemento in p0:
        if elemento in dic0:
            dic0[elemento]+=1
        else:
            dic0[elemento]=1

    for elemento in p1:
        if elemento in dic1:
            dic1[elemento]+=1
        else:
            dic1[elemento]=1
    
    if dic0==dic1:
        return True
    return False

def main():
    while True:
        palavra0 = input('Informe a primeira palavra:')
        palavra1 = input('Informe a segunda palavra:')
        if anagrama(palavra0,palavra1):
            print('É um anagrama!')
        else:
            print('Não é um anagrama!')

if __name__=="__main__":
    main()