import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Formulario')

frame = tkinter.Frame(window)
frame.pack()

#Celda
info_user = tkinter.LabelFrame(frame, text='Datos del usuario')
info_user.grid(row=0,column=0,padx=80,pady=20)

#Nombre
nombre_fila = tkinter.Label(info_user, text='Nombre')
nombre_fila.grid(row=0,column=0)

#Apellido
apellido_fila = tkinter.Label(info_user, text='Apellido')
apellido_fila.grid(row=0,column=1)

nombre_entrada = tkinter.Entry(info_user)
apellido_entrada = tkinter.Entry(info_user)

nombre_entrada.grid(row=1,column=0)
apellido_entrada.grid(row=1, column=1)

#Titulo
titulo = tkinter.Label(info_user, text='titulo')
titulo_combobox = ttk.Combobox(info_user, values=['','Sr. ','Sra. ','Srta. '])
titulo.grid(row=0,column=2)
titulo_combobox.grid(row=1,column=2)

#Edad
edad_fila = tkinter.Label(info_user,text='Edad')
edad_spinbox = tkinter.Spinbox(info_user, from_=18,to=90)
edad_fila.grid(row=2,column=0)
edad_spinbox.grid(row=3, column=0)

#Nacionalidad
nacionalidad_fila = tkinter.Label(info_user, text='Nacionalidad')
nacionalidad_combox = ttk.Combobox(info_user, values=['Peruana','Extranjero'])
nacionalidad_fila.grid(row=2,column=1)
nacionalidad_combox.grid(row=3,column=1)

for widget in info_user.winfo_children():
    widget.grid_configure(padx=10,pady=5)

cursos_seccion = tkinter.LabelFrame(frame)
cursos_seccion.grid(row=1,column=0,sticky='news',padx=20,pady=20)

#Otra seccion
registro_fila = tkinter.Label(cursos_seccion,text='Estado del registro')
registro_check = tkinter.Checkbutton(cursos_seccion,text='Actualmente registrado')
registro_fila.grid(row=0,column=0)
registro_check.grid(row=1,column=0)

numero_doc_fila = tkinter.Label(info_user, text='Nª de Documento')
numero_doc_spinbox = tkinter.Spinbox(info_user, from_=10000000,to=99999999)
numero_doc_fila.grid(row=2,column=2)
numero_doc_spinbox.grid(row=3,column=2)

for widget in info_user.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    

window.mainloop()