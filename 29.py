from random import randint

pc  = randint(0, 101)
while True:  
    jogador = int(input('Insira um número inteiro entra 0 e 100: '))
    if pc > jogador:
        print(f'Você errou\n O computador escolheu MAIOR que {jogador}')
    elif pc < jogador:
        print(f'Você errou\n O computador escolheu MENOR que {jogador}')
    elif pc == jogador:
        break
print(f'Parabéns!!!\nVocê venceu.\nO computador escolheu {pc} e você {jogador}')