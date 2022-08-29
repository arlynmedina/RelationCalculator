#Parte de la interfaz
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import functions
from random import randint
import random
import tkinter.font as tkFont

#Lista que el usuario ingresará primero
conjunto = []

def agregar_elemento(entry, conjunto):
        elemento = int(entry.get())
        if elemento not in conjunto:
                conjunto.append(int(elemento))
        entry.delete(0,END)
        
def eliminar_elemento(entry, conjunto):
        conjunto.pop(-1)
        entry.delete(0,END)
        
def agregar_conjunto_random(entry, conjunto, num):
    conjunto.clear()
    i=0
    while i < int(num):
        elemento = randint(1, 100)
        if elemento not in conjunto:
                conjunto.append(int(elemento))
        i+=1
                
                
        entry.delete(0,END)
    
def limpiar_conjuntos(conjunto1):
        conjunto.clear()

#Ventana Final que se le presentará al usuario cuando se haya escogido la relación
def Resultado(OpcionesWindow, Pares,):
        ResultadoWindow = tk.Toplevel(OpcionesWindow)
        ResultadoWindow.focus()
        ResultadoWindow.grab_set()
        ResultadoWindow.title('Opciones de Relaciones')
        ResultadoWindow.geometry('640x260')
        OpcionesWindow.withdraw()

        Label1 = Label(ResultadoWindow, text = "Pares que cumplen con la relación:",font= "Helvetica 15 bold")
        Label1.place(x=15, y=5)
        imprimir = scrolledtext.ScrolledText(ResultadoWindow, font= "Helvetica 13", width=20, height=10)
        for i in range(len(Pares)):
            imprimir.insert(tk.INSERT, (i+1,Pares[i]))
            imprimir.insert(tk.INSERT, '\n')
        imprimir.configure(state ='disabled')
        imprimir.place(x=30, y=50)
        Label2 = Label(ResultadoWindow, text= "Determinación de Relación: ", font= "Helvetica 15 bold")
        Label2.place(x=350, y=5)
        Label3 = Label(ResultadoWindow, text= "Reflexiva ")
        Label3.place(x=355, y=40)
        Label4 = Label(ResultadoWindow, text= "Simétrica ")
        Label4.place(x=355, y=75)
        Label5 = Label(ResultadoWindow, text= "Transitiva ")
        Label5.place(x=355, y=110)
        Label6 = Label(ResultadoWindow, text= "Equivalencia ")
        Label6.place(x=355, y=145)
        ReturnBoton = Button(ResultadoWindow, text= "Regresar", height=1, width=15, command = lambda:[ResultadoWindow.destroy(), Pares.clear(),opciones_relaciones(OpcionesWindow, conjunto)])
        ReturnBoton.place(x=45, y= 220)
        labelR = Label(ResultadoWindow, text = functions.RelacionReflexiva(Pares))
        labelR.place(x=430 , y=40)
        labelS = Label(ResultadoWindow, text = functions.RelacionSimetrica(Pares))
        labelS.place(x=430 , y=75)
        labelT = Label(ResultadoWindow, text = functions.RelacionTransitiva(Pares))
        labelT.place(x=430 , y=110)
        labelE = Label(ResultadoWindow, text = functions.RelacionEquivalencia(functions.RelacionReflexiva(Pares), functions.RelacionSimetrica(Pares), functions.RelacionTransitiva(Pares)))
        labelE.place(x=450, y=145)
        
def opciones_relaciones(mainWindow, conjunto):
        OpcionesWindow = tk.Toplevel(mainWindow)
        OpcionesWindow.focus()
        OpcionesWindow.grab_set()
        OpcionesWindow.title('Opciones de Relaciones')
        OpcionesWindow.geometry('335x325')
        mainWindow.withdraw()

        Label1 = Label(OpcionesWindow, text="Tipos de Relaciones", font= "Helvetica 15 bold")
        Label1.place(x=90, y=10)
        BotonMayor = tk.Button(OpcionesWindow,text='Mayor o igual que',width=25,height=2, command = lambda: [Resultado(OpcionesWindow,functions.MayorIgualQue(functions.ProductoCartesiano(conjunto)))])
        BotonMayor.place(x=50, y=50)
        BotonMenor = tk.Button(OpcionesWindow,text='Menor o igual que',width=25,height=2, command = lambda: [Resultado(OpcionesWindow,functions.MenorIgualQue(functions.ProductoCartesiano(conjunto)))])
        BotonMenor.place(x=50, y=100)
        BotonIgual = tk.Button(OpcionesWindow,text='Igual',width=25,height=2, command = lambda: [Resultado(OpcionesWindow, functions.Igual(functions.ProductoCartesiano(conjunto)))])
        BotonIgual.place(x=50, y=150)
        BotonMultiplos = tk.Button(OpcionesWindow,text='Multiplos',width=25,height=2, command = lambda: [Resultado(OpcionesWindow, functions.Multiplos(functions.ProductoCartesiano(conjunto)))])
        BotonMultiplos.place(x=50, y=200)
        Boton5 = tk.Button(OpcionesWindow,text='Doble',width=25,height=2, command = lambda: [Resultado(OpcionesWindow, functions.Doble(functions.ProductoCartesiano(conjunto)))])
        Boton5.place(x=50, y=250)
        ReturnBoton = Button(OpcionesWindow, text= "Regresar", height=1, width=15, command = lambda:[OpcionesWindow.destroy(), conjunto.clear(), calcWindow(mainWindow, 0)])
        ReturnBoton.place(x=90, y= 300)

