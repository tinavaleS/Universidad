
from ast import main
from importlib import import_module
from tkinter import ttk
from tkinter import *
import tkinter
from indexController import *

# FUNCIONES
def Enteros():
    ventanaTexto = tkinter.Tk()
    ventanaTexto.geometry("100x50")
    titulo = tkinter.Label(ventanaTexto, text = "Ingrese número entero", bg= "CadetBlue")
    titulo.pack(fill = tkinter.X)
    cajaTexto =  tkinter.Entry(ventanaTexto)
    cajaTexto.pack()

    botonEnviar = tkinter.Button(ventanaTexto,text="Enviar",command=lambda: validarEntero(cajaTexto.get()))
    botonEnviar.pack()
    ventanaTexto.mainloop()



class Main:
    ventana = tkinter.Tk()
    ventana.title('Expresiones Regulares')
    ventana.geometry("400x300")
    titulo = tkinter.Label(ventana, text = "Expresiones Regulares", bg= "CadetBlue")
    titulo.pack(fill = tkinter.X)

    botonEntero = tkinter.Button(ventana, text="Enteros", padx=10, pady=10, command= lambda: Enteros())
    botonEntero.pack()

    botonReal = tkinter.Button(ventana, text="Reales", padx=10, pady=10)
    botonReal.pack()

    botonNotacion = tkinter.Button(ventana, text="Notación", padx=10, pady=10)
    botonNotacion.pack()
    
    botonCorreo = tkinter.Button(ventana, text="Correo", padx=10, pady=10)
    botonCorreo.pack()

    ventana.mainloop()






    


    








        


 

      