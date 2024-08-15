nasc = int(input('Insira o ano de nascimento: '))
atual = int(input('Insira o ano atual: '))

if atual >= nasc and nasc >= 0 and atual >= 0:
    for ano in range(nasc, atual+1, 1 ):
        print(ano)