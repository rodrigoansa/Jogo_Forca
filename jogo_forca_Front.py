import tkinter as tk
from tkinter import *
import os
import time
from random import choice

pastaApp = os.path.dirname(__file__)

window = tk.Tk()
window.title('Jogo da Forca')
window.geometry('360x640+1080+400')
window.resizable(False, False)

bg = PhotoImage(file=pastaApp+"\\bg.gif")
l_bg = Label(window,image=bg)
l_bg.place()

window.mainloop()

with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_palavras = linhas.split('\n')


palavra = choice(lista_palavras).upper()
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
    print(f'Letras Acertadas: {letras_acertadas}')
    print(f'Letras Erradas: {letras_erradas}')


    letra = input('Digite uma letra: ').upper()

    if letra in letras_acertadas+letras_erradas:
        print('Você já tentou essa letra')
        time.sleep(2)
        continue
    
    if letra in palavra:
        os.system("clear")
        letras_acertadas += letra + ' '
        acertos += palavra.count(letra)
        print('Você Venceu!')
        print(f'A palavra é: {palavra}')
               
    else:
        letras_erradas += letra + ' '
        erros += 1
        print('Você Perdeu.')
        print(f'A palavra é: {palavra}')

