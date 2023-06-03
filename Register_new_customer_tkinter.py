import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
from Register_new_customer_tkinter_backend import NewClient
import time


with open("hair_products.json", "r") as file:
    hair_products_list = json.load(file)

with open("alternave_services.json", "r") as file:
    alternave_services_json = json.load(file)

def submtion_data ():
    firstName = first_name_entry.get()
    lastName = last_name_entry.get()
    final_client = firstName+" "+lastName
    birthday = final_result.get()
    phoneNumber = phone_number_entry.get()
    email = email_entry.get()
    email.lower()
    hairCutFrequency = hair_cut_frequency_entry.get()
    hairCutStyle = hair_cut_style_entry.get()
    hairProducts = hair_products_combobox.get()
    barberName = barber_name_entry.get()
    barberName.title()
    alternaveServices = alternave_services_combobox.get()
    observations = observations_entry.get()
    observations.capitalize()
    #attendances = datetime.date.today()
    #print(f"Nombre: {firstName} {lastName}   fecha de nacimiento: {birthday} ")
    #print(f"Tel. {phoneNumber}   Correo Electronico: {email}")
    #print(f"Frecuencia de corte: {hairCutFrequency}  Productos ocurrentes: {hairProducts}")
    #print(f"Corte: {hairCutStyle}   Barbero: {barberName}")
    #print(f"Servios alternos: {alternaveServices}  observaciones: {observations}")
    

    NewClient(final_client,barberName,hairCutStyle,hairProducts,birthday,phoneNumber,observations,email,alternaveServices,hairCutFrequency)
    


#Main Window
window = tkr.Tk()
window.title("Registrar un Nuevo Cliente ") 
MainFrame = tkr.Frame(window);
MainFrame.pack()


##########################Client information #################################
client_info_frame = tkr.LabelFrame(MainFrame,text="Información del Cliente")
client_info_frame.grid(row=0,column=0,sticky="news", padx=20,pady=10)

first_name_label = tkr.Label(client_info_frame,text="Nombre: ")
first_name_label.grid(row=0,column=0)
first_name_entry = tkr.Entry(client_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_label = tkr.Label(client_info_frame,text="Apellído: ")
last_name_label.grid(row=0,column=1)
last_name_entry = tkr.Entry(client_info_frame)
last_name_entry.grid(row=1,column=1)

final_result = tkr.StringVar()
birthday_label = tkr.Label(client_info_frame,text="Fecha de Nacimiento: ")
birthday_label.grid(row=0,column=3)
birthday_entry = DateEntry(client_info_frame,selectmode="day",textvariable=final_result)
birthday_entry.grid(row=1, column= 3, padx=20)

phone_number_label = tkr.Label(client_info_frame,text="Numero Telefonico: ")
phone_number_label.grid(row=2 ,column=0)
phone_number_entry = tkr.Entry(client_info_frame)
phone_number_entry.grid(row=3,column=0)

email_label = tkr.Label(client_info_frame,text="Correo Electronico:")
email_label.grid(row=2,column=1)
email_entry = tkr.Entry(client_info_frame)
email_entry.grid(row=3,column=1)

for widget in client_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5);

######################### #Barber Information #########################

barber_information = tkr.LabelFrame(MainFrame,text="Información del Corte")
barber_information.grid(row=1,column=0,sticky="news", padx=20,pady=10)

hair_cut_style_label = tkr.Label(barber_information,text="Estilo de Corte: ")
hair_cut_style_label.grid(row=0,column=0)
hair_cut_style_entry = tkr.Entry(barber_information)
hair_cut_style_entry.grid(row=1,column=0);

hair_cut_frequency_label=tkr.Label(barber_information,text="Frecuencia de Corte: ")
hair_cut_frequency_label.grid(row=0,column=1)
hair_cut_frequency_entry = tkr.Entry(barber_information)
hair_cut_frequency_entry.grid(row=1,column=1)

hair_products_label = tkr.Label(barber_information,text="Productos Utilizados: ")
hair_products_label.grid(row=0,column=2);
hair_products_combobox = ttk.Combobox(barber_information, values=hair_products_list)
hair_products_combobox.grid(row=1,column=2)

barber_name_label = tkr.Label(barber_information,text="Nombre del Barbero")
barber_name_label.grid(row=2,column=0)
barber_name_entry = ttk.Combobox(barber_information, values=["Salvador Venegas","Lalo","Otro..."])
barber_name_entry.grid(row=3,column=0)

alternave_services_label = tkr.Label(barber_information,text="Servicios Alternos")
alternave_services_label.grid(row=2,column=1)
alternave_services_combobox = ttk.Combobox(barber_information, values=alternave_services_json)
alternave_services_combobox.grid(row=3,column=1)



for widget in barber_information.winfo_children():
    widget.grid_configure(padx=10,pady=5);


############ OBSERVATIONS ###########

client_observations_frame = tkr.LabelFrame(MainFrame,text="Observaciones del Cliente")
client_observations_frame.grid(row=3,column=0,sticky="news", padx=20,pady=10)

observations_label = tkr.Label(client_observations_frame,text="Observaciones :")
observations_label.grid(row=0,column=0)
observations_entry = tkr.Entry(client_observations_frame)
observations_entry.grid(row=1,column=0)
for widget in client_observations_frame.winfo_children():
    widget.grid_configure(padx=100,pady=5);


submtion_button = tkr.Button(MainFrame,text="Enviar Datos",command=submtion_data)
submtion_button.grid(row=0,column=2,sticky="news",padx=20,pady=20)

window.
window.mainloop()
exit()