# Avaliação de expressão pós-fixada

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
                op = operadores[-1]
                posfixa.append(op)
                operadores.remove(operadores[-1])
            operadores.append(token)

        if token=="(":
            operadores.append(token)

        if token==")":
            while operadores[-1]!="(":
                op = operadores[-1]
                posfixa.append(op)
                operadores.remove(operadores[-1])
            operadores.remove('(')

    while operadores!=[]:
        op= operadores[-1]
        posfixa.append(op)
        operadores.remove(operadores[-1])
    return posfixa

def avaliação(posfix):
    valores=[]
    for token in posfix:
        if isInteger(token):
            valores.append(int(token))
        else:
            direita = valores[-1]
            valores.remove(valores[-1])
            esquerda = valores[-1]
            valores.remove(valores[-1])
            if token=='-':
                valores.append(esquerda - direita)
            elif token=='+':
                valores.append(esquerda + direita)
            elif token=='*':
                valores.append(esquerda * direita)
            elif token=='/':
                valores.append(esquerda / direita)
            elif token=='^':
                valores.append(esquerda ** direita)
    return valores[0]

def main():
    while True:
        string= input('Informe uma expressão matemática:')
        lista = posfix(tokenização(string))
        print('Valor da expressão:', avaliação(lista))

if __name__=='__main__':
    main()