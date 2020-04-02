import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import mainmenu
import trigonometrypage


def page():

    sin1 = Tk()
    sin1.title("Trigonometry Graph")
    sin1.geometry("1400x1000")
    sin1.configure(background = "salmon1")

    Label(sin1, text="Sine",background = "salmon1",font =("arial",20, "bold")).pack()
    Label(sin1, text="Write everything in the form of a(sin(b*x+c)): ",background = "salmon1",font =("arial",20, "bold")).place(x=450,y=50)

    Label(sin1, text="a: ",background = "salmon1").place(x=600, y=200)
    Label(sin1, text="b: ",background = "salmon1").place(x=600, y=225)
    Label(sin1, text="c: ",background = "salmon1").place(x=600, y=250)

    e1 = Entry(sin1, bd=2)
    e1.place(x=625, y=200)

    e2 = Entry(sin1, bd=2)
    e2.place(x=625, y=225)

    e3 = Entry(sin1, bd=2)
    e3.place(x=625, y=250)

    # to draw
    def draw(x1, y1):
        plt.plot(x1, y1)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Sine Graph')
        plt.show()


    def do_it():
        a = (float(e1.get()))
        b = (float(e2.get()))
        c = (float(e3.get()))

        x = np.arange(-20, 20, 0.1)

        y = (a * np.sin(b * x + c))
        draw(x, y)

    def exitpage():
        sin1.destroy()

    def back():
        sin1.destroy()
        trigonometrypage.page()

    def home():
        sin1.destroy()
        mainmenu.page()

    Button(sin1, text="Calculate", command=do_it).place(x=650, y=300)
    Button(sin1, text="Home", command=home).place(x=657, y=330)
    Button(sin1, text="Back", command=back).place(x=660, y=360)
    Button(sin1, text="Exit", command=exitpage).place(x=665, y=390)

    sin1.mainloop()
