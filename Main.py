import tkinter as tk
from tkinter import filedialog


def open_file_dialog():
    print("hi")
# Crear la ventana principal de Tkinter
window = tk.Tk()

# Crear un menú
menu = tk.Menu(window)
window.config(menu=menu)

# Crear un submenú "Archivo"
file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir Base de Datos", command=open_file_dialog)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)

# Mostrar la ventana
window.mainloop()
