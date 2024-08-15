import math 

def hipo(cat_a, cat_b):
    return math.sqrt(cat_a**2 + cat_b**2)

def seno(cat_oposto, hipotenusa):
    return cat_oposto/hipotenusa

def cosseno(cat_adjacente, hipotenusa):
    return cat_adjacente/hipotenusa

def tangente(cat_oposto, cat_adjacente):
    return cat_oposto/cat_adjacente

#Programa Principal

cateto_opo = float(input('Insira o valor do cateto A: '))
cateto_adja = float(input('Insira o valor do cateto B: '))

hipotenusa = hipo(cateto_opo, cateto_adja)
valor_seno = seno(cateto_opo, hipotenusa)
valor_coss = cosseno(cateto_adja, hipotenusa)
valor_tange = tangente(cateto_opo, cateto_adja)


print(hipotenusa)
print(valor_seno)
print(valor_coss)
print(valor_tange)