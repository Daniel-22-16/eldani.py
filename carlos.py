from tkinter import ttk 
from tkinter import *

import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products application')
        # Crear un frame dentro de un contenedor
        Frame = LabelFrame(self.wind, text='Ferreteria El Tornillo Feliz')
        Frame.grid(row=0, column=0, columnspan=3, pady=10)

        # Entrada para un nombre:
        Label(Frame, text='DNI  ').grid(row=1, column=0)
        self.dni = Entry(Frame)
        self.dni.focus()
        self.dni.grid(row=1, column=1)


        # Colocar otro elemento:
        Label(Frame, text= 'Apellido  ').grid(row =2, column=0)
        self.apellido = Entry(Frame)
        self.apellido.grid(row=2, column=1)


        Label(Frame, text='Nombres  ').grid(row=2, column=2)
        self.nombre = Entry(Frame)
        self.nombre.grid(row=2, column=3)


        Label(Frame, text='Dirección  ').grid(row=3, column=0)
        self.dirección = Entry(Frame)
        self.dirección.grid(row=3, column=1,columnspan=3, sticky= W + E)


        Label(Frame, text='Teléfono  ').grid(row=3, column=0)
        self.teléfono = Entry(Frame)
        self.teléfono.grid(row=4, column=1,columnspan=3, sticky= W + E)

if __name__== '__main__' :
    window =Tk()       
    application = Product(window)
    window.mainloop()