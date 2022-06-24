# Conta de investimentos
investimento = (float(input("Informe o valor do investimento:")))

juros_ao_ano = investimento * 0.12

ano1 = investimento + juros_ao_ano
ano2 = ano1 + juros_ao_ano
ano3 = ano2 + juros_ao_ano

print (f'Valor do saldo em 1 ano: R${ano1:,.2f}')
print (f'Valor do saldo em 2 anos: R${ano2:,.2f}')
print (f'Valor do saldo em 3 anos: R${ano3:,.2f}')