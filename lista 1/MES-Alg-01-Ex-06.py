# Conta do almoço
suco = (float(input('Digite o preço do suco: R$')))
prato = (float(input('Digite o preço do prato principal: R$')))
sobremesa = (float(input('Digite o preço da sobremesa: R$')))

conta = suco + prato + sobremesa

serviço = conta * 0.1

total= conta + serviço

print (f'Valor da conta com taxa de de serviço: R$:{total:,.2f}')