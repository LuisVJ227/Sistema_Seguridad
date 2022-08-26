import time
import smtplib
import serial
from email.message import EmailMessage

Puerto = serial.Serial("COM5",9600)


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

while True:
    while(Puerto.inWaiting()==0):
        pass
        Dato = Puerto.readline()
        #Para ver los datos que arroja
        #print(Dato)
        a = Dato.splitlines()
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