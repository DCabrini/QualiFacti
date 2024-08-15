n = int(input('Insira um número inteiro: '))
mult = 1

for i in range(n, 0, -1):
    mult = i*mult

print(mult)