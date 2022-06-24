#TABELA DE MULTIPLICAÇÃO

for linha in range(1,11):
    print(f'\t{linha}', end="")
print()

for coluna in range(1,11):
    print(coluna,end='')
    for numero in range(1,11):
        numero = numero * coluna
        print(f'\t{numero}',end='')
    print()