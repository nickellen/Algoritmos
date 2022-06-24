# Somente palavras
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
    return lista

def main():
    texto = input(('Informe um texto:'))
    print('Palvras contidas no texto:', texto_palavras(texto))

if __name__=='__main__':
    main()