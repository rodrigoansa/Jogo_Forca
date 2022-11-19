import os
with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_palavras =  

palavra = 'dado'
acertos = 0
erros = 0
tracos = '_ ' * len(palavra)
letras_acertadas = ''
letras_erradas = ''

forca = """
----|
    |    
    """

nada = """


"""

cabeca = """
    O
"""
corpo = """
    O
    |
"""
braco_esq = """
    O
    |\\
"""
braco_dir = """
    O
   /|\\
"""
perna_esq = """
    O
   /|\\
     \\
"""
perna_dir = """
    O
   /|\\
   / \\
"""


chances = [
    nada,
    cabeca,
    corpo,
    braco_esq,
    braco_dir,
    perna_esq,
    perna_dir,
]


while acertos != len(palavra) and erros < 7:

    mostrar_letra = ''
    for letra  in palavra:
        os.system("clear")
        if letra in letras_acertadas:
            mostrar_letra += letra + ' '
        else:
            mostrar_letra += '_ '
    
    print(f'A palavra contém: {len(palavra)} Letras')
    print(mostrar_letra)
    print(forca+chances[erros])
    print(f'Letras Erradas: {letras_erradas}')


    letra = input('Digite uma letra: ')
    
    if letra in palavra:
        os.system("clear")
        letras_acertadas += letra + ' '
        acertos += 1
               
    else:
        letras_erradas += letra + ' '
        erros += 1
        print('Você Perdeu.')

