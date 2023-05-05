import tkinter
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from recursos import *

year=2023
month = 4
filename='RESERVA_ABRIL_2023_PRUEBA_CREACION.xlsx'

def open_register():
    # Muestra la ventana de registro de clientes
    window.deiconify()
    window_register.lift()
    window_register.focus_set()

def open_data():
    # Abre los datos de los clientes
    messagebox.showinfo("Datos de clientes", "Aquí estarían los datos de los clientes si los hubiera")

def boton_registrar():
    pass

workbook = main_excel(filename,year,month)

window = tkinter.Tk()
window.title("Formulario para hotel")

notebook = tk.ttk.Notebook(window)
notebook.pack()

lista_dias_inicial = conseguir_fechas(year,month)

for date in lista_dias_inicial:
    # Crea una nueva pestaña
    tab = tk.Frame(notebook)
    notebook.add(tab, text=f"{date[0]} {date[1]}")
    
    # Agrega la lista de fechas y días a la pestaña
    label = tk.Label(tab, text=f"{date[0]} {date[1]}")
    label.pack()

leer_excel(filename,tk,window)

# Crea los botones
button_register = tk.Button(window, text="Registrar", command=open_register)
button_data = tk.Button(window, text="Ver Datos", command=open_data)

# Añade los botones a la ventana
button_register.pack()
button_data.pack()

# Crea la ventana de registro de clientes
window_register = tk.Toplevel(window)
window_register.title("Formulario para hotel")
# ... sigue aquí el resto del código que ya tienes ...

# Oculta la ventana de registro de clientes al inicio
window_register.withdraw()

frame = tkinter.Frame(window)
frame.pack()

user_info_frame =tkinter.LabelFrame(frame, text="Registrar cliente")
user_info_frame.grid(row= 0, column=0, padx=40, pady=15)

tipo_habitacion = tkinter.Label(user_info_frame, text="Tipo de Habitación")
tipo_habitacion.grid(row=0, column=0)

tipo_habitacion_combobox = ttk.Combobox(user_info_frame,values=['Simple','Doble','Triple','Matrimonial','Suite'])
tipo_habitacion_combobox.grid(row=1, column=0)

estado = tkinter.Label(user_info_frame, text="Estado")
estado.grid(row=0, column=1)

estado_combobox = ttk.Combobox(user_info_frame,values=['Desocupado/Limpieza','Habilitada','Reservado','Almacén','Pagado','Ocupada'])
estado_combobox.grid(row=1, column=1)

num_doc = tkinter.Label(user_info_frame, text="Nª Documento")
num_doc.grid(row=0, column=2)

num_doc_entrada = tkinter.Entry(user_info_frame)
num_doc_entrada.grid(row=1, column=2)

nombre = tkinter.Label(user_info_frame, text="Nombres")
nombre.grid(row=2, column=0)

nombre_entrada = tkinter.Entry(user_info_frame)
nombre_entrada.grid(row=3, column=0)

apellido = tkinter.Label(user_info_frame, text="Apellidos")
apellido.grid(row=2, column=1)

apellido_entrada = tkinter.Entry(user_info_frame)
apellido_entrada.grid(row=3, column=1)

num_boleta = tkinter.Label(user_info_frame, text="Nª Boleta")
num_boleta.grid(row=2, column=2)

num_boleta_entrada = tkinter.Entry(user_info_frame)
num_boleta_entrada.grid(row=3, column=2)

telefono = tkinter.Label(user_info_frame, text="Telefono")
telefono.grid(row=4, column=0)

telefono_entrada = tkinter.Entry(user_info_frame)
telefono_entrada.grid(row=5, column=0)

fecha_ingreso_entrada, fecha_salida_entrada,cond_indefinido,fecha_salida_indefinida = crear_widgets(user_info_frame,DateEntry)

user_info_frame_observacion =tkinter.LabelFrame(frame, text="Observación", padx=10, pady=10)
user_info_frame_observacion.grid(row= 6, column=0, padx=40, pady=15)

observacion_entrada = tkinter.Entry(user_info_frame_observacion, width=90)
observacion_entrada.grid(row=7, column=0, sticky="W")

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=25, pady=5)

# Button
button = tkinter.Button(frame, text="Ingresar Datos", command=lambda: guardar_datos(tipo_habitacion_combobox,estado_combobox,num_doc_entrada,nombre_entrada,apellido_entrada,num_boleta_entrada,telefono_entrada,fecha_ingreso_entrada,fecha_salida_entrada,observacion_entrada,cond_indefinido,fecha_salida_indefinida))
button.grid(row=0, column=3, sticky="news", padx=20, pady=10)

window.mainloop()

#workbook.Close()
#excel.Quit()

