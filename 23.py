
senha = ' '
while senha != 'SAIR':
    cel = float(input('Insira o valor da temperatura em Celsius: '))
    far = 9*(cel/5) + 32
    senha = str(input('Deseja encerrar?\n Digite Sair: ')).upper().strip()
    #if perg in 'SAIR':
    #    break
print(f'{cel}°C = {far}°F ')