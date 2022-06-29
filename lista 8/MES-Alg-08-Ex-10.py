# Decodififcação run-lenght
def decodificação_runlenght(lista):
    cópia = list(lista[0] * int(lista[1]))
    if len(lista)==2:
        return cópia
    return cópia + decodificação_runlenght(lista[2:])

def main():
    lista = ["A", 12, "B", 4, "A", 6, "B", 1]
    print('Lista compactada em run-lenght:', lista)
    print('Lista descompactada:', decodificação_runlenght(lista))

if __name__=='__main__':
    main()