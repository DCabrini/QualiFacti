def impar(palavra):
    return palavra[::2]

#Programa Principal
p = str(input('Insira a palavra: '))
impares = impar(p)
print(impares)