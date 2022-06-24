# Diferença simétrica
def diferença_simétrica(M,N):
    soma0 = list(M.difference(N))
    soma1 = list(N.difference(M))
    return sorted(soma0 + soma1)

def main():
    conjunto1 = set()
    while True:
        numero0 = input('Informe um número para o primeiro conjunto(enter para parar):')
        if numero0== '':
            break
        conjunto1.add(int(numero0))
    print('\n')

    conjunto2 = set()
    while True:
        numero = input('Informe um número para o segundo conjunto(enter para parar):')
        if numero== '':
            break
        conjunto2.add(int(numero))

    print('Diferença simétrica dos conjuntos:', diferença_simétrica(conjunto1,conjunto2))

if __name__=="__main__":
    main()