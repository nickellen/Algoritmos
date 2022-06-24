#Distância entre dois potos na terra
import math

lat1 = (float(input('Digite a latitude do primeiro ponto:')))
long1 = (float(input('Digite a longitude do primeiro ponto:')))
lat2 = (float(input('Digite a latitude do segundo ponto:')))
long2 = (float(input('Digite a logitude do segundo ponto:')))

t1 = math.radians (lat1)
g1 = math.radians (long2)
t2 = math.radians (lat2)
g2 = math.radians (long2)

senlat1 = math.sin(t1)
senlat2 = math.sin(t2)
coslat1 = math.sin(t1)
coslat2 = math.cos (t2)
coslong = math.cos (g1-g2)

distancia = 6371.01 * math.acos (senlat1*senlat2+coslat1*coslat1*coslat2*coslong)

print (f'A distância entre os dois ponto é de: {distancia:.2f} km')