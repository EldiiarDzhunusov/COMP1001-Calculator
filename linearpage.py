import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import mainmenu
import polynomialpage

def page():

    lin1 = Tk()
    lin1.title("Polynomial Graph")
    lin1.geometry("1400x1000")
    lin1.configure(background = "cyan3")

    Label(lin1, text="Linear",background = "cyan3",font =("arial",20, "bold")).pack()
    Label(lin1, text="Write everything in the form of mx+b: ",background = "cyan3",font =("arial",20, "bold")).place(x=450,y=50)

    Label(lin1, text="m: ",background = "cyan3").place(x=600, y=200)
    Label(lin1, text="b: ",background = "cyan3").place(x=600, y=225)

    e1 = Entry(lin1, bd=2)
    e1.place(x=625, y=200)

    e2 = Entry(lin1, bd=2)
    e2.place(x=625, y=225)


    # to draw
    def draw(x1, y1):
        plt.plot(x1, y1)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Linear Graph')
        plt.show()

    def do_it():
        a = (float(e1.get()))
        b = (float(e2.get()))

        x = np.arange(-20, 20, 0.1)

        y = (a * x + b)
        draw(x, y)

    def exitpage():
        lin1.destroy()

    def back():
        lin1.destroy()
        polynomialpage.page()

    def home():
        lin1.destroy()
        mainmenu.page()

    Button(lin1, text="Calculate", command=do_it).place(x=650, y=300)
    Button(lin1, text="Home", command=home).place(x=657, y=330)
    Button(lin1, text="Back", command=back).place(x=660, y=360)
    Button(lin1, text="Exit", command=exitpage).place(x=665, y=390)

    lin1.mainloop()
