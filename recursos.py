import tkinter
from tkinter import messagebox
import datetime
from openpyxl import load_workbook
def guardar_datos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada,observacion_entrada,fecha_salida_indefinida):
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
    observacion_value = observacion_entrada.get()
    #fecha_salida_indefinida_value = fecha_salida_indefinida.get()
    '''print(tipo_habitacion_value)
    print(estado_value)
    print(num_doc_value)
    print(nombre_value)
    print(apellido_value)
    print(num_boleta_value)
    print(telefono_value)'''

    mensaje = f"Tipo de Habitación: {tipo_habitacion_value}\nEstado: {estado_value}\nN° Documento: {num_doc_value}\nNombres: {nombre_value}\nApellidos: {apellido_value}\nN° Boleta: {num_boleta_value}\nTeléfono: {telefono_value}\nFecha de Ingreso: {fecha_ingreso_value}\nFecha de Salida: {fecha_salida_value}\nObservación: {observacion_value}"
    print(mensaje)
    tkinter.messagebox.showinfo("Datos ingresados", mensaje)
    
    llenar_excel(tipo_habitacion_value,estado_value,num_doc_value,nombre_value,apellido_value,num_boleta_value,telefono_value,fecha_ingreso_value,fecha_salida_value,observacion_value,fecha_salida_indefinida)

    # Limpiar los campos
    limpiar_campos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada,observacion_entrada,fecha_salida_indefinida)

def limpiar_campos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada,observacion_entrada,fecha_salida_indefinida):
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
    observacion_entrada.delete(0, tkinter.END)
    # Desmarcar la opción de "fecha indefinida"
    fecha_salida_indefinida.deselect()
    #fecha_ingreso_entrada.set_date("")
    #fecha_salida_entrada.set_date("")

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

    # Crear widget para la opción de fecha de salida indefinida
    fecha_salida_indefinida = tkinter.Checkbutton(user_info_frame, text="Fecha de salida indefinida")
    fecha_salida_indefinida.grid(row=6, column=3)

    # Definir función para actualizar fecha de salida mínima
    def actualizar_fecha_salida_minimo(evento):
        try:
            fecha_ingreso = evento.widget.get_date()
            fecha_salida_entrada.config(validate="none")

            if not fecha_salida_indefinida.get():
                fecha_salida_entrada.config(
                    mindate=fecha_ingreso,
                    year=fecha_ingreso.year,
                    month=fecha_ingreso.month,
                    day=fecha_ingreso.day
                )
                fecha_salida_entrada.config(validate="key")       
            else:
                fecha_salida_entrada.delete(0, tkinter.END)

            fecha_salida_entrada.set_date(fecha_salida_entrada.get_date())

        except AttributeError:
            pass
    # Vincular función con el evento de selección de fecha de ingreso
    fecha_ingreso_entrada.bind("<<DateEntrySelected>>", actualizar_fecha_salida_minimo)
    print('Fecha salida indefinida → ',fecha_salida_indefinida)
    # Devolver los widgets
    return fecha_ingreso_entrada, fecha_salida_entrada ,fecha_salida_indefinida

def llenar_excel(tipo_habitacion_value,estado_value,num_doc_value,nombre_value,apellido_value,num_boleta_value,telefono_value,fecha_ingreso_value,fecha_salida_value,observacion_value,fecha_salida_indefinida_value):
    # Carga el archivo de Excel
    workbook = load_workbook(filename='hotel.xlsx')

    # Crea una nueva hoja en el archivo de Excel
    if 'Registro de clientes' in workbook.sheetnames:
        sheet = workbook['Registro de clientes']
    else:
        sheet = workbook.create_sheet('Registro de clientes')

    sheet['A2'] = tipo_habitacion_value
    sheet['B2'] = estado_value
    sheet['C2'] = num_doc_value
    sheet['D2'] = nombre_value
    sheet['E2'] = apellido_value
    sheet['F2'] = num_boleta_value
    sheet['G2'] = telefono_value
    sheet['H2'] = fecha_ingreso_value
    if not fecha_salida_indefinida_value:
        sheet['I2'] = fecha_salida_value
    else:
        sheet['I2'] = "Indefinido"
    sheet['J2'] = observacion_value

# Guarda el libro de trabajo de Excel en un archivo
    workbook.save('hotel.xlsx')
    workbook.close()