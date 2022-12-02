import customtkinter

customtkinter.set_appearance_mode('default')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x250')

def button_event():
    print("button pressed")

botao_1 = customtkinter.CTkButton(janela, text="CTkButton", command=button_event, width=120, height=32, border_width=0, corner_radius=8)
botao_1.place(x=250, y=125, anchor=customtkinter.CENTER)

janela.mainloop()