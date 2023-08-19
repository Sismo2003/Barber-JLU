import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_selected_data():
    selected_item = treeview_y.focus()  # Obtener el elemento seleccionado
    if selected_item:
        item_data = treeview_y.item(selected_item, "values")  # Obtener los valores del elemento seleccionado
        if item_data:
            data_string = "\n".join(item_data)  # Crear una cadena con los datos
            messagebox.showinfo("Datos Seleccionados", data_string)  # Mostrar una ventana con los datos

root = tk.Tk()
root.title("Ejemplo Treeview con Ventana de Datos")

treeview_y = ttk.Treeview(root, columns=("Columna1", "Columna2"))
treeview_y.heading("#1", text="Columna 1")
treeview_y.heading("#2", text="Columna 2")

# Agregar elementos al treeview (estos son solo ejemplos)
treeview_y.insert("", "end", values=("Dato 1A", "Dato 1B"))
treeview_y.insert("", "end", values=("Dato 2A", "Dato 2B"))

treeview_y.pack()

button = ttk.Button(root, text="Mostrar Datos Seleccionados", command=show_selected_data)
button.pack()

root.mainloop()
