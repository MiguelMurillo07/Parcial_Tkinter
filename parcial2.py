# Parcial final: Cree un programa con la ayuda de tkinter que pida un numero entero para determinar filas y columnas de una matriz, donde genere números aleatorios y te pida buscar un número en específico y lo indique gráficamente por medio de un color distinto al de los demás. 


from tkinter import *
import random
from tkinter import messagebox

# Definiciones de la app

def salir():
    messagebox.showinfo("Salir", "La app se cerrará.")
    principal.destroy()

def borrar():
    messagebox.showinfo("Borrar todo", "Hizo click en el botón borrar")
    t.set("")
    n.set("")
    t_resultados.delete("1.0", "end")

def calcular():
    messagebox.showinfo("Graficación", "Dió el paso siguiente para graficar")

principal = Tk()
principal.title("Matrices y Canvas")
principal.geometry("700x500")
principal.resizable(False, False)
principal.config(bg="purple")

# Variables locales

t = StringVar()
n = StringVar()


# Frame entrada
frame_entrada = Frame(principal)
frame_entrada.config(bg="white", width=680, height=150)
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text="Matríz Cuadrada")
titulo.config(bg="red", fg="green", font=("Rockwell",15))
titulo.place(x=250, y=15)

# Etiqueta para el tamaño de la matriz

tamaño = Label(frame_entrada, text="Tamaño de la matriz: ")
tamaño.config(bg="white", fg="black", font=("Rockwell", 15))
tamaño.place(x=30, y=65)

# Entry para el tamaño

tamaño_e = Entry(frame_entrada, textvariable=t)
tamaño_e.config(font=("Rockwell", 15), justify=LEFT)
tamaño_e.place(x=250, y=65, width=50)

# Etiqueta para el número a buscar

numero = Label(frame_entrada, text="Número a buscar: ")
numero.config(bg="white", fg="black", font=("Rockwell", 15))
numero.place(x=32, y=102)

# Entry para el número

numero_e = Entry(frame_entrada, textvariable=n)
numero_e.config(font=("Rockwell", 15), justify=LEFT)
numero_e.place(x=250, y=105, width=50)

# Frame operaciones

frame_operaciones = Frame(principal)
frame_operaciones.config(bg="blue", width=680, height=80)
frame_operaciones.place(x=10, y=180)

# Botones

# Boton para calcular

bt_calcular = Button(frame_operaciones, text="Interpretar", command=calcular, font=("Rockwell", 11))
bt_calcular.place(x=90, y=25, width=120, height=30)

# Botón para salir

bt_salir = Button(frame_operaciones, text="Salir", command=salir, font=("Rockwell", 11))
bt_salir.place(x=550, y=25, width=60, height=30)

# Botón para borrar

bt_borrar = Button(frame_operaciones, text="Borrar datos", command=borrar, font=("Rockwell", 11))
bt_borrar.place(x=310, y=25, width=100, height=30)

# Frame resultados
frame_resultados = Frame(principal)
frame_resultados.config(bg="brown", width=680, height=200)
frame_resultados.place(x=10, y=280)


# Creacion de canvas

canva1 = Canvas()



principal.mainloop()
