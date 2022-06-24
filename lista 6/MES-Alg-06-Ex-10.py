# Formatando uma lista
def formatando_lista(lista):
    novo_texto=''
    comp = len(lista)
    for i in range(0,comp):
        if i==comp-2:
            novo_texto+=lista[i]+' e '
        elif i==comp-1:
            novo_texto+=lista[i]
        else:
            novo_texto+= lista[i] + ', '
    return novo_texto

def main():
    lista = []
    while True:
        string= input('Digite uma palavra (enter para parar):')
        if string!='':
            lista.append(string)
        else:
            break
    print('Lista formatada:', formatando_lista(lista))

if __name__=="__main__":
    main()