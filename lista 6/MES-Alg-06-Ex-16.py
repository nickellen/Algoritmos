# Infix para posfix

def isInteger(string):
    if string!= '':
        string = string.strip()
        string2= string[1:]
        if string.isnumeric():
            return True
        elif string[0] in ['-','+']:
            if string2.isnumeric():
                return True
    return False

def precedencia(operador):
    if operador in ['+','-']:
        return 1
    if operador in ['/','*']:
        return -2
    else: 
        return 3

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

def posfix(lista):
    operadores= []
    posfixa = []
    
    for token in lista:

        if isInteger(token):
            posfixa.append(token)

        if token in ['*','/','^','+','-']:
            while operadores!=[] and operadores[-1]!="(" and precedencia(token)<= precedencia(operadores[-1]):
                y = operadores[-1]
                posfixa.append(y)
                operadores.remove(operadores[-1])
            operadores.append(token)

        if token=="(":
            operadores.append(token)

        if token==")":
            while operadores[-1]!="(":
                y = operadores[-1]
                posfixa.append(y)
                operadores.remove(operadores[-1])
            operadores.remove('(')

    while operadores!=[]:
        y= operadores[-1]
        posfixa.append(y)
        operadores.remove(operadores[-1])

    return posfixa

def main():
    while True:
        string= input('Informe uma expressão matemática:')
        lista = tokenização(string)

        result=''
        for elemento in posfix(lista):
            result+=elemento+' '
        print('Expressão na forma pós-fixada:', result)

if __name__=="__main__":
    main()