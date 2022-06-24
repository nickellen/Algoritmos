# Dias em um mês
def dias_no_mes(mes, ano):
    meses31= [1, 3 ,5, 7, 8, 10, 12]
    meses30 = [4, 6, 9, 11]
    if mes in meses31:
        return '31 dias'
    elif mes in meses30:
        return '30 dias' 
    else:
        if ano%400==0 or ano%4==0:
            return '29 dias'
        else:
            return '28 dias'

def main():
    while True:
        mes = int(input('Informe um mês(1 a 12):'))
        ano = int(input('Informe um ano:'))
        print('Quantidade de dias no mês:', dias_no_mes(mes, ano))

if __name__=="__main__":
    main()