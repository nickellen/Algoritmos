# Corretor ortográfico
def texto_palavras(texto):
    lista = []
    palavra =''
    for caractere in texto:
        if caractere in ["!",".","?",",", " ","-","/"]:
            if palavra!="":
                lista.append(palavra)
                palavra = ''
        else:
            palavra+= caractere
    if palavra!='':
        lista.append(palavra)
    return ' '.join(lista)

def erros(arquivo):

    
    print('ERROS ORTOGRÁFICOS:')
    for linha in arquivo:
        linha = linha.split()
        for palavra in linha:
            palavra = texto_palavras(palavra)
            palavra = palavra.lower()
            if palavra not in conjunto:
                print(palavra)
    return ''

def main():
    import sys

    try:
        arquivo = open(sys.argv[1], 'r', encoding= 'utf 8')
        erros(arquivo)

    except UnicodeDecodeError:
        arquivo = open(sys.argv[1], 'r', encoding= 'utf 16')
        erros(arquivo)
    
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    
    except IndexError:
        print('Arquivo não fornecido')

if __name__=='__main__':
    main()