import tkinter
from tkinter import messagebox
import datetime
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
    hoy = datetime.date.today().strftime('%d/%m/%Y')
    fecha_ingreso_entrada.set_date(hoy)
    fecha_salida_entrada.set_date(hoy)
    #fecha_ingreso_entrada.set_date("")
    #fecha_salida_entrada.set_date("")

def actualizar_fecha_salida_minimo(evento):
    fecha_ingreso = evento.widget.get_date()
    # fecha_salida_entrada.config(min_date=fecha_ingreso)

def crear_widgets(user_info_frame,DateEntry):
    # Crear widget de la fecha de ingreso
    fecha_ingreso = tkinter.Label(user_info_frame, text="Fecha Ingreso")
    fecha_ingreso.grid(row=4, column=1)

    fecha_ingreso_entrada = DateEntry(user_info_frame, date_pattern='dd/mm/yyyy')
    fecha_ingreso_entrada.grid(row=5, column=1)

    # Crear widget de la fecha de salida
    fecha_salida = tkinter.Label(user_info_frame, text="Fecha Salida")
    fecha_salida.grid(row=4, column=2)

    fecha_salida_entrada = DateEntry(user_info_frame, date_pattern='dd/mm/yyyy')
    fecha_salida_entrada.grid(row=5, column=2)

    # Definir función para actualizar fecha de salida mínima
    def actualizar_fecha_salida_minimo(evento):
        try:
            fecha_ingreso = evento.widget.get_date()
            fecha_salida_entrada.config(validate="none")
            fecha_salida_entrada.config(
                mindate=fecha_ingreso,
                year=fecha_ingreso.year,
                month=fecha_ingreso.month,
                day=fecha_ingreso.day
            )
            fecha_salida_entrada.config(validate="key")

            fecha_salida_entrada.set_date(fecha_salida_entrada.get_date())
        except AttributeError:
            pass
    # Vincular función con el evento de selección de fecha de ingreso
    fecha_ingreso_entrada.bind("<<DateEntrySelected>>", actualizar_fecha_salida_minimo)

    # Devolver los widgets
    return fecha_ingreso_entrada, fecha_salida_entrada

def llenar_excel(tipo_habitacion_value,estado_value,num_doc_value,nombre_value,apellido_value,num_boleta_value,telefono_value,fecha_ingreso_value,fecha_salida_value):

    print('')

