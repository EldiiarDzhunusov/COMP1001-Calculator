import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import mainmenu
import trigonometrypage


def page():

    tan1 = Tk()
    tan1.title("Trigonometry Graph")
    tan1.geometry("1400x1000")
    tan1.configure(background = "LightSalmon3")

    Label(tan1, text="Tangent",background = "LightSalmon3",font =("arial",20, "bold")).pack()
    Label(tan1, text="Write everything in the form of a(tan(b*x+c)): ",background = "LightSalmon3",font =("arial",20, "bold")).place(x=450,y=50)

    Label(tan1, text="a: ",background = "LightSalmon3").place(x=600, y=200)
    Label(tan1, text="b: ",background = "LightSalmon3").place(x=600, y=225)
    Label(tan1, text="c: ",background = "LightSalmon3").place(x=600, y=250)

    e1 = Entry(tan1, bd=2)
    e1.place(x=625, y=200)

    e2 = Entry(tan1, bd=2)
    e2.place(x=625, y=225)

    e3 = Entry(tan1, bd=2)
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

        y = (a * np.tan(b * x + c))
        draw(x, y)

    def exitpage():
        tan1.destroy()

    def back():
        tan1.destroy()
        trigonometrypage.page()

    def home():
        tan1.destroy()
        mainmenu.page()

    Button(tan1, text="Calculate", command=do_it).place(x=650, y=300)
    Button(tan1, text="Home", command=home).place(x=657, y=330)
    Button(tan1, text="Back", command=back).place(x=660, y=360)
    Button(tan1, text="Exit", command=exitpage).place(x=665, y=390)

    tan1.mainloop()
