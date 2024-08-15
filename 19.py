cont_par = 0
cont_impar = 0

for i in range(1, 11):
    n = int(input('Insira um número inteiro: '))
    if n%2 ==0:
        cont_par+=1
    else:
        cont_impar += 1

print(f'Total de números pares digitado foi de {cont_par}')
print(f'O total de números ímpares digitados foi de {cont_impar}')