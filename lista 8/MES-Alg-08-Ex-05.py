# Total de valores numéricos
def valores_numéricos():
    n = input('Informe um número:')
    if n=='':
        return 0
    return int(n) + valores_numéricos()

print('Soma:', valores_numéricos())