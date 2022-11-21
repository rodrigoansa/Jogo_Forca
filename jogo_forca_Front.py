from tkinter import *
import os
import time
from random import choice


window = Tk()
window.title('Jogo da Forca')
window.geometry('360x640+1080+400')
window.resizable(False, False)

#textos
texto_contem = Label(window, text = 'A palavra contém:   Letras')
texto_contem.grid(column=1, row=5)

#Importação das imagens
def forca():
    forca = PhotoImage(file="imagens/forca.png")
    label_forca = Label(window, image=forca)
    label_forca.place(x=0, y=0, relwidth=1, relheight=1)

def cabeca():
    cabeca = PhotoImage(file="imagens/cabeca.png")
    label_cabeca = Label(window, image=cabeca)
    label_cabeca.place(x=0, y=0, relwidth=1, relheight=1)

def corpo():
    corpo = PhotoImage(file="imagens/corpo.png")
    label_corpo = Label(window, image=corpo)
    label_corpo.place(x=0, y=0, relwidth=1, relheight=1)

def braco_esq():
    braco_esq = PhotoImage(file="imagens/braco_esq.png")
    label_braco_esq = Label(window, image=braco_esq)
    label_braco_esq.place(x=0, y=0, relwidth=1, relheight=1)

def braco_dir():
    braco_dir = PhotoImage(file="imagens/braco_dir.png")
    label_braco_dir = Label(window, image=braco_dir)
    label_braco_dir.place(x=0, y=0, relwidth=1, relheight=1)

def perna_esq():
    perna_esq = PhotoImage(file="imagens/perna_esq.png")
    label_perna_esq = Label(window, image=perna_esq)
    label_perna_esq.place(x=0, y=0, relwidth=1, relheight=1)

def perna_dir():
    perna_dir = PhotoImage(file="imagens/perna_dir.png")
    label_perna_dir = Label(window, image=perna_dir)
    label_perna_dir.place(x=0, y=0, relwidth=1, relheight=1)



with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_palavras = linhas.split('\n')


palavra = choice(lista_palavras).upper()
acertos = 0
erros = 0
tracos = '_ ' * len(palavra)
letras_acertadas = ''
letras_erradas = ''


chances = [
    forca(),
    cabeca(),
    corpo(),
    braco_esq(),
    braco_dir(),
    perna_esq(),
    perna_dir(),
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
    #forca()#+chances[erros]
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

window.mainloop()