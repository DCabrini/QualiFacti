import  math
def rad(graus):
    radia = ((math.pi)/180)*graus
    return radia

#programa Principal
x = float(input('Insira o valor do ângulo em Graus: '))
resultado = rad(x)
print(resultado)