def AcercaDe(parentwindow,mode):
    global focusedDisplay
    mainWindow = tk.Toplevel(parentwindow)
    mainWindow.focus()
    mainWindow.grab_set()
    mainWindow.geometry('500x250')
    parentwindow.withdraw()
    mainWindow.title('Información del programa')
    text2 = tk.StringVar()

    label1 = tk.Label(mainWindow,text="Creado por ", font='Helvetica 16')
    label1.place(x=180,y=20)
    label2 = tk.Label(mainWindow,text="Luis Raúl Acosta Mendoza", font='Helvetica 10')
    label2.place(x=150,y=50)
    label3 = tk.Label(mainWindow,text="Ana Carolina Arellano Valdez", font='Helvetica 10')
    label3.place(x=150,y=75)
    label4 = tk.Label(mainWindow,text="Arlyn Linette Medina García", font='Helvetica 10')
    label4.place(x=150,y=100)

    mainWindow.wait_window()
    parentwindow.deiconify()

def calcWindow(root, mode):
        global focusedDisplay
        mainWindow = tk.Toplevel(root)
        mainWindow.focus()
        mainWindow.grab_set()
        mainWindow.geometry('640x300')
        root.withdraw()

        def guardar_conjuntos():
                conjunto.sort()
                Label1 = Label(mainWindow, text= "Conjunto Final", font= "Helvetica 15 bold")
                Label1.place(x=300,y=75)
                mostrarconjunto = LabelFrame(mainWindow, text= "Conjunto Creado", font= "Helvetica 10 italic", width=310, height=34)
                c = Label(mostrarconjunto, text= conjunto, font= "Helvetica 10")
                mostrarconjunto.place(x=300, y=100)
                c.place(x=0, y=0)
                Limpiarboton = Button(mainWindow, text= "Borrar Conjunto", command = lambda: [limpiar_conjuntos(conjunto),guardar_conjuntos()])
                Limpiarboton.place(x=330, y= 140)
                Continuarboton = Button(mainWindow, text= "Continuar", command = lambda: [opciones_relaciones(mainWindow, conjunto)])
                Continuarboton.place(x=500, y=140)
        
        if mode == 0:
                Label1 = Label(mainWindow, text = "Opcion crear propio conjunto", font="Helvetica 15 bold")
                Label1.place(x=25, y=5)
                Label2 = Label(mainWindow, text = "Ingrese valores del conjunto:")
                Label2.place(x=40, y=30)
                ConjEntry = Entry(mainWindow)
                ConjEntry.place(x=40,y=60)
                AgregarBoton = Button(mainWindow, text = "Agregar valor", command = lambda: [agregar_elemento(ConjEntry, conjunto),guardar_conjuntos()])
                AgregarBoton.place(x=30, y=100)
                EliminarBoton = Button(mainWindow, text = "Eliminar valor", command = lambda: [eliminar_elemento(ConjEntry, conjunto),guardar_conjuntos()])
                EliminarBoton.place(x=150, y=100)
                Label3 = Label(mainWindow, text = "Opcion crear conjunto random", font="Helvetica 15 bold")
                Label3.place(x=25,y=135)
                ConjRandomLabel = Label(mainWindow, text= "Ingrese el tamaño del conjunto:")
                ConjRandomLabel.place(x=40, y=160)
                RandomConjEntry = Entry(mainWindow)
                RandomConjEntry.place(x=40, y=190)
                ConjRandom = Button(mainWindow, text = "Generar conjunto random", command = lambda: [agregar_conjunto_random(ConjEntry, conjunto,RandomConjEntry.get()),guardar_conjuntos()])
                ConjRandom.place(x=48, y=230)

                mainWindow.wait_window()
                root.deiconify()

           


root = tk.Tk()
root.title('Relaciones')
root.geometry('335x325')
title = tk.Label(root, text='Calculadora de Relaciones', font= 'Helvetica 15', width=20, height=3)
GenerateSet = tk.Button(root,
                             text='Generar Conjunto',
                             width=30,
                             height=3,
                             bg= 'cornflower blue',
                             command=lambda: calcWindow(root, 0))

about = tk.Button(root,
                  text='Acerca de',
                  width=30,
                  height=2,
                  bg= 'SkyBlue4',
                  command=lambda: AcercaDe(root, 1))


title.place(x=75, y=30)
GenerateSet.place(x=32, y=120)
about.place(x=32, y=200)
root.mainloop()
