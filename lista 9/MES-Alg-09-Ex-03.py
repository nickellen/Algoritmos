# Exibir a "cauda" de um arquivo texto
import sys
def cauda(arquivo):
    lista = arquivo.readlines()
    new_lista = lista[-10:]

    for elemento in new_lista:
                print(elemento,end="")
                
    arquivo.close()
    return ''

def main():
    if __name__=="__main__":
        print('----------------- Cauda do arquivo -----------------')

        try:
            arquivo = open(sys.argv[1], "r")
            cauda(arquivo)

        except UnicodeDecodeError:
            arquivo = open(sys.argv[1], "r", encoding= "utf-8")
            cauda(arquivo)
                
        except FileNotFoundError:
            print('Arquivo não encontrado!')

        except IOError:
            print('Erro de entrada e saída!')
        
if __name__=='__main__':
    main()