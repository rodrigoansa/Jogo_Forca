from tkinter import *
import os
import time
from random import choice

with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_palavras = linhas.split('\n')


palavra = choice(lista_palavras).upper()
acertos = 0
erros = 0
tracos = '_ ' * len(palavra)
letras_acertadas = ''
letras_erradas = ''


window = Tk()
window.title('Jogo da Forca')
window.geometry('360x640+1080+400')
window.resizable(False, False)


forca = PhotoImage(file="imagens/forca.png")
label_forca = Label(window, image=forca)
label_forca.place(relwidth=1, relheight=1)
#Importação das imagens
def inicio():
    img = PhotoImage("imagens/forca.png")
    label_forca.configure(image=img)
    label_forca.image = img

def cabeca():
    forca = PhotoImage(file="imagens/cabeca.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

def corpo():
    forca = PhotoImage(file="imagens/corpo.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

def braco_esq():
    forca = PhotoImage(file="imagens/braco_esq.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

def braco_dir():
    forca = PhotoImage(file="imagens/braco_dir.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

def perna_esq():
    forca = PhotoImage(file="imagens/perna_esq.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

def perna_dir():
    forca = PhotoImage(file="imagens/perna_dir.png")
    label_forca = Label(window, image=forca)
    label_forca.place(relwidth=1, relheight=1)

chances = [
    inicio,
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
        if letra in letras_acertadas:
            mostrar_letra += letra + ' '
        else:
            mostrar_letra += '_ '

    inicio()
    texto_contem = Label(window, font = ("Arial Black", 13), text = (f'A palavra contém {len(palavra)} Letras'), bg='white')
    texto_contem.place(x=12, y=340)

    texto_mostrar_letra = (window, mostrar_letra)
    texto_contem.place(x=12, y=340)

    #print(mostrar_letra)
    


    texto_acertadas = Label(window, font = ("Arial Black", 11), text = f'Letras Acertadas: {letras_acertadas}', bg='white')
    texto_acertadas.place(x=5, y=443)

    texto_erradas = Label(window, font = ("Arial Black", 11), text = f'Letras Erradas: {letras_erradas}', bg='white')
    texto_erradas.place(x=5, y=465)


    letra = input('Digite uma letra: ').upper()

    if letra in letras_acertadas+letras_erradas:
        texto_tentou = Label(window, font = ("Arial Black", 13), text = ('Você já tentou essa letra'), bg='white')
        texto_tentou.place(x=12, y=420)
        time.sleep(2)
        continue
    
    if letra in palavra:
        letras_acertadas += letra + ' '
        acertos += palavra.count(letra)
        texto_venceu = Label(window, font = ("Arial Black", 13), text = ('Você Venceu!'), bg='white')
        texto_venceu.place(x=12, y=420)
        
               
    else:
        letras_erradas += letra + ' '
        erros += 1
        texto_perdeu = Label(window, font = ("Arial Black", 13), text = ('Você Perdeu.'), bg='white')
        texto_perdeu.place(x=12, y=420)
        texto_palavra = Label(window, font = ("Arial Black", 13), text = (f'A palavra é: {palavra}'), bg='white')
        texto_palavra.place(x=12, y=440)
        
window.bind("<Return>", inicio)
window.mainloop()
