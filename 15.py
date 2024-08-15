idade = int(input('Insira a idade: '))
if idade < 13:
    print('Criança')
elif 13 <= idade <= 19:
    print('Adolescente')
elif 20 <= idade <= 59:
    print('Adulto')
elif idade >= 60:
    print('Idoso')