
def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    if n1 == 0:
        return 'Divisão por zero não existe!'
    else:
        return n1/n2

#Programa Principal

n1 = float(input('Insira o prmeiro valor: '))
n2 = float(input('Insira o segundo valor: '))

print('''Qual operação deseja realizar:\n
      [+] - Soma
      [-] - Subtração
      [*] - Multiplicação
      [/] - Divisão''')
esc = str(input('Insira qual operação deseja realizar: '))

if esc == '+':
    s = soma(n1,n2)
    print(s)
elif esc == '-':
    sub = subtracao(n1,n2)
    print(sub)
elif esc == '*':
    mult = multiplicacao(n1,n2)
    print(mult)
elif esc == '/':
    div = divisao(n1,n2)
    print(div)