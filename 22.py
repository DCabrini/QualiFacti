import math
valor = float(input('Insira o valor que pode economizar por mêr R$'))
meta = float(input('Insira o total final de economia R$'))

meses = meta/valor

print(f'{math.ceil(meses)} meses')