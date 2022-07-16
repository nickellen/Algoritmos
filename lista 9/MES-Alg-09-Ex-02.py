# Exibir o cabeçalho de um arquivo texto
import sys

def cabeçalho(arquivo):
    for i in range(10):
        linha = arquivo.readline()
        print(linha, end='')
    arquivo.close()
    return ''

def main():
    print('----------------- Cabeçalho do arquivo -----------------')

    if __name__=="__main__":
        
        try:
            arquivo = open(sys.argv[1], "r", encoding= "utf-16")
            cabeçalho(arquivo)
            
        except UnicodeError:
            arquivo = open(sys.argv[1], "r", encoding= "utf-8")
            cabeçalho(arquivo)

        except FileNotFoundError:
            print("Arquivo não encontrado!")

if __name__=="__main__":
    main()