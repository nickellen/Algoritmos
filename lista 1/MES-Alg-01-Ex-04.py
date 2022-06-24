# Cálculo da área de um terreno em hectares
larg = float(input('Informe o comprimento de largura(m):'))
prof = float (input('Informe o comprimento de profundidade(m):'))

area = larg * prof

hectares = area/10000

print ('A área é de:', hectares, 'hectares')