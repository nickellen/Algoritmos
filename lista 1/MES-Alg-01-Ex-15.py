# area de um  polígono regular
import math 

n = int(input('Número de lado:'))
l = float(input('Comprimento de um lado:'))

area = n * l ** 2 / (4 * math.tan (math.pi / n))

print (f'Área do polígono regular: {area:,.2f} metros quadrados')