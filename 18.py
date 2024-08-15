compra = float(input('Insira o valor da compra R$'))

if compra < 100:
    total = compra*(1-(5/100))
    print(f'Total a pagar {total}')
elif 100<= compra <= 1000:
    total = compra*(1-(10/100))
    print(f'Total a pagar {total}')
elif compra > 1000:
    total = compra*(1-(15/100))
    print(f'Total a pagar {total}')
