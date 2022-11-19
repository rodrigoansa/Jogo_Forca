

palavra = 'dado'
acertos = 0
erros = 0
tracos = '_ ' * len(palavra)

while acertos != len(palavra) and erros < 7:
    letra = str(input('Digite uma letra: '))

    if letra in palavra:
        acertos += 1
        print(tracos)
    else:
        erros += 1
        print(f'Erros: {erros}')