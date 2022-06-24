#Raízes da equação quadrática
a= float(input('Informe o vale de a:'))
b= float(input('Informe o vale de b:'))
c= float(input('Informe o vale de c:'))

discriminante = b**2 - 4*a*c

raiz1 = (-b + discriminante**0.5) / 2*a
raiz2 = (-b - discriminante**0.5) / 2*a

if a== 0:
    print('ERRO')
else:
    if discriminante<0:
         print('A equação não possui raízes reais.')
    elif discriminante== 0:
        print('A equação possui uma raíz real:')
        print('- Valor da raíz:', raiz1)
    else:
         print('A equação possui duas raízes reais:')
         print('- Valor da primeira raíz:', raiz1)
         print('- Valor da segunda raíz:', raiz2)