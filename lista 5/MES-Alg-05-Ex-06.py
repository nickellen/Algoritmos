#Centralizando uma string
def centralizar (string,largura):
    espaço = (largura - len(string))//2
    resultado = ""
    for i in range(0, espaço):
        resultado += " "
    return resultado + string

def main():
    string = input("Informe uma palavra:")
    largura = int(input('Informe a largura da linha do terminal:'))
    print(centralizar(string, largura))

if __name__=="__main__":
   main()