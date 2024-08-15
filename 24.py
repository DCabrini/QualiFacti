l1 = float(input('Insira o valor de l1: '))
l2 = float(input('Insira o valor de l2: '))
l3 = float(input('Insira o valor de l2: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('O Triângulo é equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")