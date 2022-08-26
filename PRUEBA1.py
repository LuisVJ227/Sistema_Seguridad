from tkinter import *
import time 
import serial
import smtplib
from email.message import EmailMessage

Arduino = serial.Serial('COM5', 9600)
time.sleep(0.1)

def EnviarCorreo():
	#Declaro el correo y contraseña
    Emisor = "luisalbertodejesusv883@gmail.com"
    Contrasena = "qfurqdaeaamepcer"
    Receptor = "t1013600621@unitru.edu.pe"

    print("Iniciando envio")
    #Obteniendo la fecha y hora actual 
    Fecha = time.strftime("%d/%m/%y")
    Hora = time.strftime("%H:%M:%S")

    #Titulo del correo
    Asunto = "ALERTA DE SEGURIDAD"

    #Creando el mensaje que se quiere mandar
    Mensaje = "Alguien abrio la puerta el "+ Fecha + " a la hora " + Hora

    #Aspectos de mensaje
    em = EmailMessage()
    em["From"] = Emisor
    em["To"] = Receptor
    em["Subject"] = Asunto
    em.set_content(Mensaje)

    #Preparando el envio
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(Emisor, Contrasena)
        smtp.sendmail(Emisor, Receptor, em.as_string())

def encender():
    Arduino.write('a'.encode())
    time.sleep(0.1)

def apagar():
    Arduino.write('b'.encode())
    time.sleep(0.1)


def cerrarInterfaz():
    #Arduino.close()
    control.destroy()


control = Tk()

control.geometry("500x200")
control.title('control de sistema')


boton_1 = Label(control,  bg = 'green')
boton_1.place(x=20,y=50)

boton_2 = Label(control, bg = 'red')
boton_2.place(x=250,y=50)

#boton de encender
encender_c = Button(boton_1, text = "ACTIVAR", bg = "white", fg = "black", font = ("ARIAL", 20), command = lambda:encender())
encender_c.pack()

#boton de apagar
apagar_c = Button(boton_2, text = "APAGAR", bg = "white", fg = "black", font = ("ARIAL", 20), command = lambda:apagar())
apagar_c.pack()

control.mainloop()

while True:
    while(Arduino.inWaiting()==0):
        pass
        val = Arduino.readline()
        #Para ver los datos que arroja
        print(val)
        a = val.splitlines()
        b = str(a[0])
        c = b.replace("b","")
        d = c.replace("'","")
        e = int(d)
        print (e)

        if (e == 0):
         EnviarCorreo()
         print('ALERTA')
        time.sleep(0.5)
        time.sleep(0.1)
