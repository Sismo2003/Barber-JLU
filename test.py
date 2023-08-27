import tkinter as tk
from tkinter import ttk

def update_spinbox_value(event, item, col_idx):
    new_value = spinbox_var.get()
    treeview.set(item, column=col_idx, value=new_value)

root = tk.Tk()
root.title("Spinbox en Treeview")

treeview = ttk.Treeview(root, columns=("Columna1", "Columna2"))
treeview.heading("#1", text="Columna 1")
treeview.heading("#2", text="Columna 2")

treeview.pack()

# Insertar un item con Spinbox en la segunda columna
item = treeview.insert("", "end", values=("Item 1", ""))

# Crear y agregar una Spinbox a la segunda columna del item
spinbox_var = tk.StringVar()
spinbox = tk.Spinbox(treeview, textvariable=spinbox_var, from_=0, to=100, command=lambda: update_spinbox_value("<<SpinboxModified>>", item, 1))
spinbox_window = treeview.create_window((0, 0), window=spinbox, anchor="w", tags=("spinbox",))
spinbox_var.set(0)  # Establecer valor inicial

# Configurar el ancho de la columna para que se ajuste a la Spinbox
treeview.column("#2", width=spinbox.winfo_reqwidth())

root.mainloop()
