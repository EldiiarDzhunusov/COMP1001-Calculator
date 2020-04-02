import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import mainmenu
import trigonometrypage


def page():
    cos1 = Tk()
    cos1.title("Trigonometry Graph")
    cos1.geometry("1400x1000")
    cos1.configure(background = "light blue")

    Label(cos1, text="Cosine",font =("arial",20, "bold"),background = "light blue").pack()
    Label(cos1, text="Write everything in the form of a(cos(b*x+c)): ",background = "light blue",font =("arial",20, "bold")).place(x=450,y=50)

    Label(cos1, text="a: ",background = "light blue").place(x=600, y=200)
    Label(cos1, text="b: ",background = "light blue").place(x=600, y=225)
    Label(cos1, text="c: ",background = "light blue").place(x=600, y=250)

    e1 = Entry(cos1, bd=2)
    e1.place(x=625, y=200)

    e2 = Entry(cos1, bd=2)
    e2.place(x=625, y=225)

    e3 = Entry(cos1, bd=2)
    e3.place(x=625, y=250)

    # to draw
    def draw(x1, y1):
        plt.plot(x1, y1)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Cosine Graph')
        plt.show()

    def do_it():
        a = (float(e1.get()))
        b = (float(e2.get()))
        c = (float(e3.get()))

        x = np.arange(-20, 20, 0.1)

        y = (a * np.cos(b * x + c))
        draw(x, y)

    def exitpage():
        cos1.destroy()

    def back():
        cos1.destroy()
        trigonometrypage.page()

    def home():
        cos1.destroy()
        mainmenu.page()

    Button(cos1, text="Calculate", command=do_it).place(x=650, y=300)
    Button(cos1, text="Home", command=home).place(x=657, y=330)
    Button(cos1, text="Back", command=back).place(x=660, y=360)
    Button(cos1, text="Exit", command=exitpage).place(x=665, y=390)
    cos1.mainloop()
