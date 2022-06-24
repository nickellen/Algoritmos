#Área de um triângulo novamente
import math

lado1 = float(input('Digite o lado 1:'))
lado2 = float(input('Digite o lado 2:'))
lado3 = float(input('Digite o lado 3:'))

l = (lado1 + lado2 + lado3) / 2

area = math.sqrt (l * (l-lado1) * (l-lado2) * (l-lado3))

print ('A área do triângulo é:', area, 'metros quadrados')