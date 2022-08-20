from tkinter import *

def cerrarInterfaz():
    arduino.close()
    control.destroy()

def encenderSIST():
    arduino.write(b'HIGH')
    time(1)

def apagarSIST():
    arduino.write(b'LOW')
    time(1)

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
encender = Button(botonesFrame, text = "ACTIVAR", bg = "green", fg = "white", font = ("ARIAL", 12),command = encenderSIST)
encender.place(x=100, y=40)

#boton de apagar
apagar = Button(botonesFrame, text = "APAGAR", bg = "red", fg = "white", font = ("ARIAL", 12),command = apagarSIST)
apagar.place(x=300, y=40)

#boton de Cerrar sistema
cerrar= Button(botonesFrame, text = ("Salir"),font = ("ARIAL", 14), command = cerrarInterfaz)
cerrar.place(x=440, y=80)

control.mainloop()