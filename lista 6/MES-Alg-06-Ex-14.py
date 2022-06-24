# Precedência de operadores
def precedencia(operador):
    if operador in ['+','-']:
        return 1
    if operador in ['/','*']:
        return -2
    else: 
        return 3
        
def main():
    while True:
        operador= input('Informe um operador matemático:')
        if operador not in ['+','-','/','*','^']:
            input('Erro: Por favor insira um operador matemático (enter para continuar):')
            continue
        else:
            print(precedencia(operador))

if __name__=='__main__':
    main()