# 'Tokenizacao' de strings
def tokenização(string):
    string = string.strip()
    tokens=[]
    numero='' 
    sinal =True

    for x in string:

        if x in ['+','-']:
            if sinal and numero=='':
                numero+=x
                sinal=False
            else:
                if numero!='':
                    tokens.append(numero)
                    numero=''
                tokens.append(x)
                sinal=True

        elif x in ['*','/','(',')','^']:
            if numero!="":
                tokens.append(numero)
                numero=''
            tokens.append(x)
            sinal=True
            if x==")":
                sinal=False
                
        else: 
            numero+=x
            sinal=False
    if numero!="":
        tokens.append(numero)
    return tokens

def main():
    while True:
        string= input('Informe uma expressão matemática:')
        print('Lista de tokens correspondente:', tokenização(string))
        
if __name__=='__main__':
    main()