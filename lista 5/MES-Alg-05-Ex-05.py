#Números ordinais
def ordinal(x):
    if x>0 and x<13:
        ordinais = ['','primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo','oitavo','nono','décimo','décimo primeiro','décimo segundo']
        return ordinais[x]
    return ''

def main():
    for numero in range(1,13):
        print(numero,'-', ordinal(numero))
    numero= int(input('Informe um número:'))
    print(f'O número ordinal de {numero} é: {ordinal(numero)}')

if __name__=="__main__":
    main()