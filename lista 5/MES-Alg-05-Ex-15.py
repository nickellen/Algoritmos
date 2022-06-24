# Dígitos hexadecimais e decimais
def hex2int(x):
    x = x.upper()
    hexadecimal= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if x not in hexadecimal:
        return False
    return hexadecimal.index(x)

def int2hex(x):
    x = int(x)
    hexadecimal= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if x>=len(hexadecimal):
        return False
    return hexadecimal[x]
    
def main():
    while True:
        numero= input('Digite um número decimal para obter sua representação em hexadecimal ou vice versa:')
        if numero.isnumeric():
            if int2hex(numero)==False:
                print('Informe um número de 0 a 15!')
            else:
                print(f'O número decimal {numero} equivale a {int2hex(numero)} em hexadecimal')
            print('\n') 
        else:
            if hex2int(numero)==False:
                print('Esse símbolo não pertence ao sistema hexadecimal!')
            else:
                print(f'O número hexadecimal {numero} equivale a {hex2int(numero)} em decimal')
            print('\n')

if __name__=="__main__":
    main()