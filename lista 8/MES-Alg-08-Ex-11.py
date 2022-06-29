# Codificação run-lenght
def codificação_runlenght(texto):
    if texto=='':
        return []
    i=1
    while i!=len(texto) and texto[i]==texto[0]:
        i+=1
    return [texto[0], i] + codificação_runlenght(texto[i:])
       
def main():
    texto = input('Informe um texto:')
    print('Lista compactada em run-lenght:', codificação_runlenght(texto))

if __name__=='__main__':
    main()