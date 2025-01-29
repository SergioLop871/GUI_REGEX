# Sergio Jair López Núñez
# 27/01/2025
# Profesor: Luis Felipe Muñoz Mendoza
# Actividad 2: GUI Expresiones Regulares

# Importar el módulo de tkinter para realizar la GUI
import tkinter as tk
from tkinter import ttk
# Importar messagebox para mostrar mensajes emergentes
from tkinter import messagebox
# Importar el módulo de REGEX para validar los datos
import re

# Función que se ejecuta al seleccionar una opción en el Combobox
def select(event):
    selected_item = combo_box.get()
    label.config(text = selected_item)
    entry.delete(0, "end")

# Función para validar los distintos tipos de datos mediante REGEX
def validate_string():
    # Obtener el tipo de dato a validar
    data_type = data_type_var.get()

    # Obtener la entrada del usuario
    input = input_var.get()

    # Variable para controlar si la entrada es válida o inválida
    valid = False

    # Diccionario de expresiones regulares
    regex_patterns = {"telefono": r"^\d{10}$",
                      "email": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}\b",
                      "curp": r"^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$",
                      "rfc": r"^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))([A-Z\d]{3})?$",
                      "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                      "fecha": r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))(\4(?:(?:1[6-9]|[2-9]\d)?\d{2}))$"
                    }

    # Usar REGEX para validar el tipo de dato seleccionado
    if data_type == "Teléfono":
        # Teléfono REGEX
        if re.fullmatch(regex_patterns.get("telefono"), input):
            valid = True
        print(f"Se validó Teléfono\nREGEX: {regex_patterns.get('telefono')}")
    elif data_type == "Email":
        # Email REGEX
        if re.fullmatch(regex_patterns.get("email"), input):
            valid = True
        print(f"Se validó Email\nREGEX: {regex_patterns.get('email')}")
    elif data_type == "CURP":
        # CURP REGEX
        print(input)
        if re.fullmatch(regex_patterns.get("curp"), input):
            valid = True
        print(f"Se validó CURP\nREGEX: {regex_patterns.get('curp')}")
    elif data_type == "RFC":
        # RFC (Persona física / Persona Moral) REGULAR
        if re.fullmatch(regex_patterns.get("rfc"), input):
            valid = True
        print(f"Se validó RFC\nREGEX: {regex_patterns.get('rfc')}")
    elif data_type == "IPv4":
        # Dirección IPv4 REGEX
        if re.fullmatch(regex_patterns.get("ipv4"), input):
            valid = True
        print(f"Se validó IPv4\nREGEX: {regex_patterns.get('ipv4')}")
    else:
        # Fecha de cumpleaños DD/MM/AA
        if re.fullmatch(regex_patterns.get("fecha"), input):
            valid = True
        print(f"Fecha de Cumpleaños\nREGEX: {regex_patterns.get('fecha')}")
    
    # Mostrar ventana emergente con el resultado de la validación
    if valid:
        messagebox.showinfo(message = "Validación Exitosa")   
    else:
        messagebox.showerror(message = "Validación Fallida")

    
# Crear la ventana principal (contenedor)
root = tk.Tk()

#----- Establecer las propiedades de la ventana -----#
# Establecer el nombre de la ventana
root.title("Validación de Datos (REGEX)")
# Fijar el tamaño de la ventana
root.geometry("600x300")
# Establecer que la ventana no sea redimensionable ni en la dirección X ni Y
root.resizable(False, False)
# Cambiar el color del fondo
root.configure(bg = "lightblue")

""" Declarar variables tipo string para almacenar:
    1. Tipo de dato a validar
    2. Entrada del usuario
"""
data_type_var = tk.StringVar()
input_var = tk.StringVar()

"""Agregar los widgets (con diseño) necesarios para el diseño genérico de la GUI:
    1. Combobox
    2. Label
    3. Entry
    4. Button
"""
# Cambiar el tema actual de los widgets de la GUI a 'clam'
style = ttk.Style()
style.theme_use('clam')

# Crear el Combobox (y aplicar estilo) para la selección del tipo de dato a validar de una lista
combo_box = ttk.Combobox(root, textvariable = data_type_var, state = "readonly", font = ("Arial", 30))
# Añadir la lista desplegable al Combobox
combo_box["values"] = ("Teléfono", "Email", "CURP", "RFC", "IPv4", "Fecha de Cumpleaños")
# Establecer el valor "Teléfono" como default en el combobox
combo_box.current(0)

# Vincular evento a la selección
combo_box.bind("<<ComboboxSelected>>", select)

# Crear el label
label = tk.Label(root, text = combo_box.get(), font = ("Arial", 30, "bold"), bg = "black", fg = "white")
# Crear el campo donde el usuario introducirá la cadena
entry = tk.Entry(root, textvariable = input_var, font = ("Arial", 30))
# Crear el botón que llamará a la función para validar la cadena
check_button = tk.Button(root,
                         text = 'Verificar',
                         command = validate_string,
                         font = ("Arial", 30),
                        )

# Posicionar los widgets en coordenadas específicas
combo_box.place(x = 120, y = 25)
label.place(x = 120, y = 100)
entry.place(x = 120, y = 150)
check_button.place(x = 220, y = 225)

# Método para correr la aplicación
root.mainloop()