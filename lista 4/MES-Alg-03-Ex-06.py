#Classifique o triângulo. 
comp1 = float(input('Informe o comprimento do primeiro lado do triângulo:'))
comp2 = float(input('Informe o comprimento do segundo lado do triângulo:'))
comp3 = float(input('Informe o comprimento do terceiro lado do triângulo:'))

if comp1 == comp2 == comp3:
    print('Triângulo equilátero')
elif (comp1 == comp2) or (comp2 == comp3) or (comp1==comp3):
    print('Triângulo isóceles')
else:
    print('Triângulo escaleno')