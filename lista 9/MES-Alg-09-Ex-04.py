import sys

if __name__=="__main__":
    i = 0
    while True:
        i+=1
        
        try:
            arquivo = open(sys.argv[i], "r")
            print(f'-------------------------- ARQUIVO {i} --------------------------')

            for line in arquivo:
                print(line.rstrip())
            print()

        except FileNotFoundError:
            print(f'Arquivo {i} não encontrado!')
            
        except IndexError:
            break