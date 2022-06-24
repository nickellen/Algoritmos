#Políndromos com múltiplas palavras
import string

frase = input('Informe uma frase:').lower()
frase = frase.replace(" ", "")

pontuação = string.punctuation
for p in pontuação:
    frase= frase.replace(p,"")

tamanho = len(frase)
i=0
y = (-1)
while i< tamanho:
    if frase[i]!= frase[y]:
        print('Não é palíndromo')
        break
    i+=1
    y-=1
else: 
    print('É palíndromo')