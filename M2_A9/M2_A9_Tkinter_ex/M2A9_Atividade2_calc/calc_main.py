import tkinter as tk

root = tk.Tk()

win_titulo = root.title("Calculadora")

#Variaveis tkinter
result = tk.DoubleVar(root)
num1 = tk.DoubleVar(root)
num2 = tk.DoubleVar(root)
flg_operEnd = tk.BooleanVar(root)


#Criando elementos
but_1 = tk.Button(root, text="1")





root.mainloop()