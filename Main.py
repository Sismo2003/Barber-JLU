import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x300')
columns = ('first_name', 'last_name', 'email','col1','col2','col3','col4','col5','col6','col7','col8')

frame = ttk.Frame()
frame.grid(row=0, column=0, sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

tree = ttk.Treeview(frame, columns=columns, show='headings')
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')
tree.heading('col1', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')
tree.heading('col4', text='col4')
tree.heading('col5', text='col5')
tree.heading('col6', text='col5')
tree.heading('col7', text='col7')
tree.heading('col8', text='col8')
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
for contact in contacts:
    tree.insert('', tk.END, values=contact)
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title='Information', message=','.join(record))
        
tree.bind('<<TreeviewSelect>>', item_selected)
scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
tree.configure(xscroll=scrollbar.set)
tree.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=1, column=0, sticky="new")




root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()