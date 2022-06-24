# Número de matrícula.

matricula = int(input('Insira o número de matrícula:'))

ano = matricula // 10000

semestre = (matricula % 10000) // 1000

print ('Ano de matícula:', ano)
print ('Semestre da matrícula:', semestre)