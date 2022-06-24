# Conversão arbitrára de base numérica
def int2arb(x, base):
    numero = ""
    hexadecimal= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while True:
        resto = x%base
        numero= hexadecimal[resto] + numero
        x = x//base
        if x==0:
            break
    return numero

def arb2int(x, base):
    hexadecimal= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    x = x.upper()
    x = x[::-1]
    soma = 0
    i=0
    for numero in x:
        novo_numero = hexadecimal.index(numero) * (base** i)
        soma= soma+ novo_numero
        i+=1
    return soma

def main():
    while True:
        numero = input('Informe o número a ser convertido:')
        base_inicial = int(input('Informe a base do número (2, 8, 10, 16):'))
        base_final = int(input('Informe a base para converter o número (2, 8, 10, 16):'))

        if base_inicial!=10 and base_final!=10:
            decimal = arb2int(numero,base_inicial)
            print(int2arb((decimal),base_final))

        elif base_inicial==10:
            print(int2arb(int(numero),base_final))

        else:
            print(arb2int(numero,base_inicial))
        
if __name__=="__main__":
    main()