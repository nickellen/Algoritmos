#Cifra de César
mensagem0 = input('Informe um caractere:').upper()
posição = int(input('Informe a posição de deslocamento:'))

print('Mensagem convertida:')
for caractere in mensagem0:
    numero = ord(caractere)
    numero = int(numero)
    mensagem = numero + posição

    if mensagem>90:
        mensagem = mensagem-26
    elif mensagem<65:
        mensagem = mensagem+26

    total = chr(mensagem)

    print(total, end='')