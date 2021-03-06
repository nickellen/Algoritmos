# Caracteres únicos
def caracteres_únicos(palavra):
    if len(palavra)==len(set(palavra)):
        return True
    return False

def main():
    while True:
        string = input('Informe uma palavra:')
        if caracteres_únicos(string):
            print(f'"{string}" possui apenas letras únicas')
        else:
            print(f'"{string}" possui letras repetidas')

if __name__=="__main__":
    main()