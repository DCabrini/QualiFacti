n1 = float(input('Forneça o primeiro valor: '))
n2 = float(input('Forneça o segundo valor: '))
n3 = float(input('Forneça o terceiro valor: '))

if n1 > n2 and n1 > n3:
    if n1 > n2 + n3:
        print('O primeiro número é maior que a soma dos outros dois')
    elif n1 < n2 + n3:
        print('O primeiro número é o maior, mas não maior que a soma dos outros dois')
else:
    print('O primeiro número não é o maior') 