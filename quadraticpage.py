import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import mainmenu
import polynomialpage


def page():

    qua1 = Tk()
    qua1.title("Polynomial Graph")
    qua1.geometry("1400x1000")
    qua1.configure(background = "plum2")

    Label(qua1, text="Quadratic",background = "plum2",font =("arial",20, "bold")).pack()
    Label(qua1, text="Write everything in the form of ax^2+bx+c: ",background = "plum2",font =("arial",20, "bold")).place(x=450,y=50)

    Label(qua1, text="a: ",background = "plum2").place(x=600, y=200)
    Label(qua1, text="b: ",background = "plum2").place(x=600, y=225)
    Label(qua1, text="c: ",background = "plum2").place(x=600, y=250)

    e1 = Entry(qua1, bd=2)
    e1.place(x=625, y=200)

    e2 = Entry(qua1, bd=2)
    e2.place(x=625, y=225)

    e3 = Entry(qua1, bd=2)
    e3.place(x=625, y=250)

    # to draw
    def draw(x1, y1):
        plt.plot(x1, y1)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Quadratic Graph')
        plt.show()

    def do_it():
        a = (float(e1.get()))
        b = (float(e2.get()))
        c = (float(e3.get()))

        x = np.arange(-20, 20, 0.1)

        y = (a*(x**2) +b*x +c)
        draw(x, y)

    def exitpage():
        qua1.destroy()

    def back():
        qua1.destroy()
        polynomialpage.page()

    def home():
        qua1.destroy()
        mainmenu.page()

    Button(qua1, text="Calculate", command=do_it).place(x=650, y=300)
    Button(qua1, text="Home", command=home).place(x=657, y=330)
    Button(qua1, text="Back", command=back).place(x=660, y=360)
    Button(qua1, text="Exit", command=exitpage).place(x=665, y=390)

    qua1.mainloop()
