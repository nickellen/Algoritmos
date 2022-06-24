#nota para frequência
nota = input('Informe o nome de uma nota:')

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4= 440.00
B4 = 493.88

x = int(nota[1])

print('Frequência da nota:')
if nota[0]== 'C':
   print(C4/ 2**(4-x),'Hz')

elif nota[0]== 'D':
    print(D4/ 2**(4-x),'Hz')

elif nota[0]== 'E':
    print(E4/ 2**(4-x),'Hz')

elif nota[0]== 'F':
    print(F4/ 2**(4-x),'Hz')

elif nota[0]== 'G':
    print(G4/ 2**(4-x),'Hz')

elif nota[0]== 'A':
    print(A4/ 2**(4-x))

elif nota[0]== 'B':
    print(B4/ 2**(4-x),'Hz')
else:
    print('ERRO')