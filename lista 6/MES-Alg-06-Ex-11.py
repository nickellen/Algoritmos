# Mega sena:
import random
bilhete= []
x=0
while x!=6:
    aleatorio = random.randrange(1,61)
    if aleatorio in bilhete:
        continue
    else:
        bilhete.append(aleatorio)
    x+=1

print('Números do bilhete de mega-sena sorteados:')
for numero in sorted(bilhete):
    print(numero,' ', end='')