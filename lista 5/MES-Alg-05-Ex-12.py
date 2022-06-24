# Verificação de senha válida
def senha_valida(senha):
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    numero = 0
    minuscula = 0
    maiuscula= 0
    if len(senha)==8:
        for caractere in senha:
            if caractere in numeros:
                numero = 1
            if caractere.islower:
                minuscula = 1
            if caractere.isupper:
                maiuscula = 1
    if numero+minuscula+maiuscula==3:
        return True
    return False
    
def main():
    while True:
        senha= input('Informe a senha:')
        if senha_valida(senha):
            print('A senha é válida')
        else:
            print('A senha não é válida')

if __name__=="__main__":
    main()