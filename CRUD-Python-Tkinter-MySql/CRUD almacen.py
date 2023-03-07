# Importando librerias

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# ventana

root = Tk()
root.title("App con BBDD para almacen")
root.geometry("600x350")

# variables

productoId = StringVar()
productoNombre = StringVar()
productoCantidad = StringVar()
productoPrecio = StringVar()

# conectar con la BBDD

def conexion():
    conexion = sqlite3.connect('almacen.db')
    miCursor = conexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE productos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(70) NOT NULL,
            CANTIDAD VARCHAR(70) NOT NULL,
            PRECIO VARCHAR(70) NOT NULL)
        ''')
        messagebox.showinfo("CONEXION","Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION","Conexion exitosa con la base de datos")

def eliminar():
    conexion = sqlite3.connect('almacen.db')
    miCursor = conexion.cursor()
    if askyesno(message='¿Desea eliminar los datos permanentemente?',title='CONEXION'):
        miCursor.execute("DROP TABLE productos")
    else:
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def limpiarCampos():
    productoId.set("")
    productoNombre.set("")
    productoCantidad.set("")
    productoPrecio.set("")

def informacion():
    acerca = '''
        Aplicacion para registro de productos
        Version: 1.0
        Tecnologia: Python-Tkinter-Sqlite3
    '''
    messagebox.showinfo(title="INFORMACION",message=acerca)

def salir():
    valor = messagebox.askquestion("SALIR","¿Estas seguro que desea salir?")
    if valor == "yes":
        root.destroy()

# CRUD

def crear():
    conexion=sqlite3.connect('almacen.db')
    miCursor=conexion.cursor()
    try:
        datos = productoNombre.get(),productoCantidad.get(),productoPrecio.get()
        miCursor.execute("INSERT INTO productos VALUES(NULL,?,?,?)",(datos))
        conexion.commit()
        messagebox.showinfo("CREATE", "Registro creado correctamente")
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def actualizar():
    conexion = sqlite3.connect('almacen.db')
    miCursor = conexion.cursor()
    try:
        datos = productoNombre.get(),productoCantidad.get(),productoPrecio.get()
        miCursor.execute("UPDATE productos SET NOMBRE=?,CANTIDAD=?,PRECIO=? WHERE ID="+productoId.get(),(datos))
        conexion.commit()
        messagebox.showinfo("UPDATE","Registro actualizado correctamente")
    except:
        messagebox.showinfo("UPDATE","Ocurrio un error al actualizar el registro")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def eliminar():
    conexion = sqlite3.connect('almacen.db')
    miCursor = conexion.cursor()
    try:
        if messagebox.askyesno(message="¿Desea eliminar el registro?",title="DELETE"):
            miCursor.execute("DELETE FROM productos WHERE ID="+productoId.get())
            conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al eliminar el registro")
        pass
    limpiarCampos()
    mostrarDatosEnTabla()

def mostrarDatosEnTabla():
    conexion = sqlite3.connect('almacen.db')
    miCursor = conexion.cursor()
    registros = tabla.get_children()

    for elemento in registros:
        tabla.delete(elemento)

    try:
        miCursor.execute("SELECT * FROM productos")
        for row in miCursor:
            tabla.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
    except:
        pass
   
# menus

menuBar = Menu(root)

menuBaseDatos = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Inicio',menu=menuBaseDatos)
menuBaseDatos.add_command(label='Crear/Conectar BBDD',command=conexion)
menuBaseDatos.add_command(label='Eliminar BBDD',command=eliminar)
menuBaseDatos.add_command(label='Salir',command=salir)

menuAyuda = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Ayuda',menu=menuAyuda)
menuAyuda.add_command(label='Resetear',command=limpiarCampos)
menuAyuda.add_command(label='Info App',command=informacion)

# entrys y labels

eId = Entry(root,textvariable=productoId)

lNombre = Label(root,text='Producto').place(x=50,y=10)
eNombre = Entry(root,width=50,textvariable=productoNombre).place(x=105,y=10)
lCantidad = Label(root,text='Cantidad').place(x=50,y=40)
eCantidad = Entry(root,width=15,textvariable=productoCantidad).place(x=105,y=40)
lPrecio = Label(root,text='Precio').place(x=270,y=40)
ePrecio = Entry(root,width=15,textvariable=productoPrecio).place(x=314,y=40)

# botones

botonCrear = Button(root,text="Crear Registro",command=crear)
botonCrear.place(x=20,y=100)
botonModificar = Button(root,text="Modificar Registro",command=actualizar)
botonModificar.place(x=150,y=100)
botonMostrarLista = Button(root,text="Mostrar Lista",command=mostrarDatosEnTabla)
botonMostrarLista.place(x=310,y=100)
botonMostrarLista = Button(root,text="Eliminar Registro",command=eliminar)
botonMostrarLista.place(x=440,y=100)

# tabla de registros

tabla = ttk.Treeview(height=10,columns=('#0','#1','#2'))
tabla.place(x=110,y=140)
tabla.column('#0',width=40)
tabla.heading('#0',text='ID',anchor=CENTER)
tabla.column('#1',width=150)
tabla.heading('#1',text='Producto',anchor=CENTER)
tabla.column('#2',width=80)
tabla.heading('#2',text='Cantidad',anchor=CENTER)
tabla.column('#3',width=80)
tabla.heading('#3',text='Precio',anchor=CENTER)


def seleccionClick(event):
    item = tabla.identify('item',event.x,event.y)
    productoId.set(tabla.item(item,'text'))
    productoNombre.set(tabla.item(item,'values')[0])
    productoCantidad.set(tabla.item(item,'values')[1])
    productoPrecio.set(tabla.item(item,'values')[2])

tabla.bind("<Double-1>",seleccionClick)



root.config(menu=menuBar)
root.mainloop()
