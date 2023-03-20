# Importando las librerias

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Ventana

root = Tk()
root.title('App con BBDD en Sqlite3')
root.geometry('600x350')

# Variables

numId = StringVar()
nombreAlumno = StringVar()
apellidoAlumno = StringVar()
telAlumno = StringVar()
direcAlumno = StringVar()

# Funciones

# Conectar con BBDD

def conexion():
    conexion = sqlite3.connect('escuela.db')
    miCursor = conexion.cursor()

    try:
        miCursor.execute('''
                CREATE TABLE alumnos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL,
                APELLIDO VARCHAR(50) NOT NULL,
                TELEFONO VARCHAR(50) NOT NULL,
                DIRECCION VARCHAR(50) NOT NULL)
        ''')
        messagebox.showinfo('CONEXION',"Base de datos creada exitosamente")
    except:
        messagebox.showinfo('CONEXION',"Conexion exitosa con la base de datos")


# Eliminar BBDD

def eliminar():
    conexion = sqlite3.connect('escuela.db')
    miCursor = conexion.cursor()
    if messagebox.askyesno(message='¿Desea eliminar los datos permanentemente?',title='ELIMINAR'):
        miCursor.execute("DROP TABLE alumnos")
    else:
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

# Salir de la Aplicacion

def salir():
    valor = messagebox.askquestion("SALIR","¿Esta seguro que desea salir?")
    if valor == "yes":
        root.destroy

# Limpiar Campos

def limpiarCampos():
    numId.set("")
    nombreAlumno.set("")
    apellidoAlumno.set("")
    telAlumno.set("")
    direcAlumno.set("")

# Informacion de la aplicacion

def informacion():
    acerca = '''
        Aplicacion para registro de Alumnos
        Version: 1.0
        Tecnologia: Python-Tkinter-Sqlite3
        '''


# CRUD (Create(crear) - Read(leer) - Update(actualizar) - Delete(eliminar))

def crearRegistro():
    conexion=sqlite3.connect("escuela.db")
    miCursor=conexion.cursor()
    try:
        datos=nombreAlumno.get(),apellidoAlumno.get(),telAlumno.get(),direcAlumno.get()
        miCursor.execute("INSERT INTO alumnos VALUES(NULL,?,?,?,?)", (datos))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def actualizarRegistro():
    conexion = sqlite3.connect('escuela.db')
    miCursor = conexion.cursor()
    try:
        datos = nombreAlumno.get(),apellidoAlumno.get(),telAlumno.get(),direcAlumno.get()
        miCursor.execute("UPDATE alumnos SET NOMBRE=?,APELLIDO=?,TELEFONO=?,DIRECCION=? WHERE ID="+numId.get(), (datos))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al actualizar el registro")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def borrarRegistro():
    conexion = sqlite3.connect('escuela.db')
    miCursor = conexion.cursor()
    try:
        if messagebox.askyesno(message="¿Desea eliminar el registro definitivamente?",title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM alumnos WHERE ID="+numId.get())
            conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al tratar de eliminar el registro")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def mostrarDatosEnTabla():
    conexion = sqlite3.connect('escuela.db')
    miCursor = conexion.cursor()
    registros = tabla.get_children()

    for elemento in registros:
        tabla.delete(elemento)
        
    try:
        miCursor.execute("SELECT * FROM alumnos")
        for row in miCursor:
            tabla.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass

'''def seleccionClick(event):
    item=tabla.identify('item',event.x,event.y)
    numId.set(tabla.item(item,'text'))
    nombreAlumno.set(tabla.item(item,'values')[0])
    apellidoAlumno.set(tabla.item(item,'values')[1])
    direcAlumno.set(tabla.item(item,'values')[2])
    telAlumno.set(tabla.item(item,'values')[3])

tabla.bind("<Double-1>",seleccionClick)'''


    
# Widgets de la Pagina

# Menu de la pagina

menuBar = Menu(root)


menuBaseDeDatos = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Inicio",menu=menuBaseDeDatos)
menuBaseDeDatos.add_command(label="Crear/Conectar BBDD",command=conexion)
menuBaseDeDatos.add_command(label="Eliminar BBDD",command=eliminar)
menuBaseDeDatos.add_command(label="Salir",command=salir)

menuAyuda = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Resetear",command=limpiarCampos)
menuAyuda.add_command(label="Info App",command=informacion)


# Labels y Entrys de la pagina

entry1 = Entry(root,textvariable=numId)

label2 = Label(root,text="Nombre")
label2.place(x=50,y=10)
entry2 = Entry(root, width=50,textvariable=nombreAlumno)
entry2.place(x=105,y=10)

label3 = Label(root,text="Apellido")
label3.place(x=50,y=40)
entry3 = Entry(root, width=50,textvariable=apellidoAlumno)
entry3.place(x=105,y=40)

label4 = Label(root,text="Telefono")
label4.place(x=50,y=70)
entry4 = Entry(root, width=50,textvariable=telAlumno)
entry4.place(x=105,y=70)

label5 = Label(root,text="Direccion")
label5.place(x=50,y=100)
entry5 = Entry(root, width=50,textvariable=direcAlumno)
entry5.place(x=105,y=100)

# Botones

botonCrear = Button(root,text="Crear Registro",command=crearRegistro)
botonCrear.place(x=20,y=130)
botonModificar = Button(root,text="Modificar Registro",command=actualizarRegistro)
botonModificar.place(x=150,y=130)
botonMostrarLista = Button(root,text="Mostrar Lista",command=mostrarDatosEnTabla)
botonMostrarLista.place(x=310,y=130)
botonMostrarLista = Button(root,text="Eliminar Registro",command=borrarRegistro)
botonMostrarLista.place(x=440,y=130)

# Tabla de registros

tabla = ttk.Treeview(height=10,columns=('#0','#1','#2','#3'))
tabla.place(x=0,y=170)
tabla.column('#0',width=40)
tabla.heading('#0',text='ID',anchor=CENTER)
tabla.column('#1',width=150)
tabla.heading('#1',text='Nombre',anchor=CENTER)
tabla.column('#2',width=150)
tabla.heading('#2',text='Apellido',anchor=CENTER)
tabla.column('#3',width=90)
tabla.heading('#3',text='Telefono',anchor=CENTER)
tabla.column('#4',width=170)
tabla.heading('#4',text='Direccion',anchor=CENTER)

def seleccionClick(event):
    item=tabla.identify('item',event.x,event.y)
    numId.set(tabla.item(item,'text'))
    nombreAlumno.set(tabla.item(item,'values')[0])
    apellidoAlumno.set(tabla.item(item,'values')[1])
    direcAlumno.set(tabla.item(item,'values')[2])
    telAlumno.set(tabla.item(item,'values')[3])

tabla.bind("<Double-1>",seleccionClick)


root.config(menu=menuBar)
root.mainloop()

