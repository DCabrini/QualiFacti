from math import sqrt
v_0 = float(input('Digite a velocidade inicial (m/s): '))
a = float(input('Digite a aceleração constante (m/s²): '))
dis_p = float(input('Digite a distância pecorrida (m): '))

v = sqrt( ((v_0)**2) + 2*a*dis_p)
print(f'A velocidade final v = {v}m/s')