import tkinter
from tkinter import messagebox
def guardar_datos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada):
    # Obtener los valores ingresados
    tipo_habitacion_value = tipo_habitacion_combobox.get()
    estado_value = estado_combobox.get()
    num_doc_value = num_doc_entrada.get()
    nombre_value = nombre_entrada.get()
    apellido_value = apellido_entrada.get()
    num_boleta_value = num_boleta_entrada.get()
    telefono_value = telefono_entrada.get()
    fecha_ingreso_value = fecha_ingreso_entrada.get()
    fecha_salida_value = fecha_salida_entrada.get()

    '''print(tipo_habitacion_value)
    print(estado_value)
    print(num_doc_value)
    print(nombre_value)
    print(apellido_value)
    print(num_boleta_value)
    print(telefono_value)'''

    mensaje = f"Tipo de Habitación: {tipo_habitacion_value}\nEstado: {estado_value}\nN° Documento: {num_doc_value}\nNombres: {nombre_value}\nApellidos: {apellido_value}\nN° Boleta: {num_boleta_value}\nTeléfono: {telefono_value}\nFecha de Ingreso: {fecha_ingreso_value}\nFecha de Salida: {fecha_salida_value}"
    print(mensaje)
    tkinter.messagebox.showinfo("Datos ingresados", mensaje)

    # Limpiar los campos
    limpiar_campos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada)

def limpiar_campos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada):
    tipo_habitacion_combobox.set("")
    estado_combobox.set("")
    num_doc_entrada.delete(0, tkinter.END)
    nombre_entrada.delete(0, tkinter.END)
    apellido_entrada.delete(0, tkinter.END)
    num_boleta_entrada.delete(0, tkinter.END)
    telefono_entrada.delete(0, tkinter.END)
    fecha_ingreso_entrada.set_date("")
    fecha_salida_entrada.set_date("")