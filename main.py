def principal():
    palavra = str(input('Digite o texto:'))
    print(inverso(tirarEspacos(palavra)))

def inverso(texto):
    cont = len(texto)
    invertido = ''
    for i in range(cont - 1, -1, -1):
        invertido = invertido + texto[i]
    if texto == invertido:
        return 'O inverso de "{}" = "{}"\nTemos um palindromo'.format(texto, invertido)
    else:
        return 'O inverso de "{}" = "{}" \nNAO temos um palindromo'.format(texto, invertido)

def tirarEspacos(texto1):
    texto2 = ''
    for j in texto1:
        if j != ' ':
            texto2 = texto2 + j
    return texto2

principal()
