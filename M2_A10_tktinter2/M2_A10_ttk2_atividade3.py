#Cadastro de alunos.
#Dados devem se mostrados em uma tree view

from tkinter import *
from tkinter import ttk


def but_cadastrar():
    dict_pessoa = {}
    id = 0
    if len(lst_pessoas) == 0:
        dict_pessoa = {"id":id,"nome":var_nome.get(),"email":var_email.get()}
    else:
        id = lst_pessoas[len(lst_pessoas)-1]["id"] + 1
        var_id.set(id)
        dict_pessoa = {"id":id,"nome":var_nome.get(),"email":var_email.get()}
    lst_pessoas.append(dict_pessoa)
    atualizar_tabela(dict_pessoa)

def atualizar_tabela(dict_pessoa):
    pessoa_inf = list(dict_pessoa.values())
    tabela_result.insert("",END,values=pessoa_inf)


#Configurando a janela

root = Tk()
root.title("Cadastro alunos")
root.geometry("300x200")

#Data
lst_pessoas = []

#Variáveis da janela
var_nome = StringVar()
var_id = IntVar()
var_email = StringVar()


#Criando frames
frame_in = ttk.Frame(root, relief="solid",borderwidth=1,width=1,height=80)
frame_result = ttk.Frame(root,relief="solid",borderwidth=1)

#Criando elementos do frame 1
lbl_id = ttk.Label(frame_in,text="id:")
lbl_nome = ttk.Label(frame_in,text="Nome:")
lbl_email = ttk.Label(frame_in,text="Email:")
lbl_frame_titulo = ttk.Label(frame_in,text="Dados de entrada")

in_nome = ttk.Entry(frame_in,textvariable=var_nome)
in_email = ttk.Entry(frame_in,textvariable=var_email)
in_id = ttk.Label(frame_in,textvariable=var_id)

but_cadastro = ttk.Button(frame_in,text="Cadastrar",command=but_cadastrar)

#Posicionando elementos no frame 1
lbl_frame_titulo.grid(row= 0 , columnspan= 2)
lbl_id.grid(row=1,column=0)
in_id.grid(row=1,column=1)
lbl_nome.grid(row=2,column=0)
in_nome.grid(row=2,column=1)
lbl_email.grid(row=3,column=0)
in_email.grid(row=3,column=1)
but_cadastro.grid(row=4, columnspan=2)

#Construindo tree view
tabela_result = ttk.Treeview(frame_result,columns=("id","nome","email"),show="headings")

#Formatando as columnas
tabela_result.column("id",width=60,minwidth=30)
tabela_result.column("nome",width=60,minwidth=30)
tabela_result.column("email", width=120,minwidth=60)

#Formatando os headers
tabela_result.heading("id",text="ID")
tabela_result.heading("nome",text="Nome")
tabela_result.heading("email",text="Email")

#Mostrando a janela no frame
tabela_result.pack()



#Mostrando os frames
frame_in.pack(expand=True,fill='x')
frame_result.pack(expand=True,fill='x') 



root.mainloop()