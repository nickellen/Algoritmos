# Ordenação de 3 inteiros.

n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o sugundo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))

min = min(n1,n2,n3)
max = max(n1,n2,n3)
medio = (n1+n2+n3) - min - max

print ("Números de forma ordenada:", min, medio, max)