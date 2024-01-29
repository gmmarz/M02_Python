from tkinter import *
from tkinter import ttk

Janela = Tk()

lista_pessoas = [
    (1,"Not","not@gmail.com"),
    (2,"Davi","davi@gmail.com"),
    (3,"Dani","dani@gmail.com")
]

tabela = ttk.Treeview(Janela, columns=("id","nome","email"), show="headings")

tabela.column("id",width=60,minwidth=30) #Permite que as colunas de adptem as janelas que vão abrir em um tamanho máximo de 30 e minino de 15
tabela.column("nome",width=60, minwidth=30)
tabela.column("email",width=120,minwidth=60)

tabela.heading("id", text="ID")
tabela.heading("nome",text="Nome")
tabela.heading("email",text="Email")

#inserindo registros na tabela
# #Para inserir o dado, o primeiro argumento no exemplo está vazio pois é uma tabela normal, se fosse um elemento tipo toggle( que poderia ser colapsado) seria necessário passar um parent(um elemento que seria a pasta)
#Está seria uma maneira de adicionar elemento por elemento. 
# tabela.insert("",END,values=(1,"Not","not@gmail.com"))
# tabela.insert("",END,values=(2,"Davi","davi@gmail.com"))
# tabela.insert("",END,values=(3,"Dani","dani@gmail.com"))

#Melhor pratica seria adicionar com um for.
for pessoa in lista_pessoas:
    tabela.insert("",END,values=pessoa)

tabela.pack()


Janela.mainloop()

