# Datas mágicas
def data_magica(dia, mes, ano):
    ano = str(ano)
    ano =ano[2:]
    if mes*dia== int(ano):
        return True
    return False

def dias_no_mes(mes, ano):
    if mes in [1, 3 ,5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30 
    else:
        if ano%400==0 or ano%4==0:
            return 29
        else:
            return 28

def main():
    print('Datas mágicas do século XX:')
    for ano in range(1901,2001):
        for mes in range(1,13):
            dias = dias_no_mes(mes, ano)
            for dia in range(1, (dias+1)):
                if (data_magica(dia, mes, ano)):
                    print(f'{dia}/{mes}/{ano}')

if __name__=='__main__':
    main()