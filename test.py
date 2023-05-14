import json
import tkinter
import json
import time 


def buttonsubmission1(box1):
    ans = box1.get()
    print(ans)





    
window = tkinter.Tk()
window.geometry("1080x900")
title = tkinter.Label(window, text="Barberia JLU", font="30")
title.pack()


Clientboxtext = tkinter.Entry(window) ##caja de entrada de datos
Clientboxtext.pack()
client = buttonsubmission1(Clientboxtext)
client_button = tkinter.Button(window,text="Enviar",command=client)
client_button.pack()
window.mainloop()

