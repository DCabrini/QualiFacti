def preenche(nome, data):
    template = '''Olá
    Prezado, [NOME]
    Seja bem vindo a DC DATA
    
    [DATA]'''
    temp_pre = template.replace("[NOME]", nome).replace("[DATA]", data)
    return temp_pre


#PRograma Principal

name = str(input('Insira o nome do destinatário: '))
data = str(input('Indsira a data de hoje: '))

final = preenche(name, data)
print(final)
