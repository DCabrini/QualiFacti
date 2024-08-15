compra = float(input('Insisra o valor da compra: R$'))
desconto = int(input('Insira o valor do desconto (%): '))

total = (compra)*(1 - desconto/100)
print(f'Total da compra = R${compra}')
print(f'Valor do desconto {desconto}%')
print(f'Total final a pagar é de R${total}')
