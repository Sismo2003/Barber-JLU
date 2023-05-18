import tkinter  as tk 
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("380x200")  
sel=tk.StringVar() # declaring string variable 

cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=1,column=1,padx=20)

def my_upd(*args): # triggered when value of string varaible changes
    l1.config(text=sel.get()) # read and display date
l1=tk.Label(my_w,bg='yellow')  # Label to display date 
l1.grid(row=1,column=2)

sel.trace('w',my_upd) # on change of string variable 
my_w.mainloop()