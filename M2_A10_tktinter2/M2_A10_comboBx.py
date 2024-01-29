from tkinter import *
from tkinter import ttk

#Criando janela

root = Tk()
root.title("Exemplo combobox")

#Dias da semana
dias_semana = ["Segunda feira","Terça feira","Quarta Feira","Quinta feira","sexta feira","Sabado","Domigo"]

#Criando a combobox

cmb_bx = ttk.Combobox(root,values=dias_semana)
cmb_bx.pack(padx=75,pady=20)




root.mainloop()