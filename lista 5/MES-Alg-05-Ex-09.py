# A string representa um inteiro?
def isInteger(string):
    if string!= '':
        string = string.strip()
        string2= string[1:]
        if string.isnumeric():
            return True
        elif string[0] in ['+','-']:
            if string2.isnumeric():
                return True
    return False

def main():
    while True:
        string = input('Informe uma string:')
        if isInteger(string):
            print('É um inteiro')
        else:
            print('Não é um inteiro')

if __name__=='__main__':
    main()