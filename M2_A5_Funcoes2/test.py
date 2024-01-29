# palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'papagaio']
# resultado = list(filter(lambda x: len(x) > 5, palavras))
# print(resultado)

# numeros = [1, 2, 3, 4, 5]

# resultado = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numeros))
# print(resultado)

# def minha_funcao(*args, **kwargs):

#     for arg in args:

#         print(arg)

#     for key, value in kwargs.items():

#         print(key, value)

# minha_funcao (1,2,3,nome='Alice', idade=25)

# palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre','papagaio']
# resultado = list(filter(lambda x: len(x) > 5, palavras))
# print(resultado)

import tkinter as tk



def change_label_text():

    label.config(text="Texto alterado!")



root = tk.Tk()

root.title("Janela de Exemplo")



label = tk.Label(root, text="Olá!", font=("Arial", 16))

label.pack()



button = tk.Button(root, text="Alterar Texto", command=change_label_text)

button.pack()



root.mainloop()