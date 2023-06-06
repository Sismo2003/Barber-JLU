import tkinter as tk

ventana = tk.Tk()
ventana.title("Mostrar Texto en Ventana")

texto = tk.Text(ventana)
texto.pack()

texto.insert(tk.END, "¡Hola, mundo!\n")
texto.insert(tk.END, "Este es un ejemplo de texto en una ventana de Tkinter.")

ventana.mainloop()