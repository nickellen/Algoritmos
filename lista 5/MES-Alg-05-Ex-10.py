# Números primos
def primo(x):
    if x<=0:
        return False
    for caractere in range(2, x):
        if x%caractere==0:
            return False
    return True

def main():
    while True:
        numero = int(input('Digite um numero:'))
        if primo(numero):
            print('É primo')
        else:
            print('Não é primo')

if __name__=="__main__":
    main()