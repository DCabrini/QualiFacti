n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if (n1 > n2) and (n1 % n2) ==0:
    print('O primeiro número é maior e divisível pelo segundo')
elif (n1 > n2) and (n1 % n2) !=0:
    print('O primeiro número é maior, mas não é divisível pelo segundo')
elif (n1 < n2):
    print('O primeiro número não é maior que o segundo')