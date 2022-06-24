# Letras maiúsculas
def letras_maiusculas(frase):
    caractere = True
    nova_frase= ''
    for letra in frase:
        if letra in ['.','!','?']:
            nova_frase+= letra
            caractere = True
            continue
        if caractere and letra!=" ":
            nova_frase+= letra.upper()
            caractere= False
            continue
        else:
            nova_frase+= letra
    return nova_frase
        
def main():
    frase= input('Digite uma frase para correção das letras maiúsculas:')
    print('Frase corrigida:', letras_maiusculas(frase))

if __name__=="__main__":
    main()