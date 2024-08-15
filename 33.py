def sub(frase, palavra):
    for p in palavra:
        frase = frase.replace(p, '****')
    return frase

#Programa Principal

frase_riginal = str(input('Digite a frase: ')).lower()
palavra_proibida = [str(input('Digte  apalava proíbida: ')).lower()]

frase_final = sub(frase_riginal, palavra_proibida)

print(frase_final)

