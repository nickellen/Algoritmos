#Aproximação do valor de π
print('Aproximações de π:')
pi = 3
print(pi)
x=1

n1 = 2
n2= 3
n3 = 4

while x<15:
    x+=1
    if x%2==0:
        pi = pi+ (4 / (n1*n2*n3))
        print(pi)
    else:
        n4= n3+1
        n5 = n4+1
        pi = pi- (4 / (n3*n4*n5))
        print(pi)
        n1 = n5
        n2 = n1+1
        n3= n2+1