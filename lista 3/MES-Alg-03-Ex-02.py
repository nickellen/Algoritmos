# Idade canina
idade = int(input('Digite a idade do seu cachorrro:'))

if idade<0:
    print('ERRO')
else: 
    if idade<= 2:
        ano = idade * 10.5
        print('Seu cachorro tem', ano, 'anos caninos')
    else:
        ano = (idade-2)*4+21
        print('Seu cachorro tem', ano,'anos caninos')