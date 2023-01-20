from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ''  # La utilizaremos para almacenar información

def nuevo():
    global ruta 
    mensaje.set("Nuevo fichero")
    ruta = ''
    texto.delete(1.0, "end")
    root.title("Editor M")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', filetypes=(
        ("Fichero de texto","+.txt"),), title="Abrir un fichero de texto.")     
if ruta != "":
    fichero = open(ruta, 'r')
    contenido = fichero.read()
    texto.delete(1.0, 'end')
    texto.insert('insert', contenido)
    fichero.closed()
    root.title(ruta + " - Editor M")




def guardar():
    global ruta
    if ruta !="":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardar Correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero",
     mode="w", defaultextension=".txt")
    

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, '+w')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardar correctamente")
    else:
        mensaje.set("Guardado cancelado")



# Configuracion de la Raiz
root = Tk()
root.title("Editor M")

#menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)

filemenu.add_separator()

filemenu.add_command(label="salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

# Caja de texto 
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))


# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenidos a tu editor M")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()