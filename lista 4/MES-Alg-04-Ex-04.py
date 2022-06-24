#Perímetro de um polígono
from math import sqrt
x0 = float(input('Digite a coordenada x de um ponto: '))
y0 = float(input('Digite a coordenada y de um ponto: '))

x_ant= x0
y_ant= y0
perimetro = 0

while True:
    x = input('Digite a coordenada x de um ponto(enter para sair): ')
    if not x:
        break
    y_atual = float(input('Digite a coordenada y de um ponto: '))
    x_atual = float(x)
    distancia= sqrt((y_atual-y_ant)**2+(x_atual-x_ant)**2)
    perimetro= perimetro+ distancia
    y_ant = y_atual
    x_ant= y_atual

distancia= sqrt((y_ant-y0)**2+(x_ant-x0)**2)
perimetro = perimetro+ distancia
print('O perímetro deste polígono é igual a', perimetro)