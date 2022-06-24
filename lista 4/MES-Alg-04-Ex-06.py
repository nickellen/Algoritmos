#Bits de paridade
while True:
    byte = input('Informe uma sequência de 8 bits:')
    if len(byte)!=8:
        print('Erro: você deve informar uma sequência de 8 bits!')
        continue

    for bit in byte:
        if bit!='0' and bit!='1':
            print('Erro: Você deve informar bits 0 e 1!')
            break
    else:
        um = byte.count('1')
        if um%2==0:
            print('Bit de paridade deve ser: 0')
        else:
            print('Bit de paridade deve ser: 1')