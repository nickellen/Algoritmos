#Calculadora de envio e-commerce
def valor (x):
    primeiro_item =  10.95
    demais_itens = 2.95
    return primeiro_item + (x-1)*demais_itens

def main():
    itens = int(input('Informe a quantidade de itens para o envio:'))
    print('Custo do envio: R$', format(valor(itens), '.2f'))

if __name__=='__main__':
    main()