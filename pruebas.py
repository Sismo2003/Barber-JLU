import tkinter as tk
from tkinter import ttk

def search_and_select_value():
    search_text = search_entry.get()  # Obtener el texto de búsqueda
    column_index = 1  # Índice de la columna en la que deseas buscar (por ejemplo, 1 para la segunda columna)

    for item in treeview.get_children():
        item_values = treeview.item(item, "values")
        if item_values and len(item_values) > column_index:
            if item_values[column_index] == search_text:
                treeview.selection_set(item)  # Seleccionar automáticamente el elemento encontrado
                treeview.focus(item)  # Hacer que el elemento seleccionado sea visible si está fuera de la vista

                # Hacer que el elemento seleccionado sea visible utilizando el método see()
                treeview.see(item)

                return  # Terminar el bucle al encontrar el valor

root = tk.Tk()
root.title("Buscar, Seleccionar y Mover Scrollbar en Treeview")

treeview = ttk.Treeview(root, columns=("Columna1", "Columna2"))
treeview.heading("#1", text="Columna 1")
treeview.heading("#2", text="Columna 2")

# Agregar elementos al treeview (estos son solo ejemplos)
for i in range(20):
    treeview.insert("", "end", values=("Valor" + str(i), "Valor" + str(i)))

treeview.pack()

search_entry = ttk.Entry(root)
search_entry.pack()

search_button = ttk.Button(root, text="Buscar, Seleccionar y Mover Scrollbar", command=search_and_select_value)
search_button.pack()

# Crear un Scrollbar vertical
vertical_scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=vertical_scrollbar.set)
vertical_scrollbar.pack(side="right", fill="y")

root.mainloop()
