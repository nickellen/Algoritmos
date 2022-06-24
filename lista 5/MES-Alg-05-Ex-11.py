#Senha aleatória
def senha_aleatoria():
    import random
    senha = ''
    comprimento = random.randrange(7,11)
    for i in range(0,comprimento):
        caracter = random.randrange(33,127)
        caracter= chr(caracter)
        senha +=caracter
    return senha

def main():
    print(senha_aleatoria())

if __name__=="__main__":
    main()