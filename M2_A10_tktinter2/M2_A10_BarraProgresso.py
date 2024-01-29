from tkinter import *
from tkinter import ttk

#Criando janela

root = Tk()
root.title("Exemplo Barra de progresso")
barra_progresso = ttk.Progressbar(root,orient="horizontal", length=200,mode="determinate")
barra_progresso.pack()
barra_progresso.start(50)



root.mainloop()