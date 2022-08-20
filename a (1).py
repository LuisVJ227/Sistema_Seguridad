from tkinter import *
import time
import serial

Arduino = serial.Serial('COM5', 9600)
time.sleep(0.01)


def encender():
    print('a'.encode())
    Arduino.write('a'.encode())
    time.sleep(0.01)


def apagar():
    Arduino.write('b'.encode())
    time.sleep(0.01)


def cerrarInterfaz():
    Arduino.close()
    control.destroy()

control = Tk()

control.geometry("500x200")
control.title('control de sistema')

titleFrame = Frame()
titleFrame.config(bg = "yellow", width = "500", height = "80")
titleFrame.place(x=0, y=0)
#titulo
lbltitulo = Label(titleFrame, text = "ENCENDIDO Y APAGADO DE SISTEMA", bg = "yellow", font =("ARIAL", 15))
lbltitulo.place(x=70, y=20)

botonesFrame = Frame()
botonesFrame.config(bg = "orange", width = "500", height = "120")
botonesFrame.place(x=0, y=80)

#boton de encender
encender_c = Button(botonesFrame, text = "ACTIVAR", bg = "green", fg = "white", font = ("ARIAL", 12), command = lambda:encender())
encender_c.place(x=100, y=40)

#boton de apagar
apagar_c = Button(botonesFrame, text = "APAGAR", bg = "red", fg = "white", font = ("ARIAL", 12), command = lambda:apagar())
apagar_c.place(x=300, y=40)

#boton de Cerrar sistema
cerrar= Button(botonesFrame, text = ("Salir"),font = ("ARIAL", 14), command = lambda:cerrarInterfaz())
cerrar.place(x=440, y=80)

control.mainloop()

