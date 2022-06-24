# Calculando o troco.

centavos = int(input("Digite a quantidade de centavos:"))

moeda_50 = centavos // 50
resto1 = centavos % 50

moeda_25 = resto1 // 25
resto2 = resto1 % 25

moeda_10 = resto2 // 10
resto3 = resto2 % 10

moeda_5 = resto3 //5
resto4 = resto3 % 5

moeda_1 = resto4

print("Moeda de 50 centavos:", moeda_50)
print('Moeda de 25 centavos', moeda_25)
print('Moeda de 10 centavos', moeda_10)
print('Moeda de 5 centavos', moeda_5)
print('Moeda de 1 centavos', moeda_1)