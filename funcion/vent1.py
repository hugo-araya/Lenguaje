from tkinter import *
def ejemplo():
    label1.config(text='Hola '+caja.get())

ventana = Tk()
ventana.title('Mi ventana')
ventana.geometry('300x200+100+200')
label1 = Label(ventana,text = "Introduccion a Tkinter")
label1.grid(row=0 , column = 0)
boton1 = Button(ventana,text="Boton 1",relief=SOLID, command = ejemplo)
boton1.grid(row=0,column=1)
variable_string = StringVar()
caja = Entry(ventana,textvariable=variable_string)
caja.grid(row=1,column=1)
ventana.mainloop()