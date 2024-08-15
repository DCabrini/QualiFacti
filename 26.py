
def calcula_fatorial(n):
    mult = 1
    for v in range(n, 0, -1):
        mult = v*mult
    return mult

    

# Programa Principal
valor = int(input('Insira o valor: '))
fatorial = calcula_fatorial(valor)
print(fatorial)

