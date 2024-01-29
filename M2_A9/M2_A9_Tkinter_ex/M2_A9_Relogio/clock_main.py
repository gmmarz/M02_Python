import tkinter as tk 
import time

def time_string():
    return time.strftime("%H:%M:%S")

def update():
    #Atualiza label a cada segundo
    tmr_var.set(time_string())
    root.after(1000,update)


#Configuração da Janela
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x80")

tmr_var = tk.StringVar()

# Configurando os elementos
clock = tk.Label(root,textvariable=tmr_var,font=("Digital-7", 40))

#Mostrando os elementos 
clock.pack()

#Chamando a função update para inicializar a atualização do relogio
update()


root.mainloop()




