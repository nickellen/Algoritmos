# Raíz quadrada recursiva
def raiz_quadrada(n, estimativa=1.0):
    if abs((estimativa**2) - n) <= 1E-12:
        return estimativa
    return raiz_quadrada(n,(estimativa+(n/estimativa))/2)

numero = float(input('Informe um numero:'))
print(f'Raíz quadrada de {numero}: {raiz_quadrada(numero)}')