import time
import smtplib
from email.message import EmailMessage

#Declaro el correo y contraseña
Emisor = "luisalbertodejesusv883@gmail.com"
Contrasena = "qfurqdaeaamepcer"
Receptor = "t1513600321@unitru.edu.pe"

